from stoppy import Stopwatch


with Stopwatch() as stopwatch:
    for _ in range(3):
        # Calling `stopwatch.time(True)` is equivalent to calling `perf_counter()`, but starts from exactly zero
        print(stopwatch.time(True))
