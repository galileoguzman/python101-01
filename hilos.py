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
        print('Hello')

def print_hi_three_times():
    for i in range(3):
        print('Hi')

# ------------------------------------
# Application logic
# ------------------------------------
thread1 = threading.Thread(target=print_hello_three_times)
thread2 = threading.Thread(target=print_hi_three_times)

thread1.start()
thread2.start()
