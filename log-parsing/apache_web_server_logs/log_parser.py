import re

def parse_log(file_name=""):
    # log_file = "/path/to/access.log"
    log_file = file_name
    return_list = list()

    with open(log_file, "r") as f:
        for line in f:
            # split the log line into fields using regular expression
            fields = re.split(' - - \[|\] "|"', line)
            
            # get the timestamp and IP address
            timestamp = fields[1]
            ip_address = fields[0]
            
            # do something with the timestamp and IP address
            print(f"Timestamp: {timestamp}, IP Address: {ip_address}")
            return_list.append({'ip':ip_address, 'timestamp': timestamp})
    return return_list

