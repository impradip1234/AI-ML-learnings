# positioning with Tkinter's Grid(),Pack() and Place () system 

from tkinter import *

root = Tk()
root.title("Pradip")
root.geometry("700x700+0+0")

# Labels
lbl1 = Label(root, text="pradip yadav is here......", font=('times new roman',30))
lbl2 = Label(root, text="kya hal chal..", font=('times new roman',30))
lbl3 = Label(root, text="kay hal chal maharaj..", font=('times new roman',30))

# Packing
lbl1.pack(side=TOP)
lbl2.pack(side=LEFT)
lbl3.pack(side=RIGHT)

root.mainloop()