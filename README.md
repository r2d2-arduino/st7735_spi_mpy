# st7735_spi_mpy
MicroPython driver for ST7735 SPI displays.

## File Structure:
* **examples/** - a set of examples for using the library ST7735_SPI.
* **examples_fb/** - a set of examples for using the library ST7735_SPI_FB.
* **examples_dma/** - a set of examples for using the library ST7735_SPI_FB with DMA ( For pico only ).
* **resources/** - related files for examples.
* **st7735_spi.py** - Main library ST7735_SPI with direct draw.
* **st7735_spi_fb.py** - Main library ST7735_SPI_FB. Framebuffer and DMA version.
* **st7735_spi_base.py** - Base library for ST7735_SPI and ST7735_SPI_FB.

## Dependencies:
The main libraries inherit from the graphics libraries tft_draw:
https://github.com/r2d2-arduino/tft_draw

## Minimum code to run:
```python
from machine import SPI, Pin
from st7735_spi import ST7735_SPI

spi = SPI( 1, baudrate = 20_000_000, polarity = 1, phase = 1,
           sck = Pin(12), mosi = Pin(11) ) # Example for s3

# Set pins here
CS_PIN  = 10 #s3
DC_PIN  = 21
RST_PIN = 14
BLK_PIN = 17 # Set to None if the display doesn't have a backlight pin

tft = ST7735_SPI( spi, CS_PIN, DC_PIN, RST_PIN, BLK_PIN )

tft.fill( tft.rgb( 255, 0, 0 ) ) # Fills the entire screen with red
```

## Display functions:
* **set_rotation ( rotation = 0 )** - Set orientation of Display, 0 = 0 degrees, 1 = 90 degrees, 2 = 180 degrees, 3 = 270 degrees.
* **invert_display ( on = True )** - Enables or disables color inversion on display.
* **tearing_effect ( on = True )** - Activate "Tearing effect".
* **idle_mode ( on = True )** - Enables or disables idle mode on display.
* **scroll ( delay = 5 )** - Scrolling on the screen at a given speed.
* **set_backlight ( duty = 1023 )** - Set Backlight PWM Pin: 0 - Backlight Off; 1023 - Backlight Max.
* **show ( )** - Displays the contents of the buffer on the screen ( Framebuffer version only ).
