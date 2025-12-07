# Ender3-revamp

My Ender 3 is feeling quite outdated, especially with everyone having an A1 Mini these days. A lot of the features my printer is missing are quite simple though, so I decided to make open-source versions of them.
This is my submision for Protoype, so please accept it. I've put a ton of effort into it and hope you understnad it

## TlDR
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

## Features!
-An LED task light!
  The corner of my room that my ender 3 lives in, and past 4:30 pm(when I normally do my printing)it is hard to see anything thats going on, which makes it very hard to see print quality or errors, feed filament etc. 
  The LED task light uses some standard 24v white LED's that I have extras of from a past project. They will be powered by a 24v plug in power supply and go in a slot in the bottom of my LED enclosure(Shown below). It will simply be toggles on off by a switch in the power supply.

![Screen Shot 2025-12-04 at 5 57 29 PM](https://github.com/user-attachments/assets/a4a2d1ce-a402-485f-af76-374602b6f619)

-Print progress bar!
One of the coolest features of Bambu Lab's new flagship printer, the H2d, is the LED progress bar on the side, which is way more convenient than looking at the tiny LCD display on the side of my printer. Mine will use 0.5 meter addressable neopixel LED strip cut down to length, that will be controlled via the Raspberry pi, using the octoprint API to determine how far along the print is done. The neopixel strip will be ordered from adafruit for $12.5( See BOM). The LED's will be masked by a 3d printed diffuser at 0% infill so that you can't see the individual LED's.
In the image above, this will go in the highlighted area labeled "neopixels will go here". 

-Octopint!
Octoprint is awesome opensource software that runs on a raspberry pi and allows you to control any 3d printer remotely. It communicates to the 3d printer via the micro-usb port, so that you dont have to go into the guts of the printer, and it allows you to start and monitor prints from you computer, phone, or crappy school chromebook. All you need for it is a raspberry pi, cable, and sd card(See BOM). This will go in the picture below, which has the Raspberry pi modled into it's enclosure

![Screen Shot 2025-12-04 at 5 49 46 PM](https://github.com/user-attachments/assets/f6b8e0da-7bff-487e-ac92-94ef919efc15)


-Camera for time elapses and print failure detection
Using the camera module 2 I already have from raspberry pi, I can uses octoprint to automatically take timealapses that have the toolhead home to the same spot each time, allowing for the fancy timealapses that you see on printers like the H2D. It also can locally run machine learning models that detect print failures, like the print coming loose, and send you an alert or stop the print autonomously. The camera will go into it's pictured slot in the pictured above, with a CSI ribbon cable connected to the raspberry pi. Like a said I chose this camera because I already have it on hand, and don't have to buy it.

P.S. This is my submission for Prototype, so please accept it, even if you want me to change a few minor things I will, I just really want to go to the hackathon :)









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
