from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

blue = (0, 0, 255)
red = (255, 0, 0)

nothing = (0,0,0)


def f_initial():
    R = red
    O = nothing
    logo = [
    O, R, R, O, O, R, R, O,
    O, R, R, O, O, R, R, O,
    O, R, R, O, O, R, R, O,
    O, R, R, R, R, R, R, O,
    O, R, R, R, R, R, R, O,
    O, R, R, O, O, R, R, O,
    O, R, R, O, O, R, R, O,
    O, R, R, O, O, R, R, O,
    ]
    return logo

def s_initial():
    
    R = red
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    R, R, O, O, O, O, R, R,
    R, R, O, O, O, O, R, R, 
    O, R, O, O, O, O, R, O,
    O, R, O, O, O, O, R, O,
    O, O, R, R, R, R, O, O,
    O, O, O, R, R, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo


images = [f_initial, s_initial]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1