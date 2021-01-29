import time
import subprocess
from Worker import Worker
import asyncio


def assign_task(worker):
    if par_list:
        worker.start_subprocess_with_new_data(par_list[0])
        par_list.pop(0)


# Generate list of parameters as linear 2d array
n_list = range(0, 4, 1)
U_list = range(0, 4, 1)
par_list = [None] * (len(n_list) * len(U_list))
for i in range(len(n_list)):
    for j in range(len(U_list)):
        par_list[i * len(n_list) + j] = [n_list[i], U_list[j]]

# for item in par_list:
#     print(item)

num_threads = 5
# workers = [Worker] * num_threads
workers = [Worker()] * num_threads
for worker in workers:
    assign_task(worker)

# While list of parameters is not empty and each worker hasn't ended yet
any_worker_still_busy = False
while par_list or any_worker_still_busy:
    any_worker_still_busy = False

    for worker in workers:
        if worker.is_busy():
            any_worker_still_busy = True
            if worker.timeout():
                print("Worker timeout occurred. Data: ", worker.data_to_process)
                worker.kill_subprocess()
                assign_task(worker)

        else:
            assign_task(worker)

    time.sleep(1)
