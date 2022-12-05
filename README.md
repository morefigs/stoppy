# stoppy ⏱

A precise and lightweight stopwatch built on top of `perf_counter`. Stopwatch can be used as a direct replacement for `perf_counter` that returns absolute timing starting from zero.

The stopwatch can optionally be started automatically by calling `time` instead of `start`, which can streamline usage when polling the time repeatedly.

## Installation

Install from [PyPI](https://pypi.org/project/stoppy/) via:

```shell
pip install stoppy
```

## Usage

Basic usage is as follows:

```python
from time import sleep
from stoppy import Stopwatch

with Stopwatch(start=True) as stopwatch:
    sleep(0.1)
    stopwatch.stop()
    print(stopwatch.time())
    stopwatch.reset()
```

It can also be used as a direct replacement for `perf_counter` with absolute timing starting from zero:

```python
from stoppy import Stopwatch

with Stopwatch() as stopwatch:
    # Calling `stopwatch.time(True)` is equivalent to calling `perf_counter`, but starts from exactly zero
    print(stopwatch.time(True))
```

For all usage examples see [examples/](https://github.com/morefigs/stoppy/tree/main/examples).
