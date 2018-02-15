import json

import Sound
import Device.Device
import Device.MCP23017

sounds = Sound.getRecordedSoundDict('mf')
cfg = json.load(open('cfg/cfg.json'))

devices = [Device.makeDevice(d) for d in cfg['devices']]

while True:
    for d in devices:
        d.play()
