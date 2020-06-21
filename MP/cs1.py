'''
Multiprocessing - Corey Schaffer
Older/Manual way to create processes
'''

import multiprocessing
import time


# Making the process sleep for 1 second
def do_something(seconds):
    print(f'Sleep {seconds} second(s)..')
    time.sleep(seconds)
    print('Done Sleeping..')


# Needed for windows to avoid unintended  side effects such as starting new process
# If it's name is main, run this code. (In this case, it could result in a stray process)
# Else (if it's name is anything else), do something else, usually nothing.
if __name__ == "__main__":

    start = time.perf_counter()

    # # Creating processes
    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    processes = []
    # Starting multiple processes using a loop and a throw away variable
    for _ in range(10):
        p = multiprocessing.Process(target=do_something, args=[1.5])
        p.start()
        # By using p.join() within this loop it joins the processes before creating and starting new processes,
        # it  would be same as running in async. Instead we append the processes to a list and join later
        processes.append(p)

    for process in processes:
        process.join()

    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} second(s)')
