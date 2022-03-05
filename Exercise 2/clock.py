from tkinter import *
import datetime
import time
import winsound

def alarm():
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)

alarm()