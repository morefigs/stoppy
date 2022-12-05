# stoppy ⏱

A precise stopwatch built on top of `perf_counter`.

The stopwatch can optionally be started automatically by calling `time` instead of `start`, which can streamline usage when polling the time repeatedly.

## Installation

Install from [PyPI](https://pypi.org/project/stopwatch/) via:

```shell
pip install stoppy
```

## Usage

Basic usage is as follows:

```python
from time import sleep
from stoppy import Stopwatch

stopwatch = Stopwatch(start=True)
sleep(1)
stopwatch.stop()
print(stopwatch.time())
stopwatch.reset()
```

For more usage examples see [examples/](https://github.com/morefigs/stoppy/tree/main/examples).
