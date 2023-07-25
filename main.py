from tkinter import *

win = Tk()
win.title('Sea Battle')
win.resizable(False, False)
win.geometry('600x300')
win.configure(bg='#87CEFA')
logo = PhotoImage(file='icon.png')
win.iconphoto(False, logo)

win.mainloop()