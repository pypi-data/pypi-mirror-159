"""sonusai pplot

usage: pplot [-hv] (-m MODEL) (-i INPUT) [-c CSVF] [-x MIXID] [-o OUTPUT]

options:
   -h, --help
   -v, --verbose                Be verbose.
   -m MODEL, --model MODEL      Trained model ONNX file.
   -i INPUT, --input INPUT      Input WAV or HDF5 feature+truth file (with mixture db).
   -c CSVF, --clabels CSVF      Optional .csv file of class labels (from Sonusai gentcst)
   -x MIXID, --mixid MIXID      Integer from 0 to #mixtures specifying the mixture
                                in the .HDF5 file. [Default: 0]
   -o OUTPUT, --output OUTPUT   Optional output HDF5 file for prediction

Run prediction on a .wav file using a SonusAI .onnx model and plot results.
Optionally the input can be an .hdf5 feature+truth file to include truth in the plots and
in that case the --mixid must be specified.

Inputs:
    MODEL   A SonusAI trained ONNX model file.
    INPUT   A WAV file; or an HDF5 file containing:
                dataset:    feature (optional)
                dataset:    truth
                dict:       mixdb

Outputs:
    .pdf file with plots
    predict.log

"""
import json
import time
from os.path import basename
from os.path import exists
from os.path import splitext
from pathlib import Path
from typing import List
from typing import Union

import h5py
import numpy as np
from docopt import docopt
from pyaaware import FeatureGenerator
from pyaaware import ForwardTransform
from pyaaware import Predict

import sonusai
from sonusai import SonusAIError
from sonusai import create_file_handler
from sonusai import initial_log_messages
from sonusai import logger
from sonusai import mixture
from sonusai import update_console_handler
from sonusai.mixture import read_audio
from sonusai.utils import int16_to_float
from sonusai.utils import seconds_to_hms
from sonusai.utils import trim_docstring


