from tkinter import *
from tkinter import ttk
import сalculator_logic as c


oper=''
first=0
second=0
result=0


def calc():
    global second
    second = float(entry.get())
    if oper=='+':
        result=c.add(first,second)
    elif oper=='-':
        result=c.subtract(first,second)
    elif oper=='*':
        result=c.multiply(first,second)
    elif oper=='/':
        result=c.divide(first,second)
    entry.delete(0,END)
    entry.insert(0,str(result))


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
    try:
        first=float(entry.get())
    except ValueError:
        first=0
    oper=operation
    entry.delete(0,END)


def validate_entry():
    entry_text=entry.get()
    txt=''.join(b for b in entry_text if b in '0123456789.-') # список разрешенных символов
    if entry_text !=txt:
        entry.delete(0,END)
        entry.insert(0,txt)


window=Tk()
window.title('Калькулятор')
window.geometry()

entry=ttk.Entry(width=20)
entry.grid(row=0,column=0,columnspan=4,sticky='ew')
entry.bind('<KeyRelease>',lambda event: validate_entry()) #чтобы вызвать и передать в нее событие-используем лямбда функцию

ttk.Button(text='1', command=lambda: enter_number('1')).grid(row=1,column=0)
ttk.Button(text='2', command=lambda: enter_number('2')).grid(row=1,column=1)
ttk.Button(text='3', command=lambda: enter_number('3')).grid(row=1,column=2)
ttk.Button(text='4', command=lambda: enter_number('4')).grid(row=2,column=0)
ttk.Button(text='5', command=lambda: enter_number('5')).grid(row=2,column=1)
ttk.Button(text='6', command=lambda: enter_number('6')).grid(row=2,column=2)
ttk.Button(text='7', command=lambda: enter_number('7')).grid(row=3,column=0)
ttk.Button(text='8', command=lambda: enter_number('8')).grid(row=3,column=1)
ttk.Button(text='9', command=lambda: enter_number('9')).grid(row=3,column=2)
ttk.Button(text='0', command=lambda: enter_number('0')).grid(row=4,column=0)

ttk.Button(text='C', command=clear_entry).grid(row=4,column=1)
ttk.Button(text='=', command=calc).grid(row=4,column=2)

ttk.Button(text='+', command=lambda: set_operation('+')).grid(row=1,column=3)
ttk.Button(text='-', command=lambda: set_operation('-')).grid(row=2,column=3)
ttk.Button(text='*', command=lambda: set_operation('*')).grid(row=3,column=3)
ttk.Button(text='/', command=lambda: set_operation('/')).grid(row=4,column=3)


window.mainloop()
