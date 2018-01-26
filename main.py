from scipy.io import wavfile
import argparse
import numpy as np
import pygame
import sys
import warnings
import os
from time import sleep


def trimSoundArr(sounds):
    threshold = 10
    for n in range(0, len(sounds)):
        #trim front
        for i in range(0, len(sounds[n])):
            if (sounds[n][i] > threshold):
                break

        #trim back
        for j in range(len(sounds[n]) - 1, -1, -1):
            if (sounds[n][j] > threshold):
                break

        sounds[n] = sounds[n][i:j]


fileNames = [chr(alph) + str(num) for num in range(1, 7 + 1) for alph in range(ord('A'), ord('G') + 1)]
sounds = [wavfile.read(os.path.join('sound', 'ff.' + name + '.wav'))[1] for name in fileNames]
sounds = [[pair[0] for pair in sound] for sound in sounds]
trimSoundArr(sounds)
sounds = [np.asarray(sound) for sound in sounds]
fps, sound = wavfile.read(os.path.join('sound', 'ff.' + fileNames[0] + '.wav'))

for i in sounds[0]:
    print(i)
sounds = map(pygame.sndarray.make_sound, sounds)
#sounds = [pygame.mixer.Sound(os.path.join('sound', 'ff.' + name + '.wav')) for name in fileNames]
pygame.mixer.init(fps, -16, 1, 2048)
for sound in sounds:
    sound.play()
    sleep(0.5)
