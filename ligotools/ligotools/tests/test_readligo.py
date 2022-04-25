import numpy as np
import os
import fnmatch

from ligotools import readligo as rl

def test_loaddata_H1():
    fn_H1 = 'H-H1_LOSC_4_V2-1126259446-32.hdf5'
    strain_H1, time_H1, channel_dict_H1 = rl.loaddata('data/'+fn_H1, 'H1')
    assert len(strain_H1) == len(time_H1)
    assert len(channel_dict_H1) != 0
    
    
def test_loaddata_L1():
    fn_L1 = 'L-L1_LOSC_4_V2-1126259446-32.hdf5'
    strain_L1, time_L1, channel_dict_L1 = rl.loaddata('data/'+fn_L1, 'L1')
    assert len(strain_L1) == len(time_L1)
    assert len(channel_dict_L1) != 0
    

def test_dq_channel_to_seglist():
    fn_H1 = 'H-H1_LOSC_4_V2-1126259446-32.hdf5'
    strain_H1, time_H1, channel_dict_H1 = rl.loaddata('data/'+fn_H1, 'H1')
    seglist = rl.dq_channel_to_seglist(channel_dict_H1)
    assert seglist[0] == 0
    assert seglist[1] == len(time_H1)
    assert seglist[2] is none
    
def test_getstrain():
    fn_L1 = 'L-L1_LOSC_4_V2-1126259446-32.hdf5'
    strain_L1, time_L1, channel_dict_L1 = rl.loaddata('data/'+fn_L1, 'L1')
    start, stop = time_L1[0], time_L1[-1]
    m_strain, meta, m_dq = rl.getstrain(start, stop, 'L1')
    assert len(m_strain) != 0
    assert meta['start'] == start
    assert len(m_dq) != 0
    