def plotmix(mixture: np.ndarray,
            target: Union[None, np.ndarray] = None,
            truth_f: Union[None, np.ndarray] = None,
            trlabels: Union[None, np.ndarray] = None,  # truth labels, default to 0,1,...
            predict: Union[None, np.ndarray] = None,
            prlabels: Union[None, np.ndarray] = None,  # prediction labels, default to 0,1,...
            mixdb: Union[None, dict] = None,
            mixid: Union[None, str, List[int]] = None,
            pdfname: Union[None, str, Path] = None,
            verbose: bool = False) -> None:
    """
    Plot mixture waveform with optional prediction and/or truth together
    in a single plot. The target waveform can optionally be provided, and
    prediction and truth can have be provided with multiple classes.
    Inputs:
      mixture     required, mixture waveform #samples x 1 nd.array
      truth_f     optional, numpy array of #frames x #truth classes to plot
      predict     optional, numpy array of #frames x #predictoin classes to plot

    """
    # (mx, tt, tr_f, trlabels, pr_f, prlabels, mixdb, mi, pdfname)
    # ----------- TBD make a func w/args mx, tt, tr_f, pr, mixdat, mi, trfi, tgpath -----------
    # plt.figure(figsize=(10, 8))
    # calc # samples per frame for plotting, should be int but check anyway

    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages

    # Check args for #frames to plot. Default is 1 frame for when there is just mixture (no truth or predict)
    NPLOTF = 0  # Num of plot frames
    if (truth_f is not None):
        NPLOTF = truth_f.shape[0]  # Frames to plot
        NTPLOTS = truth_f.shape[1]  # Number of truth plots
        if (prlabels is None):
            prlabels = ([f'Class {i}' for i in range(1, predict.shape[1])])

    if (predict is not None):
        NPLOTP = predict.shape[0]
        NPPLOTS = predict.shape[1]  # Number of predict plots
        if (prlabels is None):
            prlabels = ([f'Class {i}' for i in range(1, predict.shape[1])])
        if NPLOTF > 0:
            if NPLOTP != NPLOTF:
                print('Warning: plotmix predict frames not equal to truth frames, choosing the minimum.')
            NPLOTF = min(NPLOTF, NPLOTP)
        else:
            NPLOTF = NPLOTP

    if NPLOTF == 0:
        NPLOTF = 1  # Set default to 1 frame since there is no truth or predict data
    NPLOTSPF = int(np.floor(len(mixture) / NPLOTF))
    NPLOTSAM = int(NPLOTSPF * NPLOTF)  # number of plot samples multiple of frames
    secu = np.arange(NPLOTSAM, dtype=np.float32) / sonusai.mixture.SAMPLE_RATE  # x-axis in sec

    fig, ax0 = plt.subplots(1, 1, constrained_layout=True, figsize=(11.69, 8.27))
    ax = np.array([ax0], dtype=object)
    plots = []

    # Plot the time-domain waveforms then truth/prediction on second axis
    if mixture.shape[0] > 0:
        color = 'mistyrose'
        mix_plot, = ax[0].plot(secu, mixture[0:NPLOTSAM], color=color, label='MIX')
        ax[0].tick_params(axis='y', labelcolor='red')
        plots.append(mix_plot)

    if (target is not None):  # Plot target time-domain waveform
        color = 'tab:blue'
        tt_plot, = ax[0].plot(secu, target[0:NPLOTSAM], color=color, label='TAR')
        ax[0].set_ylabel('ampl', color=color)
        ax[0].tick_params(axis='y', labelcolor=color)
        plots.append(tt_plot)

    ax2 = ax[0].twinx()  # instantiate 2nd y axis that shares the same x-axis

    if (truth_f is not None):
        # Plot first truth TBD support multi-channel
        color = 'tab:green'
        label2 = 'tr-{}'.format(trlabels[0])
        ax2.set_ylabel(label2, color=color)  # we already handled the x-label with ax1
        # Reshape/extend truth to #samples in waveform
        trex = np.tile(truth_f[:, 0], (NPLOTSPF, 1)).reshape(NPLOTSAM, order='F')
        tr_plot, = ax2.plot(secu, trex[0:NPLOTSAM], color=color, label=label2)
        ax2.set_ylim([-0.05, 1.05])
        ax2.tick_params(axis='y', labelcolor=color)
        plots.append(tr_plot)

    if (predict is not None):
        # First prediction class plot
        color = 'tab:brown'
        labeltmp = 'pr{}'.format(prlabels[0])
        ax2.set_ylabel(labeltmp, color=color)  # we already handled the x-label with ax1
        prex = np.reshape(np.tile(np.expand_dims(predict, 1), [1, NPLOTSPF, 1]), [NPLOTSAM, NPPLOTS])
        pr_plot, = ax2.plot(secu, prex[:, 0], color=color, label=labeltmp)
        ax2.set_ylim([-0.05, 1.05])
        ax2.tick_params(axis='y', labelcolor=color)
        # nno_plot, = ax1.plot(secu, nnoex[:,1], 'k', label='NN Predict All')
        plots.append(pr_plot)

    ax[0].set_xlabel('time (s)')  # set only on last/bottom plot
    # Add info to plot:
    # ax[0].legend(handles=plots, bbox_to_anchor=(1.15, 1.0), loc='upper left')
    #
    # fig.suptitle('{} of {}: {}\n{}\nTarget aug: {}\nTruth indices: {}\nGlobal Truth Function:Config {} : {}'
    #              .format(mi + 1, NM, tgpath, tgfname, taugm, tridx, tfunc, tcfg), fontsize=10)
    # fig.tight_layout()

    if pdfname:
        pdf = PdfPages('{}'.format(pdfname))
        pdf.savefig(fig)
        pdf.close()

    plt.show()
    # os.system("""bash -c 'read -s -n 1 -p "Press any key to continue..."'""")
    print('\n')
    plt.close(fig)


def main():
    try:
        args = docopt(trim_docstring(__doc__), version=sonusai.__version__, options_first=True)

        verbose = args['--verbose']
        model_name = args['--model']
        input_name = args['--input']
        output_name = args['--output']
        label_name = args['--clabels']
        mixid = int(args['--mixid'])

        start_time = time.monotonic()

        log_name = 'predict.log'
        create_file_handler(log_name)
        update_console_handler(verbose)
        initial_log_messages('predict')

        logger.info('')
        logger.info(f'Model:  {model_name}')
        logger.info(f'Input:  {input_name}')
        logger.info(f'Output: {output_name}')
        logger.info('')

        model = Predict(model_name)
        logger.debug(f'Model feature name: {model.feature}')
        logger.debug(f'Model input shape {model.input_shape}')
        logger.debug(f'Model output shape {model.output_shape}')

        if not exists(input_name):
            raise SonusAIError(f'{input_name} does not exist')

        ext = splitext(input_name)[1]

        if ext == '.wav':
            audio = read_audio(input_name)

            fft = ForwardTransform(N=mixture.DEFAULT_FRAME_SIZE * 4, R=mixture.DEFAULT_FRAME_SIZE)
            fg = FeatureGenerator(frame_size=mixture.DEFAULT_FRAME_SIZE,
                                  feature_mode=model.feature,
                                  num_classes=1,
                                  truth_mutex=model.mutex)

            transform_frames = len(audio) // mixture.DEFAULT_FRAME_SIZE
            feature_frames = len(audio) // (mixture.DEFAULT_FRAME_SIZE * fg.decimation * fg.step)

            feature = np.empty((feature_frames, fg.stride, fg.num_bands), np.float32)
            mock_truth = np.empty(fg.num_classes)

            feature_frame = 0
            for transform_frame in range(transform_frames):
                indices = slice(transform_frame * mixture.DEFAULT_FRAME_SIZE,
                                (transform_frame + 1) * mixture.DEFAULT_FRAME_SIZE)
                fd = fft.execute(int16_to_float(audio[indices]))
                fg.execute(fd, mock_truth)
                if fg.eof():
                    feature[feature_frame] = fg.feature()
                    feature_frame += 1
        elif ext == '.h5':
            with h5py.File(name=input_name, mode='r') as f:
                feature = np.array(f['feature'])
                if 'truth_f' in f.keys():
                    logger.info('Found truth data FxNCL {}'.format(f['truth_f'].shape))
                    truth_f = np.array(f['feature'])
                if 'mixdb' in f.attrs.keys():
                    mixdb = json.loads(f.attrs['mixdb'])
                    print('Running prediction on mixture id {}'.format(mi))
                    mxinfo = mixdb['mixtures'][mi]
                    tinfo = mixdb['targets'][mxinfo['target_file_index']]
                    mxframes = int(mxinfo['samples'] / mixdb['feature_step_samples'])
                    tainfo = mixdb['target_augmentations'][mxinfo['target_augmentation_index']]
                    print('  Target file:                   {}'.format(tinfo['name']))
                    print('  Duration   :                   {}s'.format(tinfo['duration']))
                    print('  Samples, Features:             {}, {}'.format(mxinfo['samples'], mxframes))
                    print('  Target Augmentation:           {}'.format(tainfo))
                    # Truth activity
                    tr_act = np.any(tr_f >= mixdb['class_weights_threshold'], axis=0)  # true if active in any frame
                    tr_actidx = np.array([i for i, x in enumerate(tr_act) if x]) + 1
                    print('Truth active in classes: {}'.format(tr_actidx))
        else:
            raise SonusAIError(f'Unknown file type for {input_name}')

        logger.debug(f'Data Input shape {feature.shape}')
        predict = model.execute(feature)
        if label_name:
            # TBD read the .csv file
            logger.debug('Read labels from {}'.format(label_name))
        else:
            prlabels = ([f'Class {i}' for i in range(1, predict.shape[1] + 1)])

        predict_max = np.max(predict, axis=0)
        # Report the highest-scoring classes and their scores.
        p_top5 = np.argsort(predict_max)[::-1][:5]
        dfname = basename(splitext(input_name)[0])  # base data filename
        logger.info('Top 5 active prediction classes by max:')
        logger.info('\n'.join('  {:12s}: {:.3f}'.format(prlabels[i], predict_max[i])
                              for i in p_top5))

        if 'mixdb' in locals():
            pdfname = "./{}-mix{}-pplot.pdf".format(dfname, mi)
            plotmix(audio, _, truth_f, )
        else:
            pdfname = "./{}-pplot.pdf".format(dfname)
            plotmix(mixture=audio,
                    predict=predict,
                    prlabels=[prlabels[i] for i in p_top5],
                    pdfname=pdfname
                    )

        if output_name:
            with h5py.File(name=output_name, mode='w') as f:
                f.create_dataset(name='predict', data=predict)
                logger.info(f'Wrote {output_name}')

        end_time = time.monotonic()
        logger.info(f'Completed in {seconds_to_hms(seconds=end_time - start_time)}')

    except KeyboardInterrupt:
        logger.info('Canceled due to keyboard interrupt')
        raise SystemExit(0)


if __name__ == '__main__':
    main()
