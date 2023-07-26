from tkinter import *


def button_press(number):
    
    global equation_text
    
    equation_text = equation_text + str(number)
    equation_label.set(equation_text)

def equals():
    global equation_text
    
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
        
    except SyntaxError:
        equation_label.set("Syntax error")
        equation_text = ""
        
    except ZeroDivisionError:
        equation_label.set("Arithmetic error")
        equation_text = "" 

def clear():
    global equation_text
    
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Simple-Calculator")
window.geometry("470x490")
window.configure(bg="black")


equation_text = ""
equation_label = StringVar()
label = Label(window, textvariable= equation_label, font = ('italic', 20), bg='green', width=31, height=2)
label.pack()

frame = Frame(window, bg='grey')
frame.pack()


button1 = Button(frame, text = 1, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text = 2, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text = 3, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text = 4, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text = 5, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text = 6, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(6))
button6.grid(row=1, column=2)

button7 = Button(frame, text = 7, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text = 8, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text = 9, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(9))
button9.grid(row=2, column=2)

button0 = Button(frame, text = 0, height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press(0))
button0.grid(row=3, column=1)

decimal = Button(frame, text = '.', height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press('.'))
decimal.grid(row=3, column=0)

plus = Button(frame, text = '+', height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press('+'))
plus.grid(row=3, column=2)

minus = Button(frame, text = '-', height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press('-'))
minus.grid(row=3, column=3)

multiply = Button(frame, text = '*', height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press('*'))
multiply.grid(row=2, column=3)

divide = Button(frame, text = '/', height = 3, width = 10, font = 35, bg='grey', command=lambda: button_press('/'))
divide.grid(row=1, column=3)

clear = Button(frame, text = 'clear', height = 3, width = 10, font = 35, bg='grey', command=clear)
clear.grid(row=0, column=3)

equalto = Button(frame, text = '=', height = 3, width = 10, font = 35, bg='grey', command=equals)
equalto.grid(row= 4, column=1)  

#label3 = Label(frame, text="Sk-calculators", font=35, bg='grey', fg='black', bd=4, relief=SOLID)
#label3.grid(row=4, column=2)


window.mainloop()