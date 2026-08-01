from machine import SPI, Pin
from st7735_spi_fb import ST7735_SPI_FB
from time import ticks_ms

# For Esp32:    spi = 2, sck=Pin(18), mosi=Pin(23)
# For Esp32-S2: spi = 2, sck=Pin(36), mosi=Pin(35)
spi = SPI( 1, baudrate = 40_000_000, polarity = 1, phase = 1,
           sck = Pin(12), mosi = Pin(11) ) # Example for s3

# Set pins here
CS_PIN  = 10 #s3
DC_PIN  = 21
RST_PIN = 14
BLK_PIN = 17

tft = ST7735_SPI_FB( spi, CS_PIN, DC_PIN,  RST_PIN, BLK_PIN,
                     height = 160, width = 128)
#tft.invert_display( True )

def file_exists(filename):
    import os
    try:
        os.stat(filename)
        return True
    except OSError:
        print("File not found:", filename)
        return False

tft.set_rotation(0)  # 0..3 - Rotates the screen
tft.fill(0x0000) # Fill the screen with black color


filename = 'resources/road128x160.raw'
if file_exists(filename):
    start = ticks_ms()

    tft.draw_raw_image(filename, 0, 0, 128, 160)
    tft.show()
    print( ticks_ms() - start, 'ms')

#s3m8 48 ms