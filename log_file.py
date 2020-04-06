from datetime import datetime


# Log data in log file.
class LogFile:

    def __init__(self):
        self.log_file = open('Log_file.txt', 'a+')

    def write(self, data):
        current_time = datetime.now().strftime("%d/%B/%Y %H:%M:%S")
        self.log_file.write('{} ::  {}\n'.format(current_time, data))

    def close(self):
        self.log_file.close()
