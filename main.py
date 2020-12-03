import subprocess
import tkinter
import tkinter.messagebox
from tkinter import *

name = "Game-Launcher"
color1 = "#0cf7d2"
color2 = "#5a92df"

root = tkinter.Tk()
root.title(name)
root.geometry("150x150")
root.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file='icon\g.png'))
root.configure(bg=color1)

def start_grb():
    subprocess.run(r"F:\Games\GhostReconBreakpoint\GRB.exe")
    messagebox.showinfo(name,"Successfully launched GRB!")

tkinter.Label(root, text="Choose ur Game:", bg=color1).pack(padx=20, pady=20)
photo = tkinter.PhotoImage(file="icon\grb.png") 
tkinter.Button(root, text="GhostReconBreakpoint", image=photo, command=start_grb, bg=color2).pack()

    
root.mainloop()
