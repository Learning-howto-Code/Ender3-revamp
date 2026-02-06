import board
import neopixel
import time
b = 1 #brighnesss

time.sleep(5)
pixels = neopixel.NeoPixel(
    board.D18,
     30,
     brightness=1.0,
     auto_write=False
)

for i in range(15):
    pixels[i] = (255,255,255)
    pixels.show()

time.sleep(10)

pixels[0] = (0,0,0)
pixels.show()

pixels.deinit()