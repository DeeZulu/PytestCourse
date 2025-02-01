import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def correct_number():
    return str(math.log(int(time.time())))
