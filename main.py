import os
from tkinter import *
from tkinter import ttk
from typing import List, Any
import time

root = Tk()
root.title("Kalkulator w Python")

#konfiguracja okna
windowHeight = 300
windowWidth = 500
root.configure(height=windowHeight, width=windowWidth, bg="lightgray")
root.resizable(True, True)

#wprowadzanie
u_entry = Entry(root, width=19, borderwidth=2, justify=RIGHT)
u_entry.grid(row=0, column=0, columnspan=3, padx=10, pady=3, sticky="nsew")

#funkcja wprowadzania
def button_click(number):
    current = u_entry.get()
    u_entry.delete(0, END)
    u_entry.insert(0, str(current) + str(number))

#funkcja czyszczenia
def button_clear():
    u_entry.delete(0, END)

#funkcja dodawania
def button_add():
    try:
        first_number = u_entry.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        u_entry.delete(0, END)
    except ValueError:
        u_entry.insert(0, "Input a number")

#funkcja EQUAL
def button_equal():
    try:
        second_number = u_entry.get()
        u_entry.delete(0, END)

        if math == "addition":
            u_entry.insert(0, f_num + int(second_number))
        if math == "subtraction":
            u_entry.insert(0, f_num - int(second_number))
        if math == "multiplication":
            u_entry.insert(0, f_num * int(second_number))
        if math == "division":
            try:
                u_entry.insert(0, f_num / int(second_number))
            except ZeroDivisionError:
                u_entry.insert(0, "Cannot divide by 0")
    except NameError:
        u_entry.insert(0, "Input a number")
#funkcja odejmowania
def button_subtract():
    try:
        first_number = u_entry.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        u_entry.delete(0, END)
    except ValueError:
        u_entry.insert(0, "Input a number")

#funkcja mnożenia
def button_multiplication():
    try:
        first_number = u_entry.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        u_entry.delete(0, END)
    except ValueError:
        u_entry.insert(0, "Input a number")

#funkcja dzielenia
def button_division():
    try:
        first_number = u_entry.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        u_entry.delete(0, END)
    except ValueError:
        u_entry.insert(0, "Input a number")



#definiowanie przycisków
#numery
button1 = Button(root, text="1", fg="blue", padx=50, pady=25, command=lambda: button_click(1))
button2 = Button(root, text="2", fg="blue", padx=50, pady=25, command=lambda: button_click(2))
button3 = Button(root, text="3", fg="blue", padx=50, pady=25, command=lambda: button_click(3))
button4 = Button(root, text="4", fg="blue", padx=50, pady=25, command=lambda: button_click(4))
button5 = Button(root, text="5", fg="blue", padx=50, pady=25, command=lambda: button_click(5))
button6 = Button(root, text="6", fg="blue", padx=50, pady=25, command=lambda: button_click(6))
button7 = Button(root, text="7", fg="blue", padx=50, pady=25, command=lambda: button_click(7))
button8 = Button(root, text="8", fg="blue", padx=50, pady=25, command=lambda: button_click(8))
button9 = Button(root, text="9", fg="blue", padx=50, pady=25, command=lambda: button_click(9))
button0 = Button(root, text="0", fg="blue", padx=50, pady=25, command=lambda: button_click(0))
buttonadd = Button(root, text="+", fg="blue", padx=50, pady=25, command=lambda: button_add())
buttonequal = Button(root, text="=", fg ="blue", padx=106, pady=25, command=lambda: button_equal())
buttonclear = Button(root, text="Clear", fg="blue", padx=98, pady=25, command=lambda: button_clear())
buttonsubtract = Button(root, text="-", fg="blue", padx=51, pady=25, command=lambda: button_subtract())
buttonmultiplication = Button(root, text="*", fg="blue", padx=50, pady=25, command=lambda: button_multiplication())
buttondivision = Button(root, text="/", fg="blue", padx=50, pady=25, command=lambda: button_division())


#umieszczanie przycisków
#rzad 1
button1.grid(row=3, column=0, sticky="nsew")
button2.grid(row=3, column=1, sticky="nsew")
button3.grid(row=3, column=2, sticky="nsew")
#rzad 2
button4.grid(row=2, column=0, sticky="nsew")
button5.grid(row=2, column=1, sticky="nsew")
button6.grid(row=2, column=2, sticky="nsew")
#rzad 3
button7.grid(row=1, column=0, sticky="nsew")
button8.grid(row=1, column=1, sticky="nsew")
button9.grid(row=1, column=2, sticky="nsew")
#rzad 4
button0.grid(row=4, column=0, sticky="nsew")

#przyciski funkcyjne
buttonclear.grid(row=4, column=1, columnspan=2, sticky="nsew")
buttonadd.grid(row=5, column =0, sticky="nsew")
buttonequal.grid(row=5, column = 1, columnspan=2, sticky="nsew")
buttonsubtract.grid(row=6, column=0, sticky="nsew")
buttonmultiplication.grid(row=6, column=1, sticky="nsew")
buttondivision.grid(row=6, column=2, sticky="nsew")


#lista przyciskow
button_list = [u_entry, button1, button2, button3, button4, button5, button6, button7, button8, button9, button0, buttonadd, buttonequal, buttondivision, buttonmultiplication, buttonclear, buttonsubtract]

#definiowanie row_number i column_number
row_number = 0
column_number = 0

#petla do ustawiania wagi kolumn i rzedow
for button in button_list:
    if row_number < 7:
        root.rowconfigure(row_number, weight=1)
        row_number += 1
    if column_number < 3:
        root.columnconfigure(column_number, weight=1)
        column_number += 1


#dynamiczne zmienianie wielkosci fonta
def resize(e):
    size = e.width / 20
    font_resize = [button.config(font=("Helvetica", int(size))) for button in button_list]
root.bind('<Configure>', resize)




root.mainloop()