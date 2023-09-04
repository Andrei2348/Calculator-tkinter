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
resultString = ''
dot_flag = False

# Создаем список символов действия (Необходимы для отслеживания нажатия)
elems = ['+', '-', '*', '/']

# Создаем список кнопок клавиатуры калькулятора
btn_list = [
"7", "8", "9", "+", 
"4", "5", "6", "-",
"1", "2", "3", "*",
"0", ".", "CE", "/",
"=", "C"]

# Создаем класс: экран калькулятора
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
    self.write()
    
  # Создаем метод для очистки экрана калькулятора
  def clear(self):
    self.textArea.configure(state = NORMAL)
    self.textArea.delete(0, END)
    self.textArea.configure(state = DISABLED)
        
  # Создаем метод вывода символов на экран калькулятора
  def write(self, text = '0'):
    self.clear()
    self.textArea.configure(state = NORMAL)
    if len(text) >= 2:
      if text[0] == '0' and text[1] != '.':
        text = text[1:]
    self.textArea.insert(END, text)
    self.textArea.configure(state = DISABLED)

# Создаем экран калькулятора
screen = CalculatorScreen()

# Создание кнопок калькулятора
row = 1
column = 0
for index in btn_list:
  # Привязка функций к кнопкам калькулятора
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
  
  # Конфигурация кнопок  '=' и 'С'
  if index == '=':
    button.configure(width = 13, bg = '#c58424', activebackground="#cc9543", activeforeground="#000")
    button.grid(row=5, column=0, columnspan = 2)
              
  if index == 'C':
    button.configure(width = 13, bg = '#c58424', activebackground="#cc9543", activeforeground="#000")
    button.grid(row=5, column=2, columnspan = 2)


def output(number):
  global string
  global dot_flag
  global resultString

  # Обнуление переменной string после знаков действия
  if len(string) > 2:
    if (string[-2] in elems) and  (string[-1] not in elems):
      resultString += (str(float(string[:-2])) + string[-2])
      string = string[-1]
      screen.write(resultString + string)
  
  # Нажатие '.'
  if (number == '.'):
    # Блокировка повторного нажатия '.'
    if dot_flag == False:
      dot_flag = True
      string += number
      screen.write(resultString + string)
    else:
      screen.write(resultString + string)
  else:
    string += number
    screen.write(resultString + string)

  # Нажатие '+-*/'
  if number in elems:
    if (string[-1] in elems) and  (string[-2] in elems):
      string = (str(float(string[:-2])) + number)
      screen.write(resultString + string)
    else:
      string = (str(float(string[:-1])) + number)
      screen.write(resultString + string)
    dot_flag = False
      
  # Нажатие '='
  if number == '=':
    resultString += str(float(string[:-1]))
    string = str(eval(resultString))
    screen.write(string)
    resultString = ''
    dot_flag = checkDot(string)

  # Нажатие 'С'
  if number == 'C':
    resetCalc()

  # Нажатие 'СЕ' Пошаговое очищение поля ввода
  if number == 'CE':
    # Стираем последнюю введенную цифру
    if len(resultString) > 0 and string == 'CE':
      resultString = resultString[:-1]
      string = ''
      screen.write(resultString)
      # Установка разрешения на '.' при очистке resultString
      dot_flag = checkDot(resultString)

    if len(resultString) > 0 and len(string) > 0 and string != 'CE':
      string = string[:-3]
      screen.write(resultString + string)
      # Установка разрешения на '.' при очистке string
      dot_flag = checkDot(string)

    if resultString == '' and len(string) > 0:
      string = string[:-3]
      screen.write(resultString + string)
      # Установка разрешения на '.' при очистке string
      dot_flag = checkDot(string)
   
    # Обнуление калькулятора
    if (resultString == '' and string == ''):
      resetCalc()
  

# Обнуление калькулятора
def resetCalc():
  global string
  global dot_flag
  global resultString
  dot_flag = False
  string = ''
  resultString = ''
  screen.write()

# Проверка наличия '.' в строке
def checkDot(data):
  if '.' in data:
    return True
  else:
    return False


root.mainloop()
