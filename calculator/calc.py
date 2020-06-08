from tkinter import *


def button_clicked(numbers, text_input):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)


def clear_disp(text_input):
    global operator

    operator = ""
    text_input.set(operator)


def button_equal(text_input):
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)


def cut_bttn(text_input):
    global operator
    temp = ""
    for i in range(len(operator) - 1):
        temp += operator[i]
    operator = temp
    text_input.set(operator)


def braces(numbers, text_input):
    global operator, count
    count += 1
    temp = ""
    if count == 1:
        temp += str(numbers)[0]
    if count == 2:
        temp += str(numbers)[1]
        count = 0

    operator = operator + temp
    text_input.set(operator)


operator = ""
count = 0


def run_calc():
    calc = Tk()

    calc.title("CALCULATOR")
    text_input = StringVar()

    txtDisplay = Entry(calc, font={'arial', 20, 'bold'}, textvariable=text_input, bd=30, insertwidth=8,
                       bg='powder blue', justify='right').grid(columnspan=8)

    brac = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='()', command=lambda: braces("()", text_input)).grid(row='1', column='0')

    square = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                    bd='8', text='1/x', command=lambda: button_clicked("1/", text_input)).grid(row='1', column='1')

    decimal = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                     bd='8', text='.', command=lambda: button_clicked(".", text_input)).grid(row='1', column='2')

    cut = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                 bd='8', text='cut', command=lambda: cut_bttn(text_input)).grid(row='1', column='3')

    """========================================================================================================="""

    btn7 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='7', command=lambda: button_clicked(7, text_input)).grid(row='2', column='0')

    btn8 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='8', command=lambda: button_clicked(8, text_input)).grid(row='2', column='1')

    btn9 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='9', command=lambda: button_clicked(9, text_input)).grid(row='2', column='2')

    addition = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                      bd='8', text='+', command=lambda: button_clicked("+", text_input)).grid(row='2', column='3')

    """====================================================================================================="""

    btn4 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='4', command=lambda: button_clicked(4, text_input)).grid(row='3', column='0')

    btn5 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='5', command=lambda: button_clicked(5, text_input)).grid(row='3', column='1')

    btn6 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='6', command=lambda: button_clicked(6, text_input)).grid(row='3', column='2')

    sub = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                 bd='8', text='-', command=lambda: button_clicked("-", text_input)).grid(row='3', column='3')

    """========================================================================================================"""

    btn1 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='1', command=lambda: button_clicked(1, text_input)).grid(row='4', column='0')

    btn2 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='2', command=lambda: button_clicked(2, text_input)).grid(row='4', column='1')

    btn3 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='3', command=lambda: button_clicked(3, text_input)).grid(row='4', column='2')

    mul = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                 bd='8', text='*', command=lambda: button_clicked("*", text_input)).grid(row='4', column='3')

    """========================================================================================================="""

    clear = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                   bd='8', text='C', command=lambda: clear_disp(text_input)).grid(row='5', column='0')

    btn0 = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                  bd='8', text='0', command=lambda: button_clicked(0, text_input)).grid(row='5', column='1')

    equal = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                   bd='8', text='=', command=lambda: button_equal(text_input)).grid(row='5', column='2')

    divide = Button(calc, font={'arial', 20, 'bold'}, padx='16', pady='16', fg='black', bg='powder blue',
                    bd='8', text='/', command=lambda: button_clicked("/", text_input)).grid(row='5', column='3')

    calc.mainloop()


run_calc()
