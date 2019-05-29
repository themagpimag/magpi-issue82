# Torch demo
from gpiozero import Button, LED

light = LED(18)
button = Button(2)

while True:
    if button.is_pressed:
        light.on()
    else:
        light.off()