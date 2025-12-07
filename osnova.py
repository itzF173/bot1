#int,float,string,enum...


#Сравнения == != < > <= >=
#Действия + - * / // **


from tkinter import *


tk = Tk()
canvas = Canvas(tk,width=300,height=300)
tk.update()
canvas.pack()
b1 = Button(tk, text="Hello")
def Hello(event):
    print("Hello")

b1.pack()
b1.bind_all("<Button-1>",Hello)


obj = [
    {"x":0,"y":5,"r": 1},
    {"x":0,"y":10, "r": 2},
    {"x":5,"y":0,"r": 1},
]

age = input("Возраст: ")
i = 0
while i < len(obj):
    i += 1
    print(i)
    x = 0

import numpy
numpy.array(obj)

tk.mainloop()

