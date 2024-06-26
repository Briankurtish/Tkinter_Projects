# Python program to create a simple GUI 
# calculator using Tkinter 

# import everything from tkinter module 
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# globally declare the expression variable 
expression = "" 

# Function to update expression 
# in the text entry box 
def press(num): 
	# point out the global expression variable 
	global expression 

	# concatenation of string 
	expression = expression + str(num) 

	# update the expression by using set method 
	equation.set(expression) 

# Function to evaluate the final expression 
def equalpress(): 
	# Try and except statement is used 
	# for handling the errors like zero 
	# division error etc. 

	# Put that code inside the try block 
	# which may generate the error 
	try: 
		global expression 

		# eval function evaluate the expression 
		# and str function convert the result 
		# into string 
		total = str(eval(expression)) 

		equation.set(total) 

		# initialize the expression variable 
		# by empty string 
		expression = "" 

	# if error is generate then handle 
	# by the except block 
	except: 
		equation.set(" error ") 
		expression = "" 

# Function to clear the contents 
# of text entry box 
def clear(): 
	global expression 
	expression = "" 
	equation.set("") 

# Driver code 
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 
	style = ttk.Style("darkly")

	# set the background colour of GUI window 
	#gui.configure(background="light green") 

	# set the title of GUI window 
	gui.title("Simple Calculator") 

	# set the configuration of GUI window 
	gui.geometry("270x180") 

	# StringVar() is the variable class 
	# we create an instance of this class 
	equation = StringVar() 

	# create the text entry box for 
	# showing the expression . 
	expression_field = ttk.Entry(gui, textvariable=equation, bootstyle="primary") 

	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure . 
	expression_field.grid(columnspan=4, ipadx=70)

	# create a Buttons and place at a particular 
	# location inside the root window . 
	# when user press the button, the command or 
	# function affiliated to that button is executed . 
	button1 = ttk.Button(gui, text=' 1 ', bootstyle="primary", command=lambda: press(1), width=5) 
	button1.grid(row=2, column=0) 

	button2 = ttk.Button(gui, text=' 2 ', bootstyle="primary", command=lambda: press(2), width=5)  
	button2.grid(row=2, column=1) 

	button3 = ttk.Button(gui, text=' 3 ', bootstyle="primary", command=lambda: press(3), width=5) 
	button3.grid(row=2, column=2) 

	button4 = ttk.Button(gui, text=' 4 ', bootstyle="primary", command=lambda: press(4), width=5) 
	button4.grid(row=3, column=0) 

	button5 = ttk.Button(gui, text=' 5 ', bootstyle="primary", command=lambda: press(5), width=5) 
	button5.grid(row=3, column=1) 

	button6 = ttk.Button(gui, text=' 6 ', bootstyle="primary", command=lambda: press(6), width=5) 
	button6.grid(row=3, column=2) 

	button7 = ttk.Button(gui, text=' 7 ', bootstyle="primary", command=lambda: press(7), width=5) 
	button7.grid(row=4, column=0) 

	button8 = ttk.Button(gui, text=' 8 ', bootstyle="primary", command=lambda: press(8), width=5) 
	button8.grid(row=4, column=1) 

	button9 = ttk.Button(gui, text=' 9 ', bootstyle="primary", command=lambda: press(9), width=5) 
	button9.grid(row=4, column=2) 

	button0 = ttk.Button(gui, text=' 0 ', bootstyle="primary", command=lambda: press(0), width=5) 
	button0.grid(row=5, column=0) 

	plus = ttk.Button(gui, text=' + ', bootstyle="warning", command=lambda: press('+'), width=5) 
	plus.grid(row=2, column=3) 

	minus = ttk.Button(gui, text=' - ', bootstyle="warning", command=lambda: press('-'), width=5) 
	minus.grid(row=3, column=3) 

	multiply = ttk.Button(gui, text=' * ', bootstyle="warning", command=lambda: press('*'), width=5) 
	multiply.grid(row=4, column=3) 

	divide = ttk.Button(gui, text=' / ', bootstyle="warning", command=lambda: press('/'), width=5) 
	divide.grid(row=5, column=3) 

	equal = ttk.Button(gui, text=' = ', bootstyle="success", command=equalpress, width=5) 
	equal.grid(row=5, column=2) 

	clear = ttk.Button(gui, text=' Clear ', bootstyle="danger", command=clear, width=5) 
	clear.grid(row=5, column='1') 

	Decimal = ttk.Button(gui, text=' . ', bootstyle="primary", command=lambda: press('.'), width=5) 
	Decimal.grid(row=6, column=0) 

	# start the GUI 
	gui.mainloop() 
