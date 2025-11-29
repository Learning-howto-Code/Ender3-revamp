import time
import requests
import board
import neopixel

# -----------------------------
# CONFIGURATION
# -----------------------------

API_KEY = "YOUR_API_KEY"
OCTO_URL = "http://192.168.x.x/api/job"      # Replace with your OctoPrint address

LED_PIN = board.D18                          # GPIO pin for NeoPixel data
NUM_LEDS = 30                                # total number of LEDs on the strip
BRIGHTNESS = 0.4                             # 0.0–1.0

UPDATE_INTERVAL = 2.0                        # seconds between polls

# -----------------------------
# SETUP
# -----------------------------

pixels = neopixel.NeoPixel(
    LED_PIN,
    NUM_LEDS,
    brightness=BRIGHTNESS,
    auto_write=False,
    pixel_order=neopixel.GRB
)

headers = {"X-Api-Key": API_KEY}


# -----------------------------
# FUNCTIONS
# -----------------------------

def get_progress():
    """Return float progress 0–100 or None if unavailable."""
    try:
        r = requests.get(OCTO_URL, headers=headers, timeout=3)
        data = r.json()
        return data["progress"]["completion"]
    except:
        return None


def show_progress_on_strip(percent):
    """Light up a portion of the strip based on percent."""
    if percent is None:
        pixels.fill((0, 0, 0))
        pixels.show()
        return

    # how many LEDs should be on
    leds_on = int((percent / 100.0) * NUM_LEDS)

    for i in range(NUM_LEDS):
        if i < leds_on:
            pixels[i] = (0, 150, 0)       # green for "completed"
        else:
            pixels[i] = (0, 0, 0)         # off

    pixels.show()


# -----------------------------
# MAIN LOOP
# -----------------------------

while True:
    progress = get_progress()
    print("Progress:", progress)

    show_progress_on_strip(progress)

    time.sleep(UPDATE_INTERVAL)

