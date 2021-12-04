# Example using PIO to drive a set of WS2812 LEDs.
import array, time
import rp2
from machine import Pin
from ws2812 import ws2812

# Configure the number of WS2812 LEDs.
NUM_LEDS = 160
PIN_NUM = 6

# the shape of the LED display
NUM_ROWS = 10
NUM_COLS = 16

class NeoPixel(object):

    def __init__(self, pin=PIN_NUM, num=NUM_LEDS, brightness=0.1):
        self.pin=pin
        self.num=num
        self.brightness=brightness
        self.numberOfRows=NUM_ROWS
        self.numberOfCols=NUM_COLS
        
        # Create the StateMachine with the ws2812 program, outputting on pin
        self.sm = rp2.StateMachine(0, ws2812, freq=8_000_000, sideset_base=Pin(PIN_NUM))

        # Start the StateMachine, it will wait for data on its FIFO.
        self.sm.active(1)

        # Display a pattern on the LEDs via an array of LED RGB values.
        self.buffer = array.array("I", [0 for _ in range(self.num)])
        
        # primary colour values in the order red, green, blue
        self.BLACK = ( 0,  0,  0)
        self.RED =   (15,  0,  0)
        self.GREEN = ( 0, 15,  0)
        self.BLUE =  ( 0,  0, 15)
        self.YELLOW= (15, 15,  0)
        self.CYAN =  ( 0, 15, 15)
        self.MAGENTA=(15,  0, 15)
        self.WHITE = (15, 15, 15)
        self.COLORS = [self.RED, self.YELLOW, self.GREEN, self.CYAN, self.BLUE, self.MAGENTA, self.WHITE,self.BLACK ]
        self.lattice = [self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.RED, self.RED, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.RED, self.RED, self.RED, self.CYAN, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.CYAN, self.RED, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN, self.RED, self.RED, self.RED, self.RED, self.RED, self.RED, self.CYAN, self.CYAN, self.RED, self.RED, self.CYAN,
                        self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN,
                        self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN, self.CYAN]
        
    ##########################################################################
    def pixels_show(self):
        ''' Update the LED display with the current pixels. '''
        dimmer_ar = array.array("I", [0 for _ in range(self.num)])
        for i,c in enumerate(self.buffer):
            # the pixel values are decoded as 0x00GGRRBB by the board
            r = int(((c >> 8) & 0xFF) * self.brightness)
            g = int(((c >> 16) & 0xFF) * self.brightness)
            b = int((c & 0xFF) * self.brightness)
            dimmer_ar[i] = (g<<16) + (r<<8) + b
        self.sm.put(dimmer_ar, 8)

    def pixels_raw(self, rawColour):
        ''' Fill the LED display with the raw colour. '''
        raw_array = array.array("I", [0 for _ in range(self.num)])
        for i in range(self.num):
            raw_array[i] = rawColour
        self.sm.put(raw_array, 8)


    def pixels_set(self, i, color):
        ''' Set the i-th pixel to the given colour. '''
        # the pixel values are decoded as 0x00GGRRBB by the board
        self.buffer[i] = int(
            ((color[0] & 0xFF) <<  8) + \
            ((color[1] & 0xFF) << 16) + \
            (color[2] & 0xFF) )

    def pixels_fill(self, color):
        ''' Fill all the pixels with the given colour. '''
        for i in range(len(self.buffer)):
            self.pixels_set(i, color)


    def color_chase(self, color, length):
        #for i in range(self.num):
        self.pixels_set(length, color)
            # time.sleep(wait)
            # self.pixels_show()
            # time.sleep(0.2)
     
    def wheel(self, pos):
        # Input a value 0 to 31 to get a color value.
        # The colours are a transition r - g - b - back to r.
        if pos < 0 or pos > 31:
            return (0, 0, 0)
        if pos < 10:
            return (31 - pos * 3, pos * 3, 0)
        if pos < 15:
            pos -= 10
            return (0, 31 - pos * 3,pos * 3)
        pos -= 15
        return (pos * 3, 0, 31 - pos * 3)
     
     
    def rainbow_cycle(self, wait):
        for j in range(256):
            for i in range(self.num):
                rc_index = (i * 256 // self.num) + j
                self.pixels_set(i, self.wheel(rc_index & 31))
            self.pixels_show()
            time.sleep(wait)
