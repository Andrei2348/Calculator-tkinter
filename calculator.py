from tkinter import *


root = Tk()
root.resizable(width = False, height = False)
root.geometry('330x510')
root.title('My Calculator')
root[ 'bg'] = '#ccc'

frame_a = Frame()
frame_b = Frame()
frame_a.pack()
frame_b.pack()


btn_list = [
"7", "8", "9", "+", 
"4", "5", "6", "-",
"1", "2", "3", "*",
"0", ".", "+/-", "/",
"=", "C"]


class CalculatorScreen():
  def __init__(self):
    self.textArea = Entry(master = frame_a)
    self.textArea.configure(bg = '#fff',
                            fg = '#000',
                            disabledbackground = "#fff",
                            disabledforeground = "#000",
                            font = 'Consolas 22',
                            state = DISABLED,
                            width = 32,
                            justify = RIGHT)
    self.textArea.pack()
        
  def write(self, text):
    self.textArea.configure(state = NORMAL)
    self.textArea.insert(END, text)
    self.textArea.configure(state = DISABLED)

  def clear(self):
    self.textArea.configure(state = NORMAL)
    self.textArea.delete(0.0, END)
    self.textArea.configure(state = DISABLED)


screen_1 = CalculatorScreen()
screen_2 = CalculatorScreen()


row = 1
column = 0
for index in btn_list:
  cmd = lambda x = index: output(x)
  button = Button(master = frame_b, text = index, command = cmd, width = 5, height = 3, font = 'Arial 14', bg = 'yellow')
  button.grid(row = row, column = column, pady = 2, padx = 2)
  column += 1
  if column > 3:
    column = 0
    row += 1
  if index == '=':
    button.configure(width = 13)
    button.grid(row=5, column=0, columnspan=2)
  if index == 'C':
    button.configure(width = 13)
    button.grid(row=5, column=2, columnspan=2)


        
def output(x):
  screen_1.write(x)
  
  
  
root.mainloop()
