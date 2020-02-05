from tkinter import *
import numpy as np
from tkinter import messagebox
from tkinter import ttk
import math
import sys
from decimal import *

# Функции
def mid(event):
	root = Tk()

	# Параметры окна
	root.title("Вычисление среднего арифметического значения")
	root.resizable(0, 0)

	# Содержимое окна
	def mid(event):
		num = ent1.get()
		num_arr = num.split()
		num_arrInt = []
		num_len = len(num_arr)

		for i in range(num_len):
			t = float(num_arr[i])
			num_arrInt.append(t)

		arr_sum = np.sum(num_arrInt)
		middle = arr_sum / num_len
		middle = round(middle, 2)

		lbl1['text'] = middle


	lbl1 = Label(root, width=30, font=30)
	lbl2 = Label(root, text='Введите числа через пробел:', width=30, font=30)
	btn1 = Button(root, text='Вычислить', width=30, font=30)
	ent1 = Entry(root, width=30, font=30)

	lbl2.grid(row=0, column=0)
	ent1.grid(row=1, column=0)
	lbl1.grid(row=2, column=0)
	btn1.grid(row=3, column=0)

	btn1.bind("<Button-1>", mid)

	root.mainloop()


def tang(event):
	root = Tk()
	root.resizable(0, 0)

	# Параметры окна
	root.title("Вычисление тангенса")

	def mid(event):
		a = ent1.get()
		b = ent2.get()
		a = float(a)
		b = float(b)

		tang = a / b
		tang = round(tang, 3)

		lbl1['text'] = tang


	lbl1 = Label(root, width=15, font=30)
	form = Label(root, text='tang = a / b', font=20)
	lbl2 = Label(root, font=30, text='Введите длины катетов:')
	btn1 = Button(root, text='Вычислить', width=30, font=30)
	lbl3 = Label(root, text='a = ', font=30, width=5)
	ent1 = Entry(root, width=15, font=30)
	lbl4 = Label(root, font=30, text='b = ', width=5)
	ent2 = Entry(root, width=15, font=30)

	form.grid(row=0, column=0)
	lbl2.grid(row=1, column=0)
	lbl3.grid(row=2, column=0)
	ent1.grid(row=3, column=0)
	lbl4.grid(row=4, column=0)
	ent2.grid(row=5, column=0)
	lbl1.grid(row=6, column=0)
	btn1.grid(row=7, column=0)

	btn1.bind("<Button-1>", mid)

	root.mainloop()


def gip(event):
	root = Tk()
	root.resizable(0, 0)

	# Параметры окна
	root.title("Вычисление гипотенузы")

	def mid(event):
		num1 = ent1.get()
		num2 = ent2.get()
		num1 = float(num1)
		num2 = float(num2)

		sum1 = num1 ** 2 + num2 ** 2

		fact = math.sqrt(sum1)
		fact = round(fact, 2)

		lbl1['text'] = fact


	lbl1 = Label(root, width=15, font=30)
	lbl2 = Label(root, font=30, text='Введите длины катетов:')
	btn1 = Button(root, text='Вычислить', width=30, font=30)
	lbl3 = Label(root, text='a = ', font=30, width=5)
	ent1 = Entry(root, width=15, font=30)
	lbl4 = Label(root, font=30, text='b = ', width=5)
	ent2 = Entry(root, width=15, font=30)

	lbl2.grid(row=0, column=0)
	lbl3.grid(row=1, column=0)
	ent1.grid(row=2, column=0)
	lbl4.grid(row=3, column=0)
	ent2.grid(row=4, column=0)
	lbl1.grid(row=5, column=0)
	btn1.grid(row=6, column=0)

	btn1.bind("<Button-1>", mid)

	root.mainloop()

	
