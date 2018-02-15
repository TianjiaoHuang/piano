class Device():
    
    def __init__(self, keys, sounds, numpin):
        self.pins = [False] * numpin
        self.isPlaying = list(self.pins)
        self.keys = keys
        self.sounds = sounds

    def updateMapping(self, keys):
        self

    def updatePins(self):
        raise NotImplementedError

    def pressed(self, pin):
        return bool(self.pins[pin])

    def play(self):
        self.updatePins()
        # for all pins that in the keys
        for i in len(self.pins):
            pin = self.pins[i]
            if pin in self.keys:
                # if pin is on and it is not playing
                # play the sound and set isPlaying to True
                if pin and (not self.isPlaying[pin]):
                    self.sounds[self.keys[pin]].play()
                    self.isPlaying[pin] = True

                # if pin is not on and it is playing
                # fade the sound out in 100ms and set isPlaying to False
                elif (not pin) and self.isPlaying[pin]:
                    self.sounds[self.keys[pin]].fadeout(100)
                    self.isPlaying[pin] = False


                

    

    