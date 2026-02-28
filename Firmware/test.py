from wsgiref import headers
import requests
import os
import board
import neopixel
import time

pixels = neopixel.NeoPixel(
    board.D18,
     20,
     brightness=1.0,
     auto_write=False
)

URL = "192.168.4.206"
KEY = os.getenv("KEY")
def task_light(): #sets second 1/2 of lights to white
    for i in range(10,20):
        pixels[i] = (255,255,255)
        pixels.show()


r = requests.get(f"http://{URL}/api/job", headers={"X-Api-Key": KEY})
r.raise_for_status()

progress = r.json()["progress"]["completion"]
state = r.json()["state"]

if progress is None:
    progress = 0
else:
    progress = int(progress)
    progress = 20 / progress 
    progress =progress *100
    progress = int((progress / 100) *20)
if state == "Operational":
    task_light()

print(state)
data = r.json()


# print(data)