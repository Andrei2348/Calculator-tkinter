from tkinter import *
from tkinter import ttk

root = Tk()
# root.resizable(width = False, height = False)
# root.geometry('300x200')
root.title('window name')
root[ 'bg']= '#ccc'

# text_1 = Label(text = '1', fg = 'black', bg = 'yellow', width = 30, height = 15)
# text_2 = Label(text = '2', fg = 'black', bg = 'red', width = 30, height = 15)
# text_3 = Label(text = '3', fg = 'black', bg = 'green', width = 30, height = 15)
# text_4 = Label(text = '4', fg = 'black', bg = 'blue', width = 30, height = 15)

# text_1.pack(side = TOP)
# text_2.pack(side = BOTTOM)
# text_3.pack(side = RIGHT)
# text_4.pack(side = LEFT)

# GRID
# i = 1
# for ROW in range(3):
#   for COLUMN in range(3):
#     print(i)
#     btn = Button(text = str(i), width = 15, font = 'Arial 14')
#     btn.grid(row = ROW, column = COLUMN, pady = 5, padx = 5)
#     i += 1
    
    
    # button = ttk.Button(root, text = index, command = cmd, width = 10)
btn = Button(text = '=', width = 34, height = 12, font = 'Arial 14')
btn.grid(row = 4, column = 0, pady = 5, padx = 5, columnspan = 2, rowspan = 2)   

# text = Label(text = 'text', width = 15)
# text.place(x = 10, y = 10)

def output(index):
  print(index)


for c in range(3): root.columnconfigure(index = c, weight=1)
for r in range(3): root.rowconfigure(index = r, weight=1)

index = 1
for r in range(3, 0, -1):
  for c in range(3):
    btn = ttk.Button(text=f"{index}")
    btn.grid(row=r, column=c, pady = 5, padx = 5)
    cmd = lambda x = index: output(x)
    btn.bind("<ButtonPress-1>", cmd)
    index += 1

root.mainloop()