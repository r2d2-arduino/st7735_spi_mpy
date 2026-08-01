from machine import SPI, Pin
from st7735_spi import ST7735_SPI
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

tft = ST7735_SPI( spi, CS_PIN, DC_PIN,  RST_PIN, BLK_PIN,
                  height = 160, width = 128)
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

tft.fill_screen(COLOR_BLACK) # Fill the screen with black color

start = ticks_ms()

tft.draw_circle(SCREEN_WIDTH >> 1, SCREEN_HEIGHT >> 1, SCREEN_WIDTH >> 1, COLOR_BLUE, 2)

tft.fill_circle(SCREEN_WIDTH >> 2, SCREEN_HEIGHT - (SCREEN_HEIGHT >> 2) + 16, SCREEN_WIDTH >> 2, COLOR_YELLOW)

tft.draw_rect(10, 10, (SCREEN_WIDTH >> 1) - 20, SCREEN_HEIGHT >> 2, COLOR_RED, 2)

tft.fill_rect(10, SCREEN_HEIGHT // 3, (SCREEN_WIDTH >> 1) - 20, SCREEN_HEIGHT >> 2, COLOR_MAGENTA)

for y in range(SCREEN_HEIGHT // 8):
    tft.draw_line(0, 0, SCREEN_WIDTH, y * 8 , COLOR_GREEN)

print( ticks_ms() - start, 'ms')

#s3m8  1,079 ms
#pico2 267