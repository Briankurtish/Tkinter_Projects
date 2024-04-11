# Python program to create 
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# import filedialog module
from tkinter import filedialog

# Function for opening the 
# file explorer window
def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",
										title = "Select a File",
										filetypes = (("Text files",
														"*.txt*"),
													("all files",
														"*.*")))
	
	# Change label contents
	label_file_explorer.configure(text="File Opened: "+filename)
	
	
																								
# Create the root window
window = ttk.Window(themename="darkly")

# Set window title
window.title('File Explorer')

# Set window size
window.geometry("700x200")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer = Label(window, 
							text = "File Explorer using Tkinter",
							width = 100, height = 4, 
							fg = "blue")

	
button_explore = ttk.Button(window, 
						text = "Browse Files",
						command = browseFiles, bootstyle="primary", width=10) 

button_exit = ttk.Button(window, 
					text = "Exit",
					command = exit, bootstyle="danger", width=10) 

# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer.grid(column = 1, row = 1)

button_explore.grid(column = 1, row = 2)

button_exit.grid(column = 1,row = 3)

# Let the window wait for any events
window.mainloop()
