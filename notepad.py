from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os, subprocess

file_path = ""
compiler = Tk()
if file_path == "":
  compiler.title("Notepad")
else:
  complier.title(f"Notepad - [{file_path}]")
compiler.resizable(width=False,height=False)

def set_file_path(path):
  global file_path
  file_path = path

def save_as():
  if file_path == "":
    path = asksaveasfilename(filetypes=[("Python Files","*.py"),("Text File","*.txt")])
  else:
    path = file_path
  with open(path,"w") as file:
    code = editor.get("1.0",END)
    file.write(code)
    set_file_path(path)

def open_file():
  path = askopenfilename(filetypes=[("Text File","*.txt"),("All Files","*.*")])
  with open(path,"r") as file:
    code = file.read()
    editor.delete("1.0",END)
    editor.insert("1.0",code)
    set_file_path(path)
    compiler.title(f"Notepad - [{file_path}]")

def new_file():
    save_as()
    editor.delete("1.0",END)
    file_path = ""

def clear():
  editor.delete("1.0",END)

menu_bar = Menu(compiler)

file_bar = Menu(menu_bar,tearoff=0)
file_bar.add_command(label="New",command=new_file,accelerator="Ctrl+N")
file_bar.add_command(label="Open",command=open_file,accelerator="Ctrl+O")
file_bar.add_command(label="Save", command=save_as,accelerator="Ctrl+S")
file_bar.add_command(label="Save As",command=save_as,accelerator="Ctrl+Alt+S")
file_bar.add_command(label="Exit",command=exit,accelerator="Ctrl+Q")

edit_bar = Menu(menu_bar,tearoff=0)
edit_bar.add_command(label="Clear",command=clear)

menu_bar.add_cascade(label="File",menu=file_bar)
menu_bar.add_cascade(label="Edit",menu=edit_bar)

compiler.config(menu=menu_bar)

editor = Text(height=21,width=70)
editor.pack()

compiler.mainloop()