from tkinter import *
from tkinter import ttk

root = Tk()
root.resizable(width = False, height = False)
root.geometry('330x410')
root.title('My Calculator')
root[ 'bg'] = '#ccc'


btn_list = [
"7", "8", "9", "+", 
"4", "5", "6", "-",
"1", "2", "3", "*",
"0", ".", "+/-", "/",
"=", "C"]

row = 1
column = 0
for index in btn_list:
  rel = ""
  cmd = lambda x = index: output(x)
  button = Button(text = index, command = cmd, width = 5, height = 3, font = 'Arial 14')
  button.grid(row = row, column = column, pady = 2, padx = 2)
  column += 1
  if column > 3:
    column = 0
    row += 1
        
        
def output(x):
  print(x)
  
  
  
root.mainloop()