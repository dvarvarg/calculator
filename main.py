from tkinter import *
from tkinter import ttk
import сalculator_logic as c


oper=''
first=0
second=0
result=0


def calc():
    second = float(entry.get())
    if oper=='+':
        result=c.add(first,second)
    elif oper=='-':
        result=c.subtruct(first,second)
    elif oper=='*':
        result=c.multiply(first,second)
    elif oper=='/':
        result=c.divide(first,second)


# функция ввода числа
def enter_number(number):
    entry.insert(END, number)


# функция для очистки поля ввода
def clear_entry():
    entry.delete(0,END)


# функция, чтоб при нажатии +-*/ автоматически в переменную oper падало нужное значение
def set_operation(operation):
    global first
    global oper
    first=float(entry.get())
    oper=operation
    entry.delete(0,END)


window=Tk()
window.title('Калькулятор')
window.geometry()

entry=ttk.Entry()
entry.pack()

window.mainloop()
