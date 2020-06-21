'''
Multiprocessing - Corey Schaffer
Newer way to create processes
'''

import concurrent.futures
import time


# Making the process sleep for 1 second
def do_something(seconds):

    print(f'Sleep {seconds} second(s)..')
    time.sleep(seconds)

    return f'Done Sleeping in {seconds}..'


if __name__ == "__main__":

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Schedues the function to  be executed one at a time and returns a future object
        # A future object encapsulates execution of our function and allows us to check on it after it's been scheduled
        # f1 = executor.submit(do_something, 1.2)
        # f2 = executor.submit(do_something, 1.1)

        # # The result method allows us to check the return value of our function
        # print(f1.result())
        # print(f2.result())

        secs = [5, 4, 3, 2, 1]
        # Submit executes the function one at a time
        # Returns the results as they are completed
        # result = [executor.submit(do_something, sec) for sec in secs]

        # for f in concurrent.futures.as_completed(result):
        #     print(f.result())

        # Map executes the function over a list of values
        # Returns the results in the order they were started
        results = executor.map(do_something, secs)

        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
