# Ender3-revamp

My Ender 3 is feeling quite outdated, especially with everyone having an A1 Mini these days. A lot of the features my printer is missing are quite simple though, so I decided to make open-source versions of them.

## The Revamp
- LED task light to light up my print bed (Basic white LED's)
- AdressableLED NeoPixel print progress bar (like the H2D)  
- OctoPrint running on a Raspberry Pi  
- A Camera Module 2 for time-lapses and locally running print-failure detection

## CAD
For the CAD, I made an enclosure for both of the LED strips, with a 3D-printed diffuser, and an enclosure for the Raspberry Pi, camera, and a spot to hide the wires. The pink assembly will mount on the top of the 8020 extrusion like the filament spool holder, and the green assembly will mount to the back side of the same extrusion (shown as a blue box for reference).

I know I wrote a lot here, but I prmise if you read it you will understand how my whole project works

Below is a zoomed out view of how it all works. there is a green piece I will 3d print that has the Rpi and camera(annotated). This will mount with m3 screws to the top extrusion of the ender 3.
![Screen Shot 2025-12-04 at 5 58 11 PM](https://github.com/user-attachments/assets/00170932-7bd9-48d1-8e19-322d61431a80)


Below is a zoomed in view of the LED assembly(in pink). It also mounts to the top extrusion of the ender 3. It has slots for both the addressable neopixels, which I'll buy from adafruit, and the bright 24v white tasklight LED's that I already have. The white ones aren't neopixels, and only for illluminaitng the dark corner of the room my printer is in.
![Screen Shot 2025-12-04 at 5 57 29 PM](https://github.com/user-attachments/assets/1a86b06e-85cb-43f7-adad-e44ff7767210)


Below is a zoomed in view of the electronics sub-assembly. It has the Rpi 02w, in green(annotated), and an arm to hold the camera(with m2.5 hardware). I drew in the ribbon cable because that kind of think doesn't work well in fusion, and I couldn't find a model for my camera, but I have an arrow showing where it will go(far left). This image is in gray to show the colors of the RPi, instead of the bright colors fusion generates to easily tell components apart.
![Screen Shot 2025-12-04 at 5 49 46 PM](https://github.com/user-attachments/assets/e0ec3385-4556-4552-8096-64c02995bc18)


Below is a zoomed out view of the electronics enclosure, showing how it fits in on a larger scale. It's a little confusing because one of the aluminum extrusions is also green, but this is NOT part of the design, and is a quirk of fusion. It has the same features metnioned above- the RPi, camera cable and spot for the camera. You can see that it mounts to the blue bar, which is the top of the Ender 3 gantry, and is also where the LED assembly will mount(Both will m2.5 hardware).


![Image 12-4-25 at 6 02 PM](https://github.com/user-attachments/assets/d32f6d00-8390-487a-a38c-e549a407aaec)







## BOM

| Item                     | Cost     | Link                                                                                                                                                  | Notes                                   |
|--------------------------|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|
| LED progress bar         | $12.50   | https://www.adafruit.com/product/3811                                                                                                                 |  I don't have any neopixels on hand, so I do have to buy this LED strip                                       |
| white LED light                | $0.00    |                                                                                                                                                    | I already have this, so I don't have to buy it                   |
| Raspberry Pi 0 2W        | $20.00   | https://www.adafruit.com/product/5291                                                                                                                 | For OctoPi                              |
| 3D printed parts         | $0.00    | https://github.com/Learning-howto-Code/Ender3-revamp                                                                                                  | Printed on my Ender                     |
| Camera Module 2          | $0.00    | https://www.adafruit.com/product/3099?src=raspberrypi                                                                                                 | It’s outdated, but I already have it    |
| Micro USB cable (M→M)    | $3.00    | https://www.aliexpress.us/item/3256805347144024.html                                                                                                  | How OctoPi connects to the printer      |
| SD card                  | $3.30    | https://www.aliexpress.us/item/3256809364275848.html                                                                                                  | Cheepst one that has enough storage     |
| RPi power supply         | $7.00    | https://www.amazon.com/Adapter-Charger-Charging-Travel-iPhone/dp/B0DQ43LMRH                                                                           |                                         |
| RPi power cord           | $2.00    | https://www.aliexpress.us/item/3256806199963909.html                                                                                                  |                                         |
| Mounting hardware        | $0.00    | N/A                                                                                                                                                    | I will get these at Ace                 |
| **Total**                | **$47.80** |                                                                                                                                                        |                                         |

Made by Jake Hopkins for Blueprint, a part of Hack Club
