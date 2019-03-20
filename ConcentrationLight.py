#================================================================================
# Script Name:
# by Wanting

# Description: it does this x x x x x
#================================================================================
import sys
import webrtcvad
import numpy as np
from mic_array import MicArray
from pixel_ring import pixel_ring
from phue import Bridge
#================================================================================
# Mic Variables
RATE = 16000
CHANNELS = 4
VAD_FRAMES = 10     # ms
DOA_FRAMES = 200    # ms
#================================================================================
# Hue Variables


#================================================================================

def get_response_from_ip(b):
    response = b.get_sensor_objects('phue')
    return response


#================================================================================
def main():

    b = Bridge('192.168.1.64')
    get_response_from_ip(b)
    lights = b.lights
    lights[0].brightness = 200
    lights[1].brightness = 0
    lights[0].hue = 33858
    lights[1].hue = 33858
    lights[1].hue = 65057
    lights[0].saturation = 44
    lights[1].saturation = 20
    second = 0

    while True:
        vad = webrtcvad.Vad(3)
        speech_count = 0
        chunks = []
        doa_chunks = int(DOA_FRAMES / VAD_FRAMES)

        try:
            with MicArray(RATE, CHANNELS, RATE * VAD_FRAMES / 1000)  as mic:
                for chunk in mic.read_chunks():
                    # Use single channel audio to detect voice activity
                    if vad.is_speech(chunk[0::CHANNELS].tobytes(), RATE):
                        speech_count += 1
                        second += 1
                        # sys.stdout.write(str(speech_count))
                        print (second)
                        if second == 200:
                            if lights[0].brightness >= 0:
                                lights[0].brightness -= 100
                                second = 0
                            # lights[0].brightness -= 10
                            # lights[1].brightness += 10
                            # lights[1].hue += 5
                            # if lights[1].saturation <= 254:
                            #     lights[1].hue -= 5
                    else:
                        # sys.stdout.write('0')
                        # if lights[0].brightness <= 200:
                            # lights[0].brightness +=1
                            # lights[0].brightness += 1
                            # lights[1].brightness -= 1
                            # if lights[1].saturation >= 20:
                            #     lights[1].hue -= 5

                    sys.stdout.flush()

                    chunks.append(chunk)
                    if len(chunks) == doa_chunks:
                        if speech_count > (doa_chunks / 2):
                            pass
                            # frames = np.concatenate(chunks)
                            # direction = mic.get_direction(frames)
                            # pixel_ring.set_direction(direction)
                            #print('\n{}'.format(int(direction)))

                        speech_count = 0
                        chunks = []

        except KeyboardInterrupt:
            pass

    pixel_ring.off()

#================================================================================
if __name__ == '__main__':
    main()