def calc(event):
	root = Tk() 
	root.title("Калькулятор")
	root.resizable(0, 0)


	bttn_list = [
	"7", "8", "9", "+", "*", 
	"4", "5", "6", "-", "/",
	"1", "2", "3",  "=", "xⁿ",
	"0", ".", "±",  "C",
	"Exit", "π", "sin", "cos",
	"(", ")","n!","√2", ]

	r = 1
	c = 0
	for i in bttn_list:
	    rel = ""
	    cmd=lambda x=i: calc(x)
	    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
	    c += 1
	    if c > 4:
	        c = 0
	        r += 1

	calc_entry = Entry(root, width = 33)
	calc_entry.grid(row=0, column=0, columnspan=5)

	#логика калькулятора
	def calc(key):
	    global memory
	    if key == "=":
	#исключение написания слов
	        str1 = "-+0123456789.*/)(" 
	        if calc_entry.get()[0] not in str1:
	            calc_entry.insert(END, "First symbol is not number!")
	            messagebox.showerror("Error!", "You did not enter the number!")
	#исчисления
	        try:
	            result = eval(calc_entry.get())
	            calc_entry.insert(END, "=" + str(result))
	        except:
	            calc_entry.insert(END, "Error!")
	            messagebox.showerror("Error!", "Check the correctness of data")

	#очищение поля ввода
	    elif key == "C":
	        calc_entry.delete(0, END)

	    elif key == "±":
	        if "=" in calc_entry.get():
	            calc_entry.delete(0, END)
	        try:
	            if calc_entry.get()[0] == "-":
	                calc_entry.delete(0)
	            else:
	                calc_entry.insert(0, "-")
	        except IndexError:
	            pass
	    elif key == "π":
	        calc_entry.insert(END, math.pi)
	    elif key == "Exit":
	        root.after(1,root.destroy)
	        sys.exit
	    elif key == "xⁿ":
	        calc_entry.insert(END, "**")
	    elif key == "sin":
	        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
	    elif key == "cos":
	        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
	    elif key == "(":
	        calc_entry.insert(END, "(")
	    elif key == ")":
	        calc_entry.insert(END, ")")
	    elif key == "n!":
	        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
	    elif key == "√2":
	        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
	    else:
	        if "=" in calc_entry.get():
	            calc_entry.delete(0, END)
	        calc_entry.insert(END, key)

	root.mainloop()


def sqr(event):
	root = Tk()

	# Параметры окна
	root.title("Вычисление корня квадратного уравнения")
	root.resizable(0, 0)

	# Содержимое окна
	def mid(event):
		num = ent1.get()
		x1  = 0
		x2 = 0

		a = ent1.get()
		b = ent2.get()
		c = ent3.get()

		a = float(a)
		b = float(b)
		c = float(c)

		d = b ** 2 - 4 * a * c

		if d > 0:
			x1 = (-b + math.sqrt(d)) / (2 * a)
			x2 = (-b - math.sqrt(d)) / (2 * a)

			x1 = round(x1, 3)
			x2 = round(x2, 3)

			lbl1['text'] = x1
			lbl2['text'] = x2
		elif(d == 0):
			x1 = -b / (2 * a)
			lbl1['text'] = x1
			lbl2['text'] = ''
		else:
			lbl1['text'] = 'Корней нет'
			lbl2['text'] = ''


	lbl1 = Label(root, width=15, font=30)
	lbl2 = Label(root, width=15, font=30)
	lbl3 = Label(root, width=20, font=30, text='Введите множители:')
	btn1 = Button(root, text='Вычислить', width=15, font=30)
	txt_a = Label(root, text='a = ', font=30)
	txt_b = Label(root, text='b = ', font=30)
	txt_c = Label(root, text='c = ', font=30)
	ent1 = Entry(root, font=30)
	ent2 = Entry(root, font=30)
	ent3 = Entry(root, font=30)

	lbl3.grid(row=0, column=0)
	txt_a.grid(row=1, column=0)
	ent1.grid(row=2, column=0)
	txt_b.grid(row=3, column=0)
	ent2.grid(row=4, column=0)
	txt_c.grid(row=5, column=0)
	ent3.grid(row=6, column=0)
	lbl1.grid(row=7, column=0)
	lbl2.grid(row=8, column=0)
	btn1.grid(row=9, column=0)

	btn1.bind("<Button-1>", mid)

	root.mainloop()


