import time

from pylsl import StreamInfo, StreamOutlet
info = StreamInfo(name='crosshairMarkers', type='Markers', channel_count=1,
                  channel_format='string', source_id='openBCIdata8ch')
# Initialize the stream.
outlet = StreamOutlet(info)

markers = {
        'start': ['START'],
        'stop': ['STOP'],
        'running': [99],
        }
i = 0  
while True:
    outlet.push_sample(markers['start'])
    time.sleep(5)
    outlet.push_sample(markers['stop'])
    time.sleep(1)