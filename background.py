import time
import os


def sleeptime(hour, min, sec):
    return hour * 3600 + min * 60 + sec


second = sleeptime(0, 30, 0)
while True:
    os.system('')  # Do something commands
    time.sleep(second)
