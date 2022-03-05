from tkinter import *
import datetime
import time
import winsound


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        if now == set_alarm_timer:
            print("Time to Wake up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break

# Gets information and sends them to actual function.
def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

#Starts Tkinter, sets title and size
clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("200x100")

# Text positions
Label(clock, text="Hour", font=60).place(x=0, y=20)
Label(clock, text="Min", font=60).place(x=75, y=20)
Label(clock, text="Sec", font=60).place(x=150, y=20)

# When to wake you up text.
Label(clock, text="When to wake you up", fg="blue", font=(
    "Helevetica", 7, "bold")).place(x=50, y=0)

# The Variables we require to set the alarm(initialization):
# Tkinter requiers different kind of variables, not regular python ones.
hour = StringVar()
min = StringVar()
sec = StringVar()

# Time required to set the alarm clock:
# We also assign these values to previous variables.
hourTime = Entry(clock, textvariable=hour, bg="pink",
                 width=10).place(x=0, y=40)
minTime = Entry(clock, textvariable=min, bg="pink",
                width=10).place(x=75, y=40)
secTime = Entry(clock, textvariable=sec, bg="pink",
                width=10).place(x=150, y=40)

# To take the time input by user:
submit = Button(clock, text="Set Alarm", fg="red", width=10,
                command=actual_time).place(x=100/2+10, y=75)
#Starts the window
clock.mainloop()

