import board
import neopixel
import time

NUM_LEDS = 30

pixels = neopixel.NeoPixel(
    board.D18,
    10,
    brightness=1.0,
    auto_write=False
)
pixels2 = neopixel.NeoPixel(
    board.D19,
    10,
    brightness=1.0,
    auto_write=False
)

pixels.fill((0, 0, 0))
pixels.show()
pixels2.fill((0, 0, 0))
pixels2.show()
time.sleep(0.1)
pixels.show()
pixels2.show()
time.sleep(0.5)

pixels.deinit()
pixels2.deinit()    