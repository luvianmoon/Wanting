#================================================================================
# Script Name: Concentration & light
# by Wanting

# Description: The project is about using respeaker to recognize human voice and use color and brightness to present it. When speech was detected, light 1 will go dark while the lught 2 burn bright at the same time. Light 2 will also turn into red color which will make people feel uncomfortable.
#================================================================================
import sys
import webrtcvad
import numpy as np
from mic_array import MicArray
from pixel_ring import pixel_ring
from phue import Bridge
import time
import os

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
    lights[1].hue = 65057
    lights[0].saturation = 44
    lights[1].saturation = 10
    countratenumber = 0

    while True:
        vad = webrtcvad.Vad(3)
        speech_count = 0
        chunks = []
        doa_chunks = int(DOA_FRAMES / VAD_FRAMES)

        try:
            with MicArray(RATE, CHANNELS, RATE * VAD_FRAMES / 1000)  as mic:
                for chunk in mic.read_chunks():
                    countratenumber += 1
                    if vad.is_speech(chunk[0::CHANNELS].tobytes(), RATE):
                        speech_count += 1
                        sys.stdout.write('1')
                        if countratenumber > 1000:
                            if lights[1].brightness <= 240:
                                lights[0].brightness -= 40
                                lights[1].brightness += 40
                                countratenumber = 0
                                # print ('lightis' + str(lights[1].saturation))
                                if lights[1].saturation <= 254:
                                    lights[1].saturation += 30


                    else:
                        sys.stdout.write('0')
                        if countratenumber > 1000:
                            if lights[0].brightness <= 200:
                                lights[0].brightness += 30
                                lights[1].brightness -= 30
                                countratenumber = 0
                                # print ('lightis' + str(lights[1].saturation))
                                if lights[1].saturation >= 20:
                                    lights[1].saturation -= 30


                    sys.stdout.flush()
                    chunks.append(chunk)
                    if len(chunks) == doa_chunks:
                        if speech_count > (doa_chunks / 2):
                            pass

                        speech_count = 0
                        chunks = []

        except KeyboardInterrupt:
            pass

        except PhueRequestTimeout:
            time.sleep(3)
            os.execv(sys.executable, ['ConcentrationLight.py'] + sys.argv)

    pixel_ring.off()

#================================================================================
if __name__ == '__main__':
    main()
