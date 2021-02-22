# Time Tracker
# The helper program concept
# for logging time on projects
# A.Josephs 02/02/2021

import argparse

from datetime import datetime
from os import path

class LogItem:
    def __init__(self, message):
        self.file_name = "mylog.txt"
        self.message = message
        self.current_time = get_time()
        self.previous_datetime = get_last_datetime(self.file_name)
        self.time_on_task = calculate_working_time(self)

def get_last_datetime(filename):
    if path.exists(filename) and path.getsize(filename) != 0:
        with open(filename, "r") as file:
            for line in file:
                pass
        line_p = line.split(" ")
        return line_p[0] + " " + line_p[1]
    else:
        print("New File Created mylog.txt")
        return None, None

def parse():
    """parse arguments, currently only the message"""

    my_parser = argparse.ArgumentParser(description='Log an activity message to file')

    my_parser.add_argument('Message',
                           metavar='message',
                           type=str,
                           help='the message to log on file')

    my_parser.add_argument('-t',
                       '--tag',
                       help='add a tag to the message')

    args = my_parser.parse_args()
    return args

def write_to_file(log_item):
    """save/append to file with timestamp"""
    log_file = open(log_item.file_name, "a")
    time_on_str = "-- Time on task {} --".format(log_item.time_on_task)
    new_log = "{} {} {} \n".format(log_item.current_time, log_item.message, time_on_str)
    log_file.write(new_log)
    log_file.close()

def get_time():
    """Obviously get the current time but also make it pretty"""
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def calculate_working_time(self):
    """calculate time between previous entry and new entry"""
    if self.previous_datetime[0] == None:
        return 0
    else:
        c_t = datetime.strptime(self.current_time, "%d/%m/%Y %H:%M:%S")
        p_t = datetime.strptime(self.previous_datetime, "%d/%m/%Y %H:%M:%S")
        return c_t - p_t

def main():
    args = parse()
    new_loggable = LogItem(args.Message)
    write_to_file(new_loggable)


if __name__ == "__main__":
    main()
