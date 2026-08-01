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

COLOR_BLACK   = tft.rgb( 0, 0, 0 )
COLOR_BLUE    = tft.rgb( 0, 0, 255 )
COLOR_RED     = tft.rgb( 255, 0, 0 )
COLOR_GREEN   = tft.rgb( 0, 255, 0 )
COLOR_CYAN    = tft.rgb( 0, 255, 255 )
COLOR_MAGENTA = tft.rgb( 255, 0, 255 )
COLOR_YELLOW  = tft.rgb( 255, 255, 0 )
COLOR_WHITE   = tft.rgb( 255, 255, 255 )
COLOR_GRAY    = tft.rgb( 112, 160, 112 )

tft.set_font(bigFont)
tft.set_rotation(0) # 0..3 - Rotates the screen

tft.fill(COLOR_BLACK) # Fill the screen with black color

row = tft.font.height()

tft.draw_text('RED', 4, row * 0, COLOR_RED)
tft.draw_text('GREEN', 4, row * 1, COLOR_GREEN)
tft.draw_text('BLUE', 4, row * 2, COLOR_BLUE)
tft.draw_text('CYAN', 4, row * 3, COLOR_CYAN)
tft.draw_text('MAGENTA', 4, row * 4, COLOR_MAGENTA)
tft.draw_text('YELLOW', 4, row * 5, COLOR_YELLOW)
tft.draw_text('WHITE', 4, row * 6, COLOR_WHITE)
tft.draw_text('GRAY', 4, row * 7, COLOR_GRAY)

start = ticks_ms()

tft.show()
while tft.dma.active():
    pass
print('DMA:', (ticks_ms()-start), 'ms') # 6 ms