def dk(event):
	def gcd():
	    n1,n2 = correct()
	    prime1 = prime(n1)
	    prime2 = prime(n2)
	    gcd,lcm = gcd_lcm(n1,n2)
	    lab_prime_n1["text"] = prime1
	    lab_prime_n2["text"] = prime2
	    lab_gcd["text"] = gcd
	    lab_lcm["text"] = lcm
	 
	def correct():
	    a = ent_n1.get()
	    b = ent_n2.get()
	    try:
	        a = int(a)
	    except ValueError:
	        a = 0
	        ent_n1.delete(0,END)
	        ent_n1.insert(0,0)
	    try:
	        b = int(b)
	    except ValueError:
	        b = 0
	        ent_n2.delete(0,END)
	        ent_n2.insert(0,0)
	    return abs(a), abs(b)
	 
	def prime(n):
	    a = []
	    while n > 1:
	        i = 2
	        while 1:
	            if n%i==0:
	                a.append(i)
	                n //= i
	                break
	            else:
	                i += 1
	    return a
	 
	def gcd_lcm(a,b):
	    m = a*b
	    while a!=0 and b!=0:
	        if a > b: a %= b
	        else: b %= a
	    g = a + b
	    l = m // g
	    return g, l
	 
	root1 = Tk()
	root.resizable(0, 0)
	root1.title('НОД, НОК и разложение на простые числа')
	lab_n1 = Label(root1, text="Число 1")
	lab_n1.grid(row=2,column=0)
	 
	lab_n2 = Label(root1, text="Число 2")
	lab_n2.grid(row=3,column=0)
	 
	ent_n1 = Entry(root1, width=10,bg="white")
	ent_n1.grid(row=2,column=1)
	 
	ent_n2 = Entry(root1, width=10,bg="white")
	ent_n2.grid(row=3,column=1)
	 
	lab_prime = Label(root1, text="Простые сомножители:")
	lab_prime.grid(row=1,column=3,columnspan=2)
	 
	lab_prime_n1 = Label(root1, bg="white")
	lab_prime_n1.grid(row=2,column=3,columnspan=2)
	 
	lab_prime_n2 = Label(root1, bg="white")
	lab_prime_n2.grid(row=3,column=3,columnspan=2)
	 
	lab_gcd_ = Label(root1, text="НОД",bg="lightgreen",width=7)
	lab_gcd_.grid(row=4,column=3)
	lab_gcd = Label(root1, bg="lightgreen",width=10)
	lab_gcd.grid(row=4,column=4)
	 
	lab_lcm_ = Label(root1, text="НОК",bg="lightblue",width=7)
	lab_lcm_.grid(row=5,column=3)
	lab_lcm = Label(root1, bg="lightblue",width=10)
	lab_lcm.grid(row=5,column=4)
	 
	but = Button(root1, text="Вычислить",command=gcd,pady=10)
	but.grid(row=4,column=0,rowspan=2,columnspan=2,sticky=W+N+S+E)
	 
	root1.mainloop()


def new_win():
	root = Tk()
	root.title("О программе")
	root.resizable(0, 0)

	lbl1 = Label(root, text='© Michurin Andrey 2020\n'
		'По всем вопросам писать на\n M14ur1nAK@yandex.ru',
		 fg='blue', bg='white')
	lbl1.grid(row=0, column=0)

	root.mainloop()

# Параметры экрана
root = Tk()
root.title("Главное меню")
root.resizable(0, 0)

# Код
main_menu = Menu(root)
root.configure(menu=main_menu)

first_item = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Инфо", menu=first_item)
first_item.add_command(label="О программе", command=new_win)


lbl = Label(root, text='Slover',width=27 , font=30, fg='blue', bg='white')

btn1 = Button(root, text='Среднее\n'
						'арифмитическое', width=20, fg='blue', bg='white')
btn2 = Button(root, text='Корень \nквадратного уравнения', width=20, fg='blue', bg='white')

btn3 = Button(root, text='Гипотенуза', width=20, fg='blue', bg='white')

btn4 = Button(root, text='Калькулятор', width=20, fg='blue', bg='white')

btn5 = Button(root, text='\nТангенс\n', width=20, fg='blue', bg='white')

btn6 = Button(root, text='НОД, НОК и \n'
						'разложение \n'
						'на простые числа', width=20, fg='blue', bg='white')

btn1.bind("<Button-1>", mid)
btn2.bind("<Button-1>", sqr)
btn3.bind("<Button-1>", gip)
btn4.bind("<Button-1>", calc)
btn5.bind("<Button-1>", tang)
btn6.bind("<Button-1>", dk)

lbl.grid(row=0, columnspan=2)
btn1.grid(row= 1, column=0)
btn2.grid(row=1, column=1)
btn3.grid(row=2, column=0)
btn4.grid(row=2, column=1)
btn5.grid(row=3, column=0)
btn6.grid(row=3, column=1)

root.mainloop()