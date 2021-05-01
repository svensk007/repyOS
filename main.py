from tkinter import *

version = 0.12

REPYOS = Tk()
REPYOS.title(f"repyOS - {version}")

main = Frame(bg="#bdbdbd")
startBar = Frame(bg="#8f8f8f")

def IDE():
  import ide
def NOTEPAD():
  import notepad
def start():
  tStart = Toplevel()
  button = Button(tStart,text="Quit",command=exit)
  button.pack(ipadx=20)

start = Button(startBar,text="Start",command=start)
repyIDE = Button(startBar,text="repyIDE",command=IDE)
notepadB = Button(startBar,text="Notepad",command=NOTEPAD)


main.pack(ipadx=291,ipady=150,side="top")
startBar.pack(ipadx=175,ipady=0.5,side="bottom")
start.pack(side="left",padx=0.5)
notepadB.pack(side="left",padx=0.5)
repyIDE.pack(side="left",padx=0.5)
REPYOS.mainloop()
