class Device():
    
    def __init__(self):
        self.pins = []
        self.is_playing = {k: False for k in keys}

    def update(self):
        raise NotImplementedError

    def pressed(self, pin):
        return bool(self.pins[pin])

    def play(self):
        pass

    

    