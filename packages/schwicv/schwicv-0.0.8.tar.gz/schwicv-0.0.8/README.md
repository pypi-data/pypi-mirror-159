# SchwiCV

## Installation

You can install the SchwiCV Tools from [PyPI](https://pypi.org/project/schwicv/):

    pip install schwicv

The package is supported on Python 3.6 and above.

# How to use
## Timer Lib
    from schwicv import Timer
    
    tmr = Timer(0.1)        # Makes Instance of Timer class with 0.1 seconds init time
    tmr.remaining_time      # Output of remaining time in seconds
    tmr.remaining_time_ms   # Output of remaining time in milliseconds
    tmr.execution_time      # Output of execution time since last start in seconds
    tmr.execution_time_ms   # Output of execution time since last start in milliseconds
    tmr.time_stamp          # Output of actual time stamp as datetime
    tmr.time_stamp_str      # Output of actual time stamp yearmonthday-hhmmss-µs example: 20210708-075514-612456
    tmr.remaining_percent   # Output of remaining time in percent
    tmr.time_over           # True if code needed more or equal 0.1 seconds

    tmr.start(1)            # Restart timer with 1 second init time, if re-use instance 
