'''
MultiThreading - Corey Schafer
Newer way
'''

import concurrent.futures
import time

start = time.time()

# Random function
def do_something(seconds):

    print(f'Sleeping for {seconds} second(s)..')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'

# Creating, starting and joining threads in a more automated way
with concurrent.futures.ThreadPoolExecutor() as executer:
    # f1 = executer.submit(do_something, 1.5)
    # f2 = executer.submit(do_something, 1.5)
    # print(f1.result())
    # print(f2.result())

    secs = [5, 4, 3, 2, 1]

    # Multiple threads
    # results = [executer.submit(do_something, sec) for sec in secs]

    # Returns the threads as they complete
    # for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    # Running the submit method on a list at the same time
    # Preserves the order of the threads as they were started
    results = executer.map(do_something, secs)

    for result in results:
        print(result)

finish = time.time()

print(f'Finished in {round(finish - start, 2)} second(s)')