# Time Tracker
# The helper program concept
# for logging time on projects
# A.Josephs 02/02/2021

import argparse

from datetime import datetime

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

def write_to_file(message):
    """save/append to file with timestamp"""
    log_file = open("MyLog.txt","a")
    time = get_time()
    new_line = "{} {} \n".format(time, message)
    log_file.write(new_line)
    log_file.close()

def get_time():
    """Obviously get the current time but also make it pretty"""
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string

def calculate_working_time():
    """calculate time between previous entry and new entry"""
    print("1 hr : this is how long you have been working between logs")
    # get previous line and parser
    # get current time (GLOBAL)
    # insert line with difference and string message

def main():
    args = parse()
    input_message = args.Message
    write_to_file(input_message)


if __name__ == "__main__":
    main()
