import board
import neopixel
import time

NUM_LEDS = 30

pixels = neopixel.NeoPixel(
    board.D18,
    NUM_LEDS,
    brightness=1.0,
    auto_write=False
)

pixels.fill((0, 0, 0))
pixels.show()
time.sleep(0.1)
pixels.show()
time.sleep(0.5)

pixels.deinit()