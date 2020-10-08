from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

blue = (0, 255, 0)
red = (255, 0, 0)

nothing = (0,0,0)


def f_initial():
    B = blue
    O = nothing
    logo = [
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, B, B, B, B, B, B, O,
    O, B, B, B, B, B, B, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
    O, B, B, O, O, B, B, O,
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