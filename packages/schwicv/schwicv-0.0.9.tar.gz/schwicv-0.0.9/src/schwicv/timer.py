from datetime import datetime
import time


class Timer:

    def __init__(self, target_time=0.0):
        """
        Initializes a Timer with optional Target time
        :param target_time: in seconds
        """
        self.__start_time = time.perf_counter()
        self.__set_time = target_time

    def start(self, target_time: float):
        """
        Restarts the Timer with specific Target time
        :param target_time: in seconds
        :return:
        """
        self.__start_time = time.perf_counter()
        self.__set_time = target_time

    def restart(self):
        """
        Restarts the Timer with previous Target time
        :return:
        """
        self.__start_time = time.perf_counter()

    # Property time over - Start time defined with start_ms
    def __get_time_over(self) -> bool:
        elapsed_time = time.perf_counter() - self.__start_time
        return elapsed_time >= self.__set_time

    time_over = property(__get_time_over, doc="Returns true if time is over")

    # Property Get Time Stamp of Start Time
    def __get_time_stamp(self) -> datetime:
        return datetime.now()

    time_stamp = property(__get_time_stamp, doc="Returns actual time stamp")

    # Property Get Time Stamp of Start Time as String
    def __get_time_stamp_str(self) -> str:
        time = datetime.now()
        output = time.strftime("%Y%m%d-%H%M%S-%f")
        return output

    time_stamp_str = property(__get_time_stamp_str, doc="Returns Actual time stamp, example: 20210708-075514-612456 "
                                                        "yearmonthday-hhmmss-µs")

    # Property Execution Time in seconds as float
    def __get_execution_time(self) -> float:
        return time.perf_counter() - self.__start_time

    execution_time = property(__get_execution_time, doc="Returns execution time in seconds since last start")

    # Property Execution Time ms as float
    def __get_execution_time_ms(self) -> float:
        return self.__get_execution_time() * 1000

    execution_time_ms = property(__get_execution_time_ms, doc="Returns execution time in milliseconds since last start")

    def __get_remaining_time(self) -> float:
        execution_time = self.__get_execution_time()
        if self.__set_time > execution_time:
            remaining_time = self.__set_time - execution_time
        else:
            remaining_time = 0
        return remaining_time

    remaining_time = property(__get_remaining_time, doc="Returns remaining time in seconds since last start")

    def __get_remaining_time_ms(self) -> float:
        execution_time_ms = self.__get_execution_time_ms()
        if self.__set_time*1000 > execution_time_ms:
            remaining_time_ms = self.__set_time*1000 - execution_time_ms
        else:
            remaining_time_ms = 0
        return remaining_time_ms

    remaining_time_ms = property(__get_remaining_time_ms, doc="Returns remaining time in milliseconds since last start")

    def __get_remaining_percent(self) -> float:
        remaining_time = self.__get_remaining_time()
        if remaining_time > 0:
            remaining_percent = remaining_time / self.__set_time * 100
        else:
            remaining_percent = 0
        return remaining_percent

    remaining_percent = property(__get_remaining_percent, doc="Returns remaining time in percent since last start")


if __name__ == "__main__":
    tmr = Timer(5)
    time.sleep(4)

    print("yo")
    print(time.perf_counter())
    print(time.perf_counter())
    print(time.perf_counter_ns())
    time.sleep(0.1)
    print(time.perf_counter_ns())