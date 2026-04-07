# from tkinter import*
# root=Tk()
# root.title("My first GUI")
# root.geometry("500x500")
# # root.wm_iconbitmap("favicon.ico")
# root.resizable(False,False)
# root.mainloop()

# second one ..
import tkinter as tk
root = tk.Tk()  # for Creating window 
root.title("My First GUI")  # for setting Title....
root.geometry("550x550")  #for resizing the window size...
label = tk.Label(root, text="Hello Pradip 👋")
label.pack()

button = tk.Button(root, text="Click here!")
button.pack

root.mainloop()  # Run the app 