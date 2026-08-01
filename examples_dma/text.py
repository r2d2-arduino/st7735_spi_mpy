from st7735_spi_fb import ST7735_SPI_FB
from pio_spi import PIO_SPI
import resources.LibreBodoni20 as bigFont
from time import ticks_ms

# standart SPI dosn't work with dma
piospi = PIO_SPI( sck = 10, mosi = 11 )

CS_PIN  = 13 #pico
DC_PIN  = 20
RST_PIN = 21
BLK_PIN = 15 # Or None
    
tft = ST7735_SPI_FB( piospi, CS_PIN, DC_PIN, RST_PIN, BLK_PIN,
                      width = 128, height = 160, dma = True )
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
print((ticks_ms()-start), 'ms')

#s3m8 29 ms
#dma  23 + 6