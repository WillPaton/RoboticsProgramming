import os
import inspect
from tkinter import *
from tkinter import ttk

local_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

#create window
window = Tk()
window.title("Shopping Cart")
window['height'] = window.winfo_screenheight() * 0.50# height = 50% of screen size
window['width'] = window['height'] * 0.8# width = 80% of window height

#Images
test_image = PhotoImage(file = (local_dir + "\\test_image.png"))


content = ttk.Frame(window)
main_frame = ttk.Frame(content)
main_frame['width'] = window['width']
main_frame['height'] = window['height']

#button
button = ttk.Button(content)
button['image'] = test_image

content.grid(column=0, row=0)
main_frame.grid(column=0, row=0)
button.grid(column=0, row=0)

window.mainloop()