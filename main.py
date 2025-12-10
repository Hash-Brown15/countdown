from tkinter import*
import time
from tkinter import messagebox

my_window = Tk()
my_window.geometry("400x400")
my_window.title = "Time Counter"

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")

hourEntry = Entry(my_window, width=3, font=("Arial", 18), textvariable=hour)
hourEntry.place(x=80, y=40)

minuteEntry = Entry(my_window, width=3, font=("Arial", 18), textvariable=minute)
minuteEntry.place(x=130, y=40)

secondEntry = Entry(my_window, width=3, font=("Arial", 18), textvariable=second)
secondEntry.place(x=180, y=40)

def submit():
    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

    except:
        print("Please input the right value")
    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 00
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(mins))
        second.set("{00:2d}".format(secs))

        my_window.update()
        time.sleep(1)

        if (temp == 00):
            messagebox.showinfo("Time Countdown", "Time's up ")
        temp -= 1

set_time_countdown = Button(my_window, text="Set Time Countdown",command=submit)
set_time_countdown.place(x=80, y=80)

my_window.mainloop()