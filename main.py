from scipy.io import wavfile
import numpy as np
import pygame
import os
from time import sleep


def trimSoundArr(sounds):
    threshold = 100
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


sounds = map(pygame.sndarray.make_sound, sounds)
sounds = zip(fileNames, sounds)
screen = pygame.display.set_mode((150, 150))
pygame.mixer.init(fps, -16, 1, 2048)

with open('kb.kb') as file:
    keys = [line.strip() for line in file]
key_sound = dict(zip(keys, sounds))
is_playing = {k: False for k in keys}
while True:
        event = pygame.event.wait()

        if event.type in (pygame.KEYDOWN, pygame.KEYUP):
            key = pygame.key.name(event.key)

        if event.type == pygame.KEYDOWN:
            if (key in key_sound.keys()) and (not is_playing[key]):
                print(key_sound[key][0])
                key_sound[key][1].play()
                is_playing[key] = True

            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                break

        elif event.type == pygame.KEYUP and key in key_sound.keys():
            # Stops with 50ms fadeout
            #key_sound[key][1].fadeout(50)
            is_playing[key] = False