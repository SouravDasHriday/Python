import os

# defining a function:

def check_date(command):
    print(os.system(command))

def check_uptime(command):
    print(os.system(command))

def check_disk(command): 
    print(os.system(command))

def check_ram(command):
    print(os.system(command))

# calling a function:

check_date("date")
check_uptime("uptime")
check_disk("df -hT")
check_ram("free -h")




