from time import sleep

from stoppy import Stopwatch


stopwatch = Stopwatch(start=True)
sleep(1)
stopwatch.stop()
print(stopwatch.time())
stopwatch.reset()
