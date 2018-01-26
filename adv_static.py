#!/usr/bin/env python
"""Play a fixed frequency sound."""
from __future__ import division
import pygame
import numpy as np
import math
from time import sleep

from pyaudio import PyAudio # sudo apt-get install python{,3}-pyaudio

try:
    from itertools import izip
except ImportError: # Python 3
    izip = zip
    xrange = range

def sine_tone(frequency, duration=2, volume=1, sample_rate=22050):
    n_samples = int(sample_rate * duration)
    restframes = n_samples % sample_rate

    s = lambda t: volume * math.sin(2 * math.pi * frequency * t / sample_rate)
    samples = list(int(s(t) * 0x7f + 0x80) for t in xrange(n_samples))
    sound = pygame.sndarray.make_sound(np.asarray(samples))
    sound.play()


screen = pygame.display.set_mode((150, 150))
pygame.mixer.init(22050, -16, 1, 2048)

sine_tone(220.000)
sleep(1)
sine_tone(246.942)
sleep(1)
sine_tone(261.626)
sleep(1)
sine_tone(293.665)
sleep(1)
sine_tone(329.628)
sleep(1)
sine_tone(349.228)
sleep(1)
sine_tone(391.995)
sleep(1)

