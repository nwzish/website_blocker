import time
from datetime import datetime as dt
from variables import *

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,strat_time) < dt.now() <  dt(dt.now().year,dt.now().month,dt.now().day,end_time):
        print("Blocking hour")
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                     file.write(redirect + " " + website + "\n")
    else:
        print("Fun hour")
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
    time.sleep(5)
