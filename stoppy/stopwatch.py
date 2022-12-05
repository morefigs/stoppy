from typing import Optional
from time import perf_counter


class Stopwatch:
    """
    A precise stopwatch built on top of `perf_counter`. The stopwatch can optionally be started automatically by calling
    `time` instead of `start`, which can streamline usage when polling the time repeatedly.
    """
    _time_elapsed: float
    _perf_counter_zero: Optional[float]

    def __init__(self, start: bool = False):
        """
        :param start: Start the stopwatch upon instantiation.
        """
        self.reset(start)

    def __enter__(self) -> Stopwatch:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        pass

    @property
    def running(self) -> bool:
        return self._perf_counter_zero is not None

    def start(self) -> None:
        if not self.running:
            self._perf_counter_zero = perf_counter()

    def stop(self) -> None:
        if self.running:
            self._time_elapsed += perf_counter() - self._perf_counter_zero
            self._perf_counter_zero = None

    def reset(self, start: bool = False) -> None:
        """
        Reset the stopwatch.
        :param start: Start the stopwatch upon reset.
        """
        self._time_elapsed = 0.0
        self._perf_counter_zero = None

        if start:
            self.start()

    def time(self, start: bool = False) -> float:
        """
        Get the stopwatch time, in seconds.
        :param start: Start the stopwatch if it's not running. If the stopwatch is not running and start is True, the
        time returned will be the time immediately before it starts, e.g. it will return exactly 0 for a new object.
        """
        if self.running:
            return self._time_elapsed + perf_counter() - self._perf_counter_zero

        if start:
            self.start()

        return self._time_elapsed
