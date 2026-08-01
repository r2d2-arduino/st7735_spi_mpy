from st7735_spi_fb import ST7735_SPI_FB
from pio_spi import PIO_SPI
import resources.LibreBodoni20 as bigFont
from resources.bitmaps import suncloud
from time import sleep_ms

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

tft.set_font(bigFont)
tft.tearing_effect()
tft.fill(COLOR_BLACK)
tft.show()

def rainbow( ):

    for y in range(0, 32):
        red    = tft.color565( y * 6 + 64, 0, 0 )
        yellow = tft.color565( y * 6 + 64, y * 6 + 64, 0 )
        green  = tft.color565( 0, y * 6 + 64, 0 )
        blue   = tft.color565( 0, 0, y * 6 + 64 )
        purple = tft.color565( y * 6 + 64, 0, y * 6 + 64 )
        
        tft.rect(0, y,       SCREEN_WIDTH, 1, red, True)
        tft.rect(0, y + 32,  SCREEN_WIDTH, 1, yellow, True)
        tft.rect(0, y + 64,  SCREEN_WIDTH, 1, green, True)
        tft.rect(0, y + 96,  SCREEN_WIDTH, 1, blue, True)
        tft.rect(0, y + 128, SCREEN_WIDTH, 1, purple, True)

    tft.show()

#bitmap
size = 16
for y in range( SCREEN_HEIGHT // size ):
    for x in range(  SCREEN_WIDTH // size ):
        tft.draw_bitmap(suncloud, x * size, y * size, COLOR_YELLOW)        
tft.show()
sleep_ms(500)

#red gradient
for y in range(0, 32):
    color = tft.color565( y * 8, 0, 0 )
    tft.rect(0, y * 5, SCREEN_WIDTH, 5, color, True)
    
tft.show()
sleep_ms(500)

#green gradient
for y in range(0, 32):
    color = tft.color565( 0, y * 8, 0 )
    tft.rect(0, y * 5, SCREEN_WIDTH, 5, color, True) 
tft.show()
sleep_ms(500)

#blue gradient
for y in range(0, 32):
    color = tft.color565( 0, 0, y * 8 )
    tft.rect(0, y * 5, SCREEN_WIDTH, 5, color, True) 
tft.show()
sleep_ms(500)


text = " Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

tft.set_rotation(1)
tft.fill(COLOR_RED)
tft.draw_text(text, 0, 0, COLOR_YELLOW)
tft.show()
sleep_ms(500)

tft.set_rotation(2)
tft.fill(COLOR_BLUE)
tft.draw_text(text, 0, 0, COLOR_WHITE)
tft.show()
sleep_ms(500)

tft.set_rotation(3)
tft.fill(COLOR_GREEN)
tft.draw_text(text, 0, 0, COLOR_MAGENTA)
tft.show()
sleep_ms(500)

tft.set_rotation(0)
tft.fill(COLOR_BLACK)
tft.draw_text(text, 0, 0, COLOR_WHITE)
tft.show()
sleep_ms(500)

rainbow()
sleep_ms(500)

tft.vert_scroll(0, tft.height, 0)
for _ in range(3):
    for line in range(SCREEN_HEIGHT):
        tft.vert_scroll_start_address(line + 1)
        sleep_ms(3) 
