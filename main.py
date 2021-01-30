from time import sleep
from subprocess import *
from Task import Task
import multiprocessing
import numpy as np
from pathlib import Path


def convert_new_data_to_str_list(new_data):
    converted_data = new_data
    for i in range(len(new_data)):
        converted_data[i] = str(new_data[i])
    return converted_data


def Popen_command_list(path, data):
    return [path] + convert_new_data_to_str_list(data)


def assign_task(data):
    cwd = "/home/xidad/PycharmProjects/Scheduler/results/" + folder_name(data)
    if Path(cwd).is_dir():
        print(folder_name(data), "already exists")
    else:
        print(folder_name(data), "has started")
        Popen(["mkdir", folder_name(data)], cwd="/home/xidad/PycharmProjects/Scheduler/results")
        sleep(1)
        p = Popen(Popen_command_list(script_path, data), cwd=cwd)
        p.wait()


def folder_name(data):
    name = ""
    for x in data:
        name += str(x) + " "
    return name


script_path = "/home/xidad/CLionProjects/DendriteV3/cmake-build-release/DendriteV3"

# Generate list of parameters as linear 2d array
n_list = list(map(lambda x: np.round(x, decimals=3), np.linspace(0, 1, 15)))
U_list = list(map(lambda x: np.round(x, decimals=3), np.linspace(1.5, 6, 15)))
par_list = [None] * (len(n_list) * len(U_list))
for i in range(len(n_list)):
    for j in range(len(U_list)):
        par_list[i * len(U_list) + j] = [n_list[i], U_list[j]]

if Path("/home/xidad/PycharmProjects/Scheduler/results/").is_dir():
    pass
else:
    Popen(["mkdir", "results"])

num_threads = 15
pool = multiprocessing.Pool(processes=num_threads)

pool.map(assign_task, par_list)
sleep(5)
