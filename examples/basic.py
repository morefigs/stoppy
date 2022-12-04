from time import sleep

from stopwatch import Stopwatch


stopwatch = Stopwatch(start=True)
sleep(1)
stopwatch.stop()
print(stopwatch.time())
stopwatch.reset()
