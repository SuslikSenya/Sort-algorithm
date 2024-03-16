from random import randint
from tkinter import *
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time


def clear():
    en1.delete(0, END)


def insertion_sort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key
    return A


def downloadfile1():
    with open('значення.txt', 'r') as file:
        lines1 = file.readlines()
        lines = [element.strip() for element in lines1]

        en1.delete(0, "end")
        en1.insert(0, lines[0])


def active():
    value = var.get()
    en1.delete(0, END)
    if value == 1:
        button_load["state"] = "disabled"
    elif value == 2:
        button_load["state"] = "normal"

def active_graph():
    value = graph.get()
    buildGraphic["state"] = "normal"
    if value == 1:
        min_list["state"] = "disabled"
        max_list["state"] = "disabled"
        amount_list["state"] = "disabled"

    elif value == 2:
        min_list["state"] = "normal"
        max_list["state"] = "normal"
        amount_list["state"] = "normal"


def func1():
    value = var.get()
    if value == 1:
        p = int(en1.get())
        arr = []
        en1.delete(0, END)
        for _ in range(p):
            a = randint(-300, 300)
            arr.append(a)
            en1.insert(END, str(a) + ' ')
    elif value == 2:
        arr = en1.get().split()
        for i in range(len(arr)):
            arr[i] = int(arr[i])

    start_time = time.time()
    sortList = insertion_sort(arr)
    end_time = time.time()

    handGraphic.append((len(arr), end_time - start_time))

    result.delete(0, END)
    result.insert(0, sortList)


def build_graphic():
    value = graph.get()
    if value == 1:
        arr = insertion_sort(handGraphic)
        x = [i[0] for i in arr]
        y = [i[1] for i in arr]
        ax.clear()
        ax.plot(x, y)
        canvas1.draw()
    else:
        mn = int(min_list.get())
        mx = int(max_list.get())
        nm = int(amount_list.get())
        crok = int((mx - mn) / nm)
        randGraphic = []
        for i in range(mn, mx + 1, crok):
            arr = []
            for _ in range(i):
                a = randint(-300, 300)
                arr.append(a)
            start_time = time.time()
            insertion_sort(arr)
            end_time = time.time()
            randGraphic.append((i, end_time - start_time))
        x = [i[0] for i in randGraphic]
        y = [i[1] for i in randGraphic]
        ax.clear()
        ax.plot(x, y)
        canvas1.draw()


def teor_graphic():
    ax.clear()

    def func(x):
        x = x*x
        return x

    tx = np.linspace(0, 100, 10000)
    ty = func(tx)

    ax.plot(tx, ty, label='y = x * x')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    canvas2.draw()


win1 = Tk()
win1.title("Лабортаторна робота №2")
win1.geometry("650x550")
win1.resizable(False, False)
var = IntVar()
graph = IntVar()

tab_control = ttk.Notebook(win1)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab_control.add(tab1, text='Варіант, ФІО')
tab_control.add(tab2, text='Сортування')
tab_control.add(tab3, text='Графік')

tab_control.pack(expand=1, fill='both')

# ---------------------------------Первая вкладка----------------------------------

Label(tab1, text="ІО-24", font=("Times New Roman", 14, "normal")).place(x=10, y=10)
Label(tab1, text="Слободенюк О.А.", font=("Times New Roman", 14, "normal")).place(x=10, y=40)
Label(tab1, text="Варіант 24", font=("Times New Roman", 14, "normal")).place(x=10, y=70)
Label(tab1, text="Варіант Завдання:", font=("Times New Roman", 14, "normal")).place(x=10, y=100)

image1 = PhotoImage(file="Screenshot_1.png")
label_image = Label(tab1, image=image1)
label_image.place(x=10, y=130)

fig, ax = plt.subplots(figsize=(3.2, 3))
canvas1 = FigureCanvasTkAgg(fig, master=tab3)
canvas1.get_tk_widget().place(x=10, y=210)

canvas2 = FigureCanvasTkAgg(fig, master=tab3)
canvas2.get_tk_widget().place(x=330, y=210)

# ---------------------------------Вторая вкладка----------------------------------

# RadioBtn
Radiobutton(tab2, variable=var, value=2, text="Введення множин(через пробіл)",
            command=active, height=1, font=("Times New Roman", 14, "normal")).place(x=10, y=10)
Radiobutton(tab2, variable=var, value=1, text="Випадкова генерація(введіть кількість елементів множини)",
            command=active, height=1, font=("Times New Roman", 14, "normal")).place(x=10, y=40)

# Entry
label_a = Label(tab2, text="Масив данных", font=("Times New Roman", 14, "normal"))
label_a.place(x=10, y=70)

en1 = Entry(tab2, width=50)
en1.place(x=160, y=70)

x = [0]
y = [0]

# Btn
button_calc = Button(tab2, text="Розрахувати", width=10, height=1, command=func1)
button_calc.place(x=10, y=100)

button_load = Button(tab2, text="Завантажити із файлу", width=20, height=1, state='disabled', command=downloadfile1)
button_load.place(x=110, y=100)

button_clear = Button(tab2, text="Очистити данні", width=20, height=1, command=clear)
button_clear.place(x=280, y=100)

# Resault
label_result = Label(tab2, text="Результат виконання: ", font=("Times New Roman", 14, "normal"))
label_result.place(x=10, y=130)

result = Listbox(tab2, width=90, height=1)
result.place(x=10, y=160)
wscroll = Scrollbar(tab2, command=result.xview, orient=HORIZONTAL)
wscroll.place(x=10, y=190)
result.configure(xscrollcommand=wscroll.set)

# ---------------------------------Третья вкладка----------------------------------
handGraphic = [(0, 0)]

# RadioBtn
Radiobutton(tab3, variable=graph, value=2, text="На основі випадково згенерованих списків",
            command=active_graph, height=1, font=("Times New Roman", 14, "normal")).place(x=10, y=10)
Radiobutton(tab3, variable=graph, value=1, text="На основі списків відсортованих в розділі сортування",
            command=active_graph, height=1, font=("Times New Roman", 14, "normal")).place(x=10, y=40)

# Labels

Label(tab3, text="Кількість списків", font=("Times New Roman", 14, "normal")).place(x=10, y=70)
Label(tab3, text="Найменша кількість елементів у списку", font=("Times New Roman", 14, "normal")).place(x=10, y=100)
Label(tab3, text="Найбільша кількість елементів у списку", font=("Times New Roman", 14, "normal")).place(x=10, y=130)

# Entry
amount_list = Entry(tab3, width=20)
amount_list.place(x=350, y=75)
min_list = Entry(tab3, width=20)
min_list.place(x=350, y=105)
max_list = Entry(tab3, width=20)
max_list.place(x=350, y=135)

buildGraphic = Button(tab3, text="Побудувати графік", font="Times 12", width=40, command=build_graphic)
buildGraphic.place(x=10, y=170)
Button(tab3, text="Теоретичний графік", font="Times 12", width=40, command=teor_graphic).place(x=330, y=170)

tab_control.pack(expand=1, fill='both')


win1.mainloop()
