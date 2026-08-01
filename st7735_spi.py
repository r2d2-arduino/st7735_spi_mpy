"""
ST7735_SPI display v 0.3.1

Display: ST7735
Connection: SPI
Colors: 16-bit
Controllers: Esp32-family, RP2
 
Project path: https://github.com/r2d2-arduino/st7735_spi_mpy
MIT License

Author: Arthur Derkach 
"""
from st7735_spi_base import ST7735_SPI_BASE
from tft_draw.draw_spi_c16 import DRAW_SPI_C16

class ST7735_SPI ( ST7735_SPI_BASE, DRAW_SPI_C16 ):
    
    def __init__( self, spi, cs_pin, dc_pin, rst_pin, blk_pin = None,
                  width = 128, height = 160, bgr = False ):
        """ Constructor
        Args
        spi  (object): SPI
        cs_pin  (int): Chip Select pin number
        dc_pin  (int): Data/Command pin number
        rst_pin (int): Reset pin number 
        blk_pin (int): Backlight pin number
        width   (int): Screen width in pixels (less)
        height  (int): Screen height in pixels
        bgr    (bool): Color order: False = RGB, True = BGR
        """        
        super().__init__( spi, cs_pin, dc_pin, rst_pin, blk_pin,
                  width, height, bgr )
        
        DRAW_SPI_C16.__init__( self, self.spi, self.cs, self.dc,
                               self.width, self.height, self.offset_x, self.offset_y )
        
        self.init()


    def set_rotation( self, rotation = 0 ):
        if self.height == self.width: #fix for 128x128 display
            self.fix_for_128x128(rotation)
            
        super().set_rotation( rotation )

            
    def fix_for_128x128( self, rotation ):
        if rotation == 0:
            self.offset_x = 2
            self.offset_y = 1
        if rotation == 1:
            self.offset_x = 1
            self.offset_y = 2
        if rotation == 2:
            self.offset_x = 2
            self.offset_y = 3
        if rotation == 3:
            self.offset_x = 3
            self.offset_y = 2  