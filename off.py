import board
import neopixel
import time

pixels = neopixel.NeoPixel(
    board.D18,
    20,
    brightness=1.0,
    auto_write=False
)

pixels.fill((0, 0, 0))
pixels.show()
time.sleep(0.1)
pixels.fill((0, 0, 0))
pixels.show()
time.sleep(0.5)

pixels.deinit()    