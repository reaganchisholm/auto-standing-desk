#!/usr/bin/env python3

from gpiozero import LED
from random import randint, choice
from time import sleep
import schedule

led = LED(17)
led.on() # on == off

# Switches pin off for 1s
def switchOn():
    led.off() # off == on
    sleep(1)
    led.on() # on == off 

# Makes desk stand up and then cancels the job
def standUp():
    print("Time to stand up!")
    switchOn()
    return schedule.CancelJob

# Generates 2 random hour:minutes and schedules the jobs
def setupStandTimes():
    randomHourOne = randint(8,11)
    randomMinOne = randint(1,59)
    randomHourTwo = randint(13,16)
    randomMinTwo = randint(1,59)

    randomTimeOne = f"{str(randomHourOne).zfill(2)}:{str(randomMinOne).zfill(2)}"
    randomTimeTwo = f"{str(randomHourTwo).zfill(2)}:{str(randomMinTwo).zfill(2)}"

    jobOne = schedule.every().day.at(randomTimeOne).do(standUp)
    jobTwo = schedule.every().day.at(randomTimeTwo).do(standUp)
    print(f"Will stand desk up at {randomTimeOne} and {randomTimeTwo} today")

    return jobOne, jobTwo 

# Generate new times at 8am on M,T,W,T,F
schedule.every().monday.at("08:00").do(setupStandTimes)
schedule.every().tuesday.at("08:00").do(setupStandTimes)
schedule.every().wednesday.at("08:00").do(setupStandTimes)
schedule.every().thursday.at("08:00").do(setupStandTimes)
schedule.every().friday.at("08:00").do(setupStandTimes)

while True:
    schedule.run_pending()
    sleep(1)
