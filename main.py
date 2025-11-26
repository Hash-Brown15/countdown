from tkinter import*
import time

my_window = Tk()
my_window.geometry("400x400")
my_window.title = "Time Counter"

hour = Entry(my_window)
hour.pack()

minutes = Entry(my_window)
minutes.pack()  

seconds = Entry(my_window)
seconds.pack()

set_time_countdown = Button(my_window, text="Set Time Countdown")
set_time_countdown.pack()