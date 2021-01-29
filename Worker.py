import subprocess
from timer import Timer


class Worker:
    def __init__(self):
        self.script_path = "/home/xidad/CLionProjects/untitled/cmake-build-debug/untitled"
        self.subprocess_var = None
        self.data_to_process = None
        self.time_restriction = 10
        self.timer = Timer()

    def start_subprocess_with_new_data(self, new_data):
        self.timer.update()
        if self.subprocess_var is not None:
            self.subprocess_var.kill()
        self.data_to_process = self.convert_new_data_to_str_list(new_data)
        self.subprocess_var = subprocess.Popen(self.Popen_command_list())

    def Popen_command_list(self):
        return [self.script_path] + self.data_to_process

    def is_busy(self):
        if self.subprocess_var.poll() is None:
            return True
        else:
            return False

    def kill_subprocess(self):
        self.subprocess_var.kill()

    def timeout(self):
        return self.timer.elapsed_time() > self.time_restriction

    def convert_new_data_to_str_list(self, new_data):
        converted_data = new_data
        for i in range(len(new_data)):
            converted_data[i] = str(new_data[i])
        return converted_data
