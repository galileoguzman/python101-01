# -------------------------------------
# Description: Intial program to do a loop while
# -------------------------------------

# ------------------------------------
# Importing libraries / importing third party libraries
# ------------------------------------
import time

# ------------------------------------
# Variables and constants
# ------------------------------------
LIMIT_NUMBER = 10
counter = 0

# ------------------------------------
# Application logic
# ------------------------------------
print('Application is starting up\n\n')

while(counter < LIMIT_NUMBER):
    localtime = time.localtime()
    time_text = time.strftime('%I:%M:%S %p', localtime) # 18:56:32 PM
    print(f'Counter value:\t {counter}\t {time_text}') # Counter value : 1 18:56:32 PM
    counter = counter + 1
    time.sleep(2.0)

# End of my program
print('\nApplication finished')
