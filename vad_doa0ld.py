
import sys
import webrtcvad
import numpy as np
from mic_array import MicArray
from pixel_ring import pixel_ring
from phue import Bridge

b = Bridge('192.168.1.64')
b.connect()
light = b.lights
L1 = light[0]
L2 = light[1]
L1.brightness = 200
L2.brightness = 0
a = '1'

RATE = 16000
CHANNELS = 4
VAD_FRAMES = 10     # ms
DOA_FRAMES = 200    # ms


def main():
  while True:
    vad = webrtcvad.Vad(3)

    speech_count = 0
    chunks = []
    doa_chunks = int(DOA_FRAMES / VAD_FRAMES)

    try:
        with MicArray(RATE, CHANNELS, RATE * VAD_FRAMES / 1000)  as mic:
            L1 = light[0]
            L2 = light[1]



            for chunk in mic.read_chunks():
                # Use single channel audio to detect voice activity
                if vad.is_speech(chunk[0::CHANNELS].tobytes(), RATE):
                    speech_count += 1
                    sys.stdout.write('1')
                    
                else:
                    #sys.stdout.write('0')
                    pass

                #if L1 <= 200:
                    #if a == speech_count:
                        L1 -= 10
                        L2 += 10
                    #else:
                        L1 += 10
                        L2 -= 10
                #else:           
                       #pass

                sys.stdout.flush()

                chunks.append(chunk)
                if len(chunks) == doa_chunks:
                    if speech_count > (doa_chunks / 2):
                        frames = np.concatenate(chunks)
                        direction = mic.get_direction(frames)
                        pixel_ring.set_direction(direction)
                        #print('\n{}'.format(int(direction)))

                    speech_count = 0
                    chunks = []

               

    except KeyboardInterrupt:
        pass
        
    pixel_ring.off()


if __name__ == '__main__':
    main()
