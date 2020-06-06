#simple calculator
from tkinter import *

window = Tk()
window.geometry("312x324")  # size of the window width:- 500, height:- 375
window.resizable(0, 0)  # this prevents from resizing the window
window.title("Calculator")


def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set(expression)

def button_equal():
    global expression
    result = str(eval(expression)) # eval is a function that takes in a string and evaluates
    input_text.set(result)
    expression = ""

expression = ""

input_text = StringVar()

# frame for input field
input_frame = Frame(window, width=300, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=1)
input_frame.pack(side=TOP)



input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)
input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field


# frame for buttons
button_frame = Frame(window, width=312, height=272.5, bg="grey")
button_frame.pack()


# first row
button_clear = Button(button_frame, text="C", fg="black", width=32, height=3, bd=0, bg="#eee",
                      command=button_clear).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
button_divide = Button(button_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                       command=lambda: button_click("/")).grid(row=0, column=3, padx=1, pady=1)
# second row
button_7 = Button(button_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(7)).grid(row=1, column=0, padx=1, pady=1)
button_8 = Button(button_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(8)).grid(row=1, column=1, columnspan=1, padx=1, pady=1)
button_9 = Button(button_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(9)).grid(row=1, column=2, padx=1, pady=1)
button_multiply = Button(button_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                         command=lambda: button_click("*")).grid(row=1, column=3, padx=1, pady=1)

# third row
button_4 = Button(button_frame, text="4", fg="black",width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(4)).grid(row=2, column=0, padx=1,pady=1)
button_5 = Button(button_frame, text="5", fg="black",width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(5)).grid(row=2, column=1, padx=1,pady=1)
button_6 = Button(button_frame, text="6", fg="black",width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(6)).grid(row=2, column=2, padx=1,pady=1)
button_minus = Button(button_frame, text="-", fg="black",width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                      command=lambda: button_click('-')).grid(row=2, column=3, padx=1, pady=1)

# fourth row
button_1 = Button(button_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(1)).grid(row=3, column=0, padx=1,pady=1)
button_2 = Button(button_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(2)).grid(row=3, column=1, padx=1,pady=1)
button_3 = Button(button_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(3)).grid(row=3, column=2, padx=1,pady=1)
button_add = Button(button_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                    command=lambda: button_click('+')).grid(row=3, column=3, padx=1,pady=1)


# fifth row
button_0 = Button(button_frame, text="0",  fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
                  command=lambda: button_click(0)).grid(row=4, column=0, columnspan=2, padx=1,pady=1)
button_decimal = Button(button_frame, text='.',  fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                        command=lambda: button_click('.')).grid(row=4, column=2, padx=1,pady=1)
button_equal1 = Button(button_frame, text="=",  fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                      command=lambda: button_equal()).grid(row=4, column=3, padx=1,pady=1)

window.mainloop()
