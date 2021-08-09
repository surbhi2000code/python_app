# Python Programming Course:GUI Applications sections
#                                        - Rahul Mula
# Source code for creating the age calculator

from tkinter import *
from datetime import datetime

# Main Window & Configuration
App = Tk()
App.title("Age Calculator")
App['background'] = 'white'
App.geometry('600x600')

# 'Enter Your DOB' Label
lbl = Label(App, text='Enter Your DOB', background='black', foreground='white')
lbl.grid(row=0, column=0, columnspan=2, padx=25, pady=25)

# Date Label & Entry widget
dateL = Label(App, text='Date:', background='white', foreground='black')
dateE = Entry(App, background='grey', relief='sunken', foreground='black', width=4)

# Month Label & Entry widget
monL = Label(App, text='Month:', background='white', foreground='black')
monE = Entry(App, background='grey', foreground='black', width=4)

# Year Label & Entry widget
yrL = Label(App, text='Year:', background='white', foreground='black')
yrE = Entry(App, background='grey', foreground='black', width=8)

# Placing the widgets using grid
dateL.grid(row=1, column=0, padx=5, pady=15)
dateE.grid(row=1, column=1, padx=0, pady=15)
monL.grid(row=1, column=2,padx=5, pady=15)
monE.grid(row=1, column=3, padx=0, pady=15)
yrL.grid(row=1, column=4, padx=10, pady=15)
yrE.grid(row=1, column=5, padx=0, pady=15)


# Finding Total days and creating it's Label
def find_days():
    year = int(yrE.get())
    month = int(monE.get())
    day = int(dateE.get())
    dob = datetime(year=year, month=month, day=day)

    time_now = datetime.now()
    time_dif = time_now - dob
    msg = Label(App, text='You lived ' + str(time_dif.days) + ' days!', background='yellow',
                foreground='black')
    msg.grid(row=3, column=0, columnspan=3, pady=15)


# Finding Total seconds and creating it's Label
def find_sec():
    year = int(yrE.get())
    month = int(monE.get())
    day = int(dateE.get())
    dob = datetime(year=year, month=month, day=day)

    time_now = datetime.now()
    time_dif = time_now - dob
    msg = Label(App, text='You lived ' + str(time_dif.total_seconds()) + ' seconds!', background='yellow',
                foreground='black')
    msg.grid(row=4, column=0, columnspan=6, pady=15)


# Buttons for finding total days & seconds
daysB = Button(App, text='Total days', command=find_days, background='white', foreground='black')
scndB = Button(App, text='Total seconds', command=find_sec, background='white', foreground='black')
# Placing the buttons
daysB.grid(row=2, column=0, padx=5, pady=5, columnspan=3)
scndB.grid(row=2, column=3, padx=5, pady=5, columnspan=3)

App.mainloop()

