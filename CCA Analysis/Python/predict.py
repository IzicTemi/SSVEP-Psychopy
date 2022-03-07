import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import numpy as np
import scipy.io as sio
from scripts import cca_module as cc
from scripts import ssvep_files as su

# data_path = os.path.abspath('../Dataset')
# all_segment_data = dict()
# all_acc = list()

# Set parameters
window_len = 2
shift_len = 1
sample_rate = 250
duration = int(window_len*sample_rate)
flicker_freq = np.array([9.25, 11.25, 13.25, 9.75, 11.75, 13.75, 
                       10.25, 12.25, 14.25, 10.75, 12.75, 14.75])

# Sample data for testing
# Replace with LSL data
dataset = sio.loadmat('D:\Desktop\Brain-computer-interfaces\Dataset\S004.mat')
eeg = np.array(dataset['data'], dtype='float32')
eeg = eeg[:,:,0,:,:]
eeg = np.squeeze(eeg)
eeg = np.transpose(eeg, (3, 0, 1, 2))

# Filter data
filtered_data = su.get_filtered_eeg(eeg, 7.25, 90, 2, sample_rate)
# Segment data
data = su.get_segmented_epochs(filtered_data, window_len, shift_len, sample_rate)

data = data[11, :, 1, 0, :]
key = cc.predicted_value(data)
print(key)