#!/usr/bin/env python3

import time
from gpiozero import LED

# GPIO pin 17
led = LED(17) 

# Should turn relay on for 1s
led.on()
time.sleep(1)
led.off()
time.sleep(1)