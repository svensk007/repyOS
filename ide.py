from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import os, subprocess

compiler = Tk()
compiler.title("replOS IDE")
compiler.resizable(width=False,height=False)
file_path = ""

#Button Commands

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
  path = askopenfilename(filetypes=[("Python Files","*.py"),("Text File","*.txt")])
  with open(path,"r") as file:
    code = file.read()
    editor.delete("1.0",END)
    editor.insert("1.0",code)
    set_file_path(path)

def run():
  if file_path == "":
    save_prompt = Toplevel()
    text = Label(save_prompt,text="Save your code!")
    text.pack()
    return
  code_output.delete("1.0",END)
  command = f"python {file_path}"
  process = subprocess.Popen(command,stdout=subprocess.PIPE,shell=True)
  output, error = process.communicate()
  code_output.insert("1.0",output)
  code_output.insert("1.0",error)

def new_file():
    save_as()
    editor.delete("1.0",END)
    file_path = ""

def clear():
  editor.delete("1.0",END)
def clear_console():
  code_output.delete("1.0",END)

#Menu bar(file, edit)

menu_bar = Menu(compiler)

file_bar = Menu(menu_bar,tearoff=0)
file_bar.add_command(label="Run",command=run,accelerator="Ctrl+Enter")
file_bar.add_command(label="New",command=new_file,accelerator="Ctrl+N")
file_bar.add_command(label="Open",command=open_file,accelerator="Ctrl+O")
file_bar.add_command(label="Save", command=save_as,accelerator="Ctrl+S")
file_bar.add_command(label="Save As",command=save_as,accelerator="Ctrl+Alt+S")
file_bar.add_command(label="Exit",command=exit,accelerator="Ctrl+Q")

edit_bar = Menu(menu_bar,tearoff=0)
edit_bar.add_command(label="Clear",command=clear)
edit_bar.add_command(label="Clear Console",command=clear_console)

menu_bar.add_cascade(label="File",menu=file_bar)
menu_bar.add_cascade(label="Edit",menu=edit_bar)

compiler.config(menu=menu_bar)

editor = Text(height=20)
editor.pack()

code_output = Text(height=12)
code_output.pack()

compiler.mainloop()