"""
Dealing with dates and times

3 modules: time, datetime, calendar

"""
import time
from time import perf_counter as my_timer  # actual elapsed time
# from time import monotonic as my_timer
# from time import process_time as my_timer  # cpu time
import random

print(time.gmtime(0))
print(time.localtime())  # current day in a named tuple
print(time.time())  # number of seconds since start of the epoch

time_here = time.localtime()
print(time_here)
print("Year: ", time_here[0], time_here.tm_year)  # current year
print("Month: ", time_here[1], time_here.tm_mon)  # current month
print("Day: ", time_here[2], time_here.tm_mday)  # current day

print("*" * 80)

input("Press enter to start")

wait_time = random.randint(1, 6)
time.sleep(wait_time)
start_time = my_timer()
input("Press enter to stop")
end_time = my_timer()

print("Started at " + time.strftime("%X", time.localtime(start_time)))
print("Ended at " + time.strftime("%X", time.localtime(end_time)))
print("Your reaction time was {} seconds.".format(end_time - start_time))
