
import config

string = ''
dot_flag = False


def output(number):
  global string
  global dot_flag
  config.screen.clear()

  # Нажатие .
  if (number == '.'):
    if dot_flag == False:
      dot_flag = True
      string += number
      config.screen.write(string)
    else:
      config.screen.write(string)
  else:
    string += number
    config.screen.write(string)

  # Нажатие +-*/
  if number in config.elems:
    dot_flag = False
    if string[-2] in config.elems:
      string = string[:-2] + number
      config.screen.clear()
      config.screen.write(string)
      
  # Нажатие =
  if number == '=':
    string = str(eval(string[:-1]))
    config.screen.clear()
    config.screen.write(string)
    dot_flag = False
    for element in string:
      if element == '.':
        dot_flag = True

  # Нажатие С
  if number == 'C':
    dot_flag = False
    string = ''
    config.screen.clear()
    config.screen.write('0')

  # Нажатие СЕ
  if number == 'CE':
    config.screen.clear()
    if len(string) > 3:
      print(string[-3])
      if string[-3] == '.':
        dot_flag = False
      string = string[:-3]
      config.screen.write(string)
    else:
      string = ''
      dot_flag = False
      config.screen.write('0')
    

