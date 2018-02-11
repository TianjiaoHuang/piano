class Device():
    pins = []

    def __init__(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def pressed(self, pin):
        return bool(self.pins[pin])

    

    