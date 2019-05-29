from gpiozero import Button, LED
from time import sleep
import random

buttons = [Button(2), Button(3), Button(4), Button(17)]
leds = [LED(18), LED(23), LED(24), LED(25)]

sequence = []

def lights_on():
    for led in leds:
        led.on()
    
def lights_off():
    for led in leds:
        led.off()

def flash_all():
    for _ in range(3):
        lights_on()
        sleep(0.25)
        lights_off()
        sleep(0.25)

lights_off()

while True:
# Add a new light to the end of the sequence
    new_light = random.choice(leds)
    sequence.append(new_light)

# Flash all before playback
    flash_all()

# play the sequence
    for light in sequence:
        light.on()
        sleep(0.5)
        light.off()
        sleep(0.25)

# get the player's input
    for light in sequence:
        guess = None
        while guess == None:
            for button in buttons:
                if button.is_pressed:
                    # convert button push to list index number
                    guess = buttons.index(button)
        
        if leds[guess] == light:
            light.on()
            sleep(0.5)
            light.off()
            sleep(0.25)
        else:
            print("You failed at level ", len(sequence))
            for _ in range(10):
                light.on()
                sleep(0.15)
                light.off()
                sleep(0.15)
            sequence = []
            break