from tkinter import *



root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)
#root.iconbitmap('calu.ico')

e = Entry(root, width=58, borderwidth=20)
e.grid(row=0, column=0, columnspan=25,padx=45,pady=45)





def button_click(number):
	 current= e.get()
	 e.delete(0, END)
	 e.insert(0, str(current) + str(number) )


def button_clear():
	e.delete(0, END)


def button_add():
	first_number = e.get()
	global f_num 
	global math
	math ="add"
	f_num = float(first_number)
	e.delete(0, END)
  

def button_subtract():
	first_number = e.get()
	global f_num 
	global math
	math ="sub"
	f_num = float(first_number)
	e.delete(0, END)
  

def button_multiply():
	first_number = e.get()
	global f_num 
	global math
	math ="mul"
	f_num = float(first_number)
	e.delete(0, END)
  	

def button_divide():
	first_number = e.get()
	global f_num 
	global math
	math ="div"
	f_num = float(first_number)
	e.delete(0, END)
  

def button_sqrt():
	number=float(e.get())
	e.delete(0, END)
	e.insert(0, number**0.5)
	return


def button_sq():
	number=float(e.get())
	e.delete(0, END)
	e.insert(0, number**2)


def button_fact():
	
		number = int(e.get())
		fact=1
		try:
			while number > 0:
				fact=fact*number
				number -= 1
			e.delete(0, END)
			e.insert(0, fact)
		except Exception:
			e.delete(0, END)
			e.insert(0, "ERROR!")

def button_equal():
	second_number = e.get()
	e.delete(0, END)
	
	if math == "add":
		e.insert(0, f_num + float(second_number))

	if math == "sub":
		e.insert(0, f_num - float(second_number))

	if math == "mul":
		e.insert(0, f_num * float(second_number))

	if math == "div":
		e.insert(0, f_num / float(second_number))
	    






button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1), foreground="white", background="Blue")
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2), foreground="black", background="white")
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3), foreground="white", background="Blue")
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4), foreground="black", background="white")
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5), foreground="white", background="Blue")
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6), foreground="black", background="white")
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7), foreground="white", background="Blue")
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8), foreground="black", background="white")
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9), foreground="white", background="Blue")
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0), foreground="black", background="white")
button_dot = Button(root, text=".", padx=40, pady=20, command=lambda: button_click("."), foreground="white", background="Blue")
button_add = Button(root, text="+", padx=39, pady=50, command= button_add, foreground="black", background="white")
button_subtract = Button(root, text="-", padx=39, pady=20, command= button_subtract, foreground="white", background="Blue" )
button_multiply = Button(root, text="x", padx=39, pady=20, command= button_multiply, foreground="black", background="white")
button_divide = Button(root, text="/", padx=39, pady=20, command= button_divide, foreground="white", background="Blue")
button_sqrt = Button(root, text="√x", padx=34, pady=20, command= button_sqrt, foreground="black", background="white")
button_sq= Button(root, text="x²", padx=34, pady=20, command= button_sq, foreground="white", background="Blue")
button_fact = Button(root, text="x!", padx=34, pady=20, command= button_fact, foreground="black", background="white")

button_equal = Button(root, text="=", padx=40, pady=20, command=button_equal, foreground="black", background="white")
button_clear = Button(root, text="Clear",padx=224, pady=20, command= button_clear, foreground="White", background="Black")



button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)  

button_0.grid(row=4,column=0)
button_dot.grid(row=4,column=1)
button_clear.grid(row=5, column=0, columnspan=5)
button_add.grid(row=3, rowspan=2, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=1, column=3)
button_divide.grid(row=1, column=4)
button_sqrt.grid(row=2, column=4)
button_sq.grid(row=3, column=4)
button_fact.grid(row=4, column=4)
button_equal.grid(row=4, column=2)




#button_quit= button(root,text="Exit",command=root.quit)
#button_quit.grid(row=, column=, columnspan=)



root.mainloop()

