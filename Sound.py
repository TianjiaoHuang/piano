#!/usr/bin/env python
import math
import os
import pygame
import numpy as np
from scipy.io import wavfile

pygame.mixer.init(44100, -16, 2, 4096)
keyNumbers = [89,90,91,92,93,94,95,96,97,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,98,99,100,101,102]
names = ['C0','C#0','D0','D#0','E0','F0','F#0','G0','G#0','A0','A#0','B0','C1','C#1','D1','D#1','E1','F1','F#1','G1','G#1','A1','A#1','B1','C2','C#2','D2','D#2','E2','F2','F#2','G2','G#2','A2','A#2','B2','C3','C#3','D3','D#3','E3','F3','F#3','G3','G#3','A3','A#3','B3','C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4','C5','C#5','D5','D#5','E5','F5','F#5','G5','G#5','A5','A#5','B5','C6','C#6','D6','D#6','E6','F6','F#6','G6','G#6','A6','A#6','B6','C7','C#7','D7','D#7','E7','F7','F#7','G7','G#7','A7','A#7','B7','C8','C#8','D8','D#8','E8','F8']
freqs = [16.3516,17.3239,18.3540,19.4454,20.6017,21.8268,23.1247,24.4997,25.9565,27.5000,29.1352,30.8677,32.7032,34.6478,36.7081,38.8909,41.2034,43.6535,46.2493,48.9994,51.9131,55.0000,58.2705,61.7354,65.4064,69.2957,73.4162,77.7817,82.4069,87.3071,92.4986,97.9989,103.826,110.000,116.541,123.471,130.813,138.591,146.832,155.563,164.814,174.614,184.997,195.998,207.652,220.000,233.082,246.942,261.626,277.183,293.665,311.127,329.628,349.228,369.994,391.995,415.305,440.000,466.164,493.883,523.251,554.365,587.330,622.254,659.255,698.456,739.989,783.991,830.609,880.000,932.328,987.767,1046.50,1108.73,1174.66,1244.51,1318.51,1396.91,1479.98,1567.98,1661.22,1760.00,1864.66,1975.53,2093.00,2217.46,2349.32,2489.02,2637.02,2793.83,2959.96,3135.96,3322.44,3520.00,3729.31,3951.07,4186.01,4434.92,4698.64,4978.03,5274.04,5587.65]

# generate a fixed frequency sound
def sine_tone(frequency, duration=2, volume=1, sample_rate=44100):
    n_samples = int(sample_rate * duration)
    max_volume, offset = 0x7f, 0

    s = lambda t: volume * math.sin(2 * math.pi * float(frequency) * t / float(sample_rate))
    samples = list(int(s(t) * max_volume + offset) for t in range(n_samples))
    samples = [[s, s] for s in samples] # for 2-channels
    return pygame.sndarray.make_sound(np.asarray(samples, dtype="int8"))

# return a dict that maps both number and name of each key to its sound
def getStaticSoundDict():
    sounds = [sine_tone(f) for f in freqs]
    d = dict(zip(names, sounds))
    d.update(dict(zip(keyNumbers, sounds)))
    return d

def trim2DSoundArr(sounds):
    threshold = 100
    for n in range(0, len(sounds)):
        #trim front
        for i in range(0, len(sounds[n])):
            if (sounds[n][i][0] > threshold):
                break

        #trim back
        for j in range(len(sounds[n]) - 1, -1, -1):
            if (sounds[n][j][0] > threshold):
                break

        sounds[n] = sounds[n][i:j]

def getRecordedSoundDict(dynamics):
    possibleDynamics = ['ff', 'mf', 'pp']
    if (not dynamics in possibleDynamics):
        raise ValueError("Invalid dynamic: " + dynamics)

    keyNames = [chr(alph) + str(num) for num in range(1, 7 + 1) for alph in range(ord('A'), ord('G') + 1)]
    sounds = [wavfile.read(os.path.join('sound', dynamics + name + '.wav'))[1] for name in keyNames]
    trim2DSoundArr(sounds)
    sounds = dict(zip(keyNames, sounds))
    return sounds

def main():
    from time import sleep
    '''
    sine_tone(220.000).play()
    sleep(1)
    sine_tone(246.942).play()
    sleep(1)
    sine_tone(261.626).play()
    sleep(1)
    sine_tone(293.665).play()
    sleep(1)
    sine_tone(329.628).play()
    sleep(1)
    sine_tone(349.228).play()
    sleep(1)
    sine_tone(391.995).play()
    sleep(1)
    '''

if __name__ == "__main__":
    main()