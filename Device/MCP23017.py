if __name__ != "__main__": 
    import smbus

def each_bit(byte):
    """return a generator that yield each bit of a byte

    >>> list(each_bit(0xf7))
    [1, 1, 1, 1, 0, 1, 1, 1]
    """
    mask = 1
    for i in range(8):
        yield mask & byte
        mask << 1

class MCP23017:    
    IODIRB  =   0x01
    IODIRA  =   0x00
    GPIOA   =   0x12 
    GPIOB   =   0x13 

    def __init__(self, address, busnum=1):
        self.address = address
        self.bus = smbus.SMBus(busnum)
        self.set_all_pins_to_input()

    def write(self, reg, val):
        return self.bus.write_byte_data(self.address, reg, val)
        
    def read(self, reg):
        return self.bus.read_byte_data(self.address, reg)

    def set_all_pins_to_input(self):
        self.write(self.IODIRA, 0xff)
        self.write(self.IODIRB, 0xff)
    
    def read_all_pins(self):
        lst = list(each_bit(self.read(self.GPIOA)))
        lst.extend(each_bit(self.read(self.GPIOB)))
        return lst

if __name__ == "__main__": 
    import doctest
    doctest.testmod()

    
        

