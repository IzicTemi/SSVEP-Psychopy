import pylsl
from pylsl import resolve_stream,StreamInlet

import numpy as np

streams=resolve_stream('name','SSVEP_CCA')
inlet=StreamInlet(streams[0])

dtaArr=0

def getSignal():
    for i in range(0,625):
        if i==0:
            data=np.array(inlet.pull_sample()[0])
        else:
            data=np.vstack((data,np.array(inlet.pull_sample)[0]))

if __name__=='__main__':
    while True:
        print(inlet.pull_sample())