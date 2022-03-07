import math
import warnings
warnings.filterwarnings('ignore')

import numpy as np
from scipy.signal import butter, filtfilt

def butter_bandpass_filter(data, lowcut, highcut, sample_rate, order):
    '''
    Returns bandpass filtered data between the frequency ranges specified in the input.

    Args:
        data (numpy.ndarray): array of samples. 
        lowcut (float): lower cutoff frequency (Hz).
        highcut (float): lower cutoff frequency (Hz).
        sample_rate (float): sampling rate (Hz).
        order (int): order of the bandpass filter.

    Returns:
        (numpy.ndarray): bandpass filtered data.
    '''
    
    nyq = 0.5 * sample_rate
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    y = filtfilt(b, a, data)
    return y

def get_filtered_eeg(eeg, lowcut, highcut, order, sample_rate):
    '''
    Returns bandpass filtered eeg for all channels and trials.

    Args:
        eeg (numpy.ndarray): raw eeg data of shape (num_classes, num_channels, num_samples, num_trials).
        lowcut (float): lower cutoff frequency (Hz).
        highcut (float): lower cutoff frequency (Hz).
        order (int): order of the bandpass filter.
        sample_rate (float): sampling rate (Hz).

    Returns:
        (numpy.ndarray): bandpass filtered eeg of shape (num_classes, num_channels, num_samples, num_trials).
    '''
    
    num_classes = eeg.shape[0]
    num_chan = eeg.shape[1]
    total_trial_len = eeg.shape[2]
    num_trials = eeg.shape[3]
    
    trial_len = int(125+0.14*sample_rate+2*sample_rate+0.2*sample_rate-1) - int(125+0.14*sample_rate) - int(0.2*sample_rate)
    filtered_data = np.zeros((eeg.shape[0], eeg.shape[1], trial_len, eeg.shape[3]))

    for target in range(0, num_classes):
        for channel in range(0, num_chan):
            for trial in range(0, num_trials):
                signal_to_filter = np.squeeze(eeg[target, channel, int(125+0.14*sample_rate):
                                               int(125+0.14*sample_rate+2*sample_rate+0.2*sample_rate-1) - int(0.2*sample_rate), 
                                               trial])
                filtered_data[target, channel, :, trial] = butter_bandpass_filter(signal_to_filter, lowcut, 
                                                                                  highcut, sample_rate, order)
    return filtered_data

def buffer(data, duration, data_overlap):
    '''
    Returns segmented data based on the provided input window duration and overlap.

    Args:
        data (numpy.ndarray): array of samples. 
        duration (int): window length (number of samples).
        data_overlap (int): number of samples of overlap.

    Returns:
        (numpy.ndarray): segmented data of shape (number_of_segments, duration).
    '''
    
    number_segments = int(math.ceil((len(data) - data_overlap)/(duration - data_overlap)))
    temp_buf = [data[i:i+duration] for i in range(0, len(data), (duration - int(data_overlap)))]
    temp_buf[number_segments-1] = np.pad(temp_buf[number_segments-1],
                                         (0, duration-temp_buf[number_segments-1].shape[0]),
                                         'constant')
    segmented_data = np.vstack(temp_buf[0:number_segments])
    
    return segmented_data

def get_segmented_epochs(data, window_len, shift_len, sample_rate):
    '''
    Returns epoched eeg data based on the window duration and step size.

    Args:
        data (numpy.ndarray): array of samples. 
        window_len (int): window length (seconds).
        shift_len (int): step size (seconds).
        sample_rate (float): sampling rate (Hz).

    Returns:
        (numpy.ndarray): epoched eeg data of shape. 
        (num_classes, num_channels, num_trials, number_of_segments, duration).
    '''
    
    num_classes = data.shape[0]
    num_chan = data.shape[1]
    num_trials = data.shape[3]
    
    duration = int(window_len*sample_rate)
    data_overlap = (window_len - shift_len)*sample_rate
    
    number_of_segments = int(math.ceil((data.shape[2] - data_overlap)/
                                       (duration - data_overlap)))
    
    segmented_data = np.zeros((data.shape[0], data.shape[1], 
                               data.shape[3], number_of_segments, duration))

    for target in range(0, num_classes):
        for channel in range(0, num_chan):
            for trial in range(0, num_trials):
                segmented_data[target, channel, trial, :, :] = buffer(data[target, channel, :, trial], 
                                                                      duration, data_overlap) 
    
    return segmented_data
