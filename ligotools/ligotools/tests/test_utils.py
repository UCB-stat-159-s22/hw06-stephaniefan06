import numpy as np
from scipy import signal
from scipy.interpolate import interp1d
from scipy.signal import butter, filtfilt, iirdesign, zpk2tf, freqz
import h5py
import json
import os

import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# Import LIGO-specific package ligotools
from ligotools import readligo as rl
from ligotools import utils


fn_H1 = 'H-H1_LOSC_4_V2-1126259446-32.hdf5'
fn_L1 = 'L-L1_LOSC_4_V2-1126259446-32.hdf5'

strain_H1, time_H1, chan_dict_H1 = rl.loaddata('data/'+fn_H1, 'H1')
strain_L1, time_L1, chan_dict_L1 = rl.loaddata('data/'+fn_L1, 'L1')

Pxx_H1, freqs = mlab.psd(strain_H1, Fs = 4096, NFFT = 4*4096)
psd_H1 = interp1d(freqs, Pxx_H1)
dt_H1 = time_H1[1] - time_H1[0]

def test_whiten():
    strain_H1_white = utils.whiten(strain_H1, psd_H1, dt_H1)
    assert len(strain_H1_whiten) == len(strain_H1)


def test_write_wavfile():
    eventname = 'GW150914'
    strain_H1_white = utils.whiten(strain_H1, psd_H1, dt_H1)
    utils.write_wavfile('test_write_wavfile',int(4096), strain_H1_whiten)
    assert os.path.isfile('audio/test_write_wavefile.wav') == True
    #os.remove('audio/test_write_wavfile.wav')


def test_reqshift():
    strain_H1_shifted = utils.reqshift(strain_H1,fshift=100,sample_rate=4096)
    assert len(strain_H1_shifted) == len(strain_H1)


def test_plotting():
    assert os.path.isfile('GW150914_ASDs.png')
    