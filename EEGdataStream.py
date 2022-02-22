from random import randint
from pyOpenBCI import OpenBCICyton
from pylsl import StreamInfo, StreamOutlet
import numpy as np
import time

SCALE_FACTOR_EEG = (4500000)/24/(2**23-1) #uV/count

print("Creating LSL stream for openBCI EEG data. \nName: openBCIdata\nID: openBCIdata8ch\n")
info_eeg = StreamInfo('openBCIdata', 'EEG', 8, 250, 'float32', 'openBCIdata8ch')
outlet_eeg=StreamOutlet(info_eeg)

def openBCIsample(sample):
    # data=np.array(board.start_stream(openBCIsample))*SCALE_FACTOR_EEG
    data=np.array([randint(100,600000) for i in range(0,8)])
    outlet_eeg.push_sample(data)
    print(data)

if __name__=='__main__':
    
    # board=OpenBCICyton(port='COM11', daisy=True)
    # board.start_stream(openBCIsample)

    #for development while in hostel
    s=0
    while True:
        openBCIsample(s)
        time.sleep(0.008)