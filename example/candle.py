from microbit import pin1, pin2
import neopixel as np

NUM = 24
ring = np.NeoPixel(pin2, NUM)

def noise(pin=pin1, num=NUM, max_num=400):
    n = pin.read_analog()
    step = max_num // NUM
    m = n // step
    m = NUM - m # this is the only difference from noise detector
    if m > NUM:
        m = NUM
    for i in range(m):
        ring[i] = (10, 0, 0)
    ring.show()
    ring.clear()

while True:
    noise()
