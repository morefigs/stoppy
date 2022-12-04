from time import sleep
from math import isclose

import pytest

from stopwatch.stopwatch import Stopwatch


STEP = 0.5
ABS_TOL = 0.1


@pytest.fixture(scope='function')
def stopwatch():
    return Stopwatch()


class TestStopwatch:
    def test_init(self):
        stopwatch = Stopwatch()
        assert stopwatch.time() == 0

        stopwatch = Stopwatch(True)
        assert stopwatch.time() > 0

    def test_running(self, stopwatch: Stopwatch):
        assert not stopwatch.running
        stopwatch.start()
        assert stopwatch.running

    def test_start(self, stopwatch: Stopwatch):
        stopwatch.start()
        assert stopwatch.running

    def test_stop(self, stopwatch: Stopwatch):
        stopwatch.stop()
        assert not stopwatch.running

    def test_reset(self, stopwatch: Stopwatch):
        stopwatch.reset(True)
        assert stopwatch.time() > 0

        stopwatch.reset()
        assert stopwatch.time() == 0

    def test_time(self, stopwatch: Stopwatch):
        # Test autostart
        assert stopwatch.time() == 0
        assert stopwatch.time() == 0
        assert stopwatch.time(True) == 0
        assert stopwatch.time() > 0

    def test_timing(self, stopwatch: Stopwatch):
        assert stopwatch.time(True) == 0
        sleep(STEP)
        assert isclose(stopwatch.time(), STEP, abs_tol=ABS_TOL)
        sleep(STEP)
        assert isclose(stopwatch.time(), STEP * 2, abs_tol=ABS_TOL)

        stopwatch.stop()
        assert isclose(stopwatch.time(), STEP * 2, abs_tol=ABS_TOL)
        assert stopwatch.time() == stopwatch.time(True)
        sleep(STEP)
        assert isclose(stopwatch.time(), STEP * 3, abs_tol=ABS_TOL)
