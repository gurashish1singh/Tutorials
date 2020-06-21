'''
MultiThreading - Corey Schafer
Older way
'''

import threading
import time

start = time.time()

# Random function
def do_something(seconds):

    print(f'Sleeping for {seconds} second(s)..')
    time.sleep(seconds)
    print('Done sleeping for...')

# # Creating threads
# t1 = threading.Thread(target=do_something)
# t2 = threading.Thread(target=do_something)

# # Starting the threads
# t1.start()
# t2.start()

# # Joining the threads to ensure that they complete before moving on to the rest of the code
# t1.join()
# t2.join()

# List of threads
threads = []

# Creating a loop to create threads
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    t.start()
    threads.append(t)

# Joining the threads
for thread in threads:
    thread.join()

finish = time.time()

print(f'Finished in {round(finish - start, 2)} second(s)')