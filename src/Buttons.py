# Install the State Tool
# Windows: 
# IEX(New-Object Net.WebClient).downloadString('https://platform.activestate.com/dl/cli/install.ps1')
# state activate --default ActiveState/ActivePython-3.8

# Linux, Mac : 
# sh <(curl -q https://platform.activestate.com/dl/cli/install.sh)
# state activate --default ActiveState/ActivePython-3.8 


from tkinter import *

root = Tk()
root.title("PyCalculator")

a = Entry(root, width=35, borderwidth=5)
a.grid(row=0, column=0, cloumnspan=3, ipadx=10, pady=10)

def button():
    return

button1 = Button(root, text="1", padx=40, pady=40, command=button)
button2 = Button(root, text="2", padx=40, pady=40, command=button)

button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
