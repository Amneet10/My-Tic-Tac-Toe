from tkinter import *
from tkinter import messagebox

window = Tk()

window.title("Welcome to Amneet Tic-Tac-Toe ")
window.geometry("400x300")

lbl = Label(window, text="Tic-tac-toe Game", font=('Helvetica', '15'))
lbl.grid(row=0, column=0)
lbl = Label(window, text="Player 1: X", font=('Helvetica', '10'))
lbl.grid(row=1, column=0)
lbl = Label(window, text="Player 2: O", font=('Helvetica', '10'))
lbl.grid(row=2, column=0)

flag = True
def setBtnValue(btnref):
    global flag
    if flag:
        btnref["text"] = 'X'
        flag = False
    else:
        btnref["text"] ='O'
        flag = True


btn1 = Button(window, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: setBtnValue(btn1))
btn1.grid(column=1, row=1)
btn2 = Button(window, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: setBtnValue(btn2))
btn2.grid(column=2, row=1)
btn3 = Button(window, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: setBtnValue(btn3))
btn3.grid(column=3, row=1)
btn4 = Button(window, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'), command=lambda: setBtnValue(btn4))
btn4.grid(column=1, row=2)
btn5 = Button(window, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: setBtnValue(btn5))
btn5.grid(column=2, row=2)
btn6 = Button(window, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: setBtnValue(btn6))
btn6.grid(column=3, row=2)
btn7 = Button(window, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: setBtnValue(btn7))
btn7.grid(column=1, row=3)
btn8 = Button(window, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: setBtnValue(btn8))
btn8.grid(column=2, row=3)
btn9 = Button(window, text=" ", bg="green", fg="Black", width=3, height=1, font=('Helvetica', '20'),command=lambda: setBtnValue(btn9))
btn9.grid(column=3, row=3)

    
      





window.mainloop()