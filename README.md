# Ender3-revamp

My Ender 3 is feeling quite outdated, especially with everyone having an A1 Mini these days. A lot of the features my printer is missing are quite simple though, so I decided to make open-source versions of them.

## The Revamp
- LED task light to light up my print bed  
- LED NeoPixel print progress bar (like the H2D)  
- OctoPrint running on a Raspberry Pi  
- A Camera Module 2 for time-lapses and locally running print-failure detection

## CAD
For the CAD, I made an enclosure for both of the LED strips, with a 3D-printed diffuser, and an enclosure for the Raspberry Pi, camera, and a spot to hide the wires. The pink assembly will mount on the top of the 8020 extrusion like the filament spool holder, and the green assembly will mount to the back side of the same extrusion (shown as a blue box for reference).

![CAD 1](https://github.com/user-attachments/assets/80a55b2e-6016-4a32-98c8-13990f0ef013)
![CAD 2](https://github.com/user-attachments/assets/22a67e2a-1419-4740-8808-bf1fc825e233)
![CAD 3](https://github.com/user-attachments/assets/7b2603b4-702d-40e1-bf23-0c4a2bb9f2e1)
![CAD 4](https://github.com/user-attachments/assets/7e49f6a4-939e-4c34-bb40-dbe90f6bf157)

## BOM

| Item                     | Cost     | Link                                                                                                                                                  | Notes                                   |
|--------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| LED progress bar         | $12.50   | https://www.adafruit.com/product/3811                                                                                                                 |                                         |
| LED light                | $0.00    | N/A                                                                                                                                                    | I already have this!                    |
| Raspberry Pi 0 2W        | $20.00   | https://www.adafruit.com/product/5291                                                                                                                 | For OctoPi                              |
| 3D printed parts         | $0.00    | https://github.com/Learning-howto-Code/Ender3-revamp                                                                                                  | Printed on my Ender                     |
| Camera Module 2          | $0.00    | https://www.adafruit.com/product/3099?src=raspberrypi                                                                                                 | It’s outdated, but I already have it    |
| Micro USB cable (M→M)    | $3.00    | https://www.aliexpress.us/item/3256805347144024.html                                                                                                  | How OctoPi connects to the printer      |
| SD card                  | $3.30    | https://www.aliexpress.us/item/3256809364275848.html                                                                                                  | Actually a legit SD card from Kodak     |
| RPi power supply         | $7.00    | https://www.amazon.com/Adapter-Charger-Charging-Travel-iPhone/dp/B0DQ43LMRH                                                                           |                                         |
| RPi power cord           | $2.00    | https://www.aliexpress.us/item/3256806199963909.html                                                                                                  |                                         |
| Mounting hardware        | $0.00    | N/A                                                                                                                                                    | I will get these at Ace                 |
| **Total**                | **$47.80** |                                                                                                                                                        |                                         |

Made by Jake Hopkins for Blueprint, a part of Hack Club
