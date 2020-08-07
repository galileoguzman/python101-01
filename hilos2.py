# -------------------------------------
# Description: Working with multi-threading in python
# -------------------------------------

# ------------------------------------
# Importing libraries / importing third party libraries
# ------------------------------------
import time
import threading

# ------------------------------------
# Funtions definition
# ------------------------------------
def print_hello_three_times():
    for i in range(3):
        time.sleep(0.4)
        localtime = time.localtime()
        localtime_text = time.strftime('%I:%M:%S %p', localtime)
        print(f'Hello\t\t\t{localtime_text}')

def print_hi_three_times():
    for i in range(3):
        time.sleep(0.8)
        localtime = time.localtime()
        localtime_text = time.strftime('%I:%M:%S %p', localtime)
        print(f'Hi\t\t\t{localtime_text}')

# ------------------------------------
# Application logic
# ------------------------------------
thread1 = threading.Thread(target=print_hello_three_times)
thread2 = threading.Thread(target=print_hi_three_times)

thread1.start()
thread2.start()
