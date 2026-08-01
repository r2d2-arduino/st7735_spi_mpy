from machine import SPI, Pin
from st7735_spi_fb import ST7735_SPI_FB
import resources.LibreBodoni20 as bigFont
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

COLOR_BLACK   = tft.color565( 0, 0, 0 )
COLOR_BLUE    = tft.color565( 0, 0, 255 )
COLOR_RED     = tft.color565( 255, 0, 0 )
COLOR_GREEN   = tft.color565( 0, 255, 0 )
COLOR_CYAN    = tft.color565( 0, 255, 255 )
COLOR_MAGENTA = tft.color565( 255, 0, 255 )
COLOR_YELLOW  = tft.color565( 255, 255, 0 )
COLOR_WHITE   = tft.color565( 255, 255, 255 )
COLOR_GRAY    = tft.color565( 112, 160, 112 )

tft.set_font(bigFont)
tft.set_rotation(0) # 0..3 - Rotates the screen

tft.fill(COLOR_BLACK) # Fill the screen with black color

start = ticks_ms()

text = " Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

tft.draw_text(text, 0, 0, COLOR_YELLOW)
tft.show()
print( ticks_ms() - start, 'ms')

#s3m8 23 ms
