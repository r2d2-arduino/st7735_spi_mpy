from st7735_spi_fb import ST7735_SPI_FB
from pio_spi import PIO_SPI
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

SCREEN_WIDTH  = tft.width
SCREEN_HEIGHT = tft.height

COLOR_BLACK   = tft.color565( 0, 0, 0 )
COLOR_BLUE    = tft.color565( 0, 0, 255 )
COLOR_RED     = tft.color565( 255, 0, 0 )
COLOR_GREEN   = tft.color565( 0, 255, 0 )
COLOR_CYAN    = tft.color565( 0, 255, 255 )
COLOR_MAGENTA = tft.color565( 255, 0, 255 )
COLOR_YELLOW  = tft.color565( 255, 255, 0 )
COLOR_WHITE   = tft.color565( 255, 255, 255 )
COLOR_GRAY    = tft.color565( 112, 160, 112 )

tft.fill(COLOR_BLACK) # Fill the screen with black color

start = ticks_ms()

tft.ellipse(SCREEN_WIDTH >> 1, SCREEN_HEIGHT >> 1, (SCREEN_WIDTH >> 1) - 1, (SCREEN_WIDTH >> 1) - 1, COLOR_BLUE)

tft.ellipse(SCREEN_WIDTH >> 2, SCREEN_HEIGHT - (SCREEN_HEIGHT >> 2) + 16, SCREEN_WIDTH >> 2, SCREEN_WIDTH >> 2, COLOR_YELLOW, True)

tft.rect(10, 10, (SCREEN_WIDTH >> 1) - 20, SCREEN_HEIGHT >> 2, COLOR_RED)

tft.rect(10, SCREEN_HEIGHT // 3, (SCREEN_WIDTH >> 1) - 20, SCREEN_HEIGHT >> 2, COLOR_MAGENTA, True)

for y in range(SCREEN_HEIGHT // 8):
    tft.line(0, 0, SCREEN_WIDTH, y * 8 , COLOR_GREEN)
tft.show()

print((ticks_ms()-start), 'ms')

#s3m8 19 ms
#dma  3 + 6
