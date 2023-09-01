from tkinter import *

root = Tk()
root.resizable(width = False, height = False)
root.geometry('330x456')
root.title('My Calculator')
root['bg'] = '#ccc'

frame_a = Frame()
frame_b = Frame()
frame_a.pack()
frame_b.pack()

string = ''
dot_flag = False
elems = ['+', '-', '*', '/']
btn_list = [
"7", "8", "9", "+", 
"4", "5", "6", "-",
"1", "2", "3", "*",
"0", ".", "/", "CE",
"=", "C"]


class CalculatorScreen():
  def __init__(self):
    self.textArea = Entry(master = frame_a)
    self.textArea.configure(bg = '#fff',
                            fg = '#000',
                            disabledbackground = "#fff",
                            disabledforeground = "#000",
                            font = 'Arial 28',
                            state = DISABLED,
                            width = 32,
                            justify = RIGHT)
    self.textArea.pack()
        
  def write(self, text):
    self.textArea.configure(state = NORMAL)
    if len(text) >= 3:
      if text[0] == '0' and text[1] != '.':
        text = text[1:]
        self.textArea.insert(END, text)
    self.textArea.insert(END, text)
    self.textArea.configure(state = DISABLED)

  def clear(self):
    self.textArea.configure(state = NORMAL)
    self.textArea.delete(0, END)
    self.textArea.configure(state = DISABLED)


screen = CalculatorScreen()
screen.write('0')

row = 1
column = 0
for index in btn_list:
  cmd = lambda x = index: output(x)
  button = Button(master = frame_b, 
                  text = index,
                  command = cmd,
                  width = 5,
                  height = 3,
                  font = 'Arial 14',
                  bg = '#786b6b',
                  activebackground="#918c8c",
                  activeforeground="#000")
  button.grid(row = row, column = column, pady = 2, padx = 2)
  column += 1
  if column > 3:
    column = 0
    row += 1
  if index == '=':
    button.configure(width = 13, bg = '#c58424', activebackground="#cc9543", activeforeground="#000")
    button.grid(row=5, column=0, columnspan=2)
              
  if index == 'C':
    button.configure(width = 13, bg = '#c58424', activebackground="#cc9543", activeforeground="#000")
    button.grid(row=5, column=2, columnspan=2)


def output(number):
  global string
  global dot_flag
  screen.clear()

  # Нажатие .
  if (number == '.'):
    if dot_flag == False:
      dot_flag = True
      string += number
      screen.write(string)
    else:
      screen.write(string)
  else:
    string += number
    screen.write(string)

  # Нажатие +-*/
  if number in elems:
    dot_flag = False

  # Нажатие =
  if number == '=':
    string = str(eval(string[:-1]))
    screen.clear()
    screen.write(string)
    dot_flag = False
    for element in string:
      if element == '.':
        dot_flag = True

  # Нажатие С
  if number == 'C':
    dot_flag = False
    string = ''
    screen.clear()
    screen.write('0')

  # Нажатие СЕ
  if number == 'CE':
    screen.clear()
    if len(string) > 3:
      print(string[-3])
      if string[-3] == '.':
        dot_flag = False
      string = string[:-3]
      screen.write(string)
    else:
      string = ''
      dot_flag = False
      screen.write('0')
    
root.mainloop()
