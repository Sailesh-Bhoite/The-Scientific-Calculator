from tkinter import *
from tkinter import ttk
import math  # We are using math module in the string, so it assumes to be not in use.

"""

PROBLEMS to be solved:
Correction for backspace function - after clicking equal.

"""

equation: str = ""  # Initially, equation is empty.
equal: int = 0  # Used for auto-clear when something is typed after calculation.
bracket: int = 0  # Flag for indicating number of closing-brackets required.
tri: int = 0  # Flag to indicate the trigonometric function is used.
op: list = ["*", "+", "/", "-", "="]
sqr: int = 0  # Square root indicator for cutting the sqrt's bracket


def scientific_on():
    """What should be done when scientific mode is on?"""
    win.geometry("608x615+350+20")
    win.after(50, lambda: b_trigo.grid(row=8, column=0, ipadx=7, ipady=10, columnspan=2))
    win.after(100, lambda: b_logarithm.grid(row=8, column=2, ipadx=8, ipady=10))
    win.after(150, lambda: b_power.grid(row=8, column=3, ipadx=10, ipady=10))
    # Just for checking button is on or not
    print("\nScientific Mode ON")


def normal_on():
    """What should be done when normal mode is on?"""
    # Hiding buttons under 'b_trigo' Button
    b_tan_inv.grid_forget()
    b_cos_inv.grid_forget()
    b_sin_inv.grid_forget()
    b_tan.grid_forget()
    b_cos.grid_forget()
    b_sin.grid_forget()
    win.after(105, lambda: b_trigo.grid_forget())

    # Hiding buttons under 'b_logarithm' Button
    b_log.grid_forget()
    b_Ln.grid_forget()
    b_exp.grid_forget()
    win.after(55, lambda: b_logarithm.grid_forget())

    # Hiding buttons under 'b_power' Button
    b_pow.grid_forget()
    b_sqr.grid_forget()
    b_fact.grid_forget()
    win.after(5, lambda: b_power.grid_forget())

    # Setting Default Text on the buttons
    trigo_text.set("Trigonometry\u25bc")
    loga_text.set("Logarithm\u25bc")
    fact_text.set("Power/Fact\u25bc")

    win.after(110, lambda: win.geometry("608x405+350+20"))

    # Just for checking button is on or not
    print("\nNormal Mode ON")


def TrigoButtonClick():
    if b_sin.winfo_ismapped():
        trigo_text.set("Trigonometry\u25bc")
        b_tan_inv.grid_forget()
        win.after(50, lambda: b_cos_inv.grid_forget())
        win.after(100, lambda: b_sin_inv.grid_forget())

        win.after(150, lambda: b_tan.grid_forget())
        win.after(200, lambda: b_cos.grid_forget())
        win.after(250, lambda: b_sin.grid_forget())

    else:
        trigo_text.set("Trigonometry\u25b2")
        b_sin.grid(row=9, column=0, ipady=10, ipadx=10)
        win.after(50, lambda: b_cos.grid(row=10, column=0, ipady=10, ipadx=10))
        win.after(100, lambda: b_tan.grid(row=11, column=0, ipady=10, ipadx=10))

        win.after(150, lambda: b_sin_inv.grid(row=9, column=1, ipadx=10, ipady=10))
        win.after(200, lambda: b_cos_inv.grid(row=10, column=1, ipadx=10, ipady=10))
        win.after(250, lambda: b_tan_inv.grid(row=11, column=1, ipadx=10, ipady=10))


def LogarithmButtonClick():
    if b_log.winfo_ismapped():
        loga_text.set("Logarithm\u25bc")
        b_exp.grid_forget()
        win.after(50, lambda: b_Ln.grid_forget())
        win.after(100, lambda: b_log.grid_forget())
    else:
        loga_text.set("Logarithm\u25b2")
        b_log.grid(row=9, column=2, ipady=10, ipadx=10)
        win.after(50, lambda: b_Ln.grid(row=10, column=2, ipady=10, ipadx=10))
        win.after(100, lambda: b_exp.grid(row=11, column=2, ipady=10, ipadx=10))


def FactorialClick():
    if b_fact.winfo_ismapped():  # If button is present
        fact_text.set("Power/Fact\u25bc")
        b_pow.grid_forget()
        win.after(50, lambda: b_sqr.grid_forget())
        win.after(100, lambda: b_fact.grid_forget())
    else:  # If button is absent
        fact_text.set("Power/Fact\u25b2")
        b_fact.grid(row=9, column=3, ipady=10, ipadx=10)
        win.after(50, lambda: b_sqr.grid(row=10, column=3, ipady=10, ipadx=10))
        win.after(100, lambda: b_pow.grid(row=11, column=3, ipady=10, ipadx=10))


def click(number):
    """Just for displaying entries in text box and appending to 'equation' variable"""
    global tri
    global equal
    global equation
    global op
    global bracket

    if equal == 1:
        clear()
        equal = 0
        click(number)  # Concept of recursion.
    else:
        c = entry.get()
        entry.delete(0, END)
        entry.insert(0, c + number)
        if number == "^":
            equation += ","
        else:
            equation += number
    if bracket == 1 and equation[-1] in op:
        equation = equation.replace(f"{equation[-1]}", f"){equation[-1]}")
        bracket = 0


def equal_press():
    """Executes when Equal Button is pressed"""
    global equal
    global equation
    global bracket
    equal = 1
    if equation == "":
        ans.insert(0, "Nothing to calculate")
    else:
        ans.delete(0, END)
        # for automatic single bracket addition at last
        if bracket == 1:
            add_bracket(1)
            bracket = 0

        # For rounding-off some values.
        if "tan(math.radians(90))" in equation:
            equation = "1/0"
        if "sin(math.radians(90))" in equation:
            equation = equation.replace("math.sin(math.radians(90))", "round(math.sin(math.radians(90)))")
        if "sin(math.radians(0))" in equation:
            equation = equation.replace("math.sin(math.radians(0))", "round(math.sin(math.radians(0)))")
        if "cos(math.radians(90))" in equation:
            equation = equation.replace("math.cos(math.radians(90))", "round(math.cos(math.radians(90)))")
        if "cos(math.radians(0))" in equation:
            equation = equation.replace("math.cos(math.radians(0))", "round(math.cos(math.radians(0)))")
        if "math.degrees(math.asin(1))" in equation:
            equation = equation.replace("math.degrees(math.asin(1))", "round(math.degrees(math.asin(1)))")
        if "math.degrees(math.asin(0))" in equation:
            equation = equation.replace("math.degrees(math.asin(0))", "round(math.degrees(math.asin(0)))")
        if "math.degrees(math.acos(0))" in equation:
            equation = equation.replace("math.degrees(math.acos(0))", "round(math.degrees(math.acos(0)))")
        if "math.degrees(math.acos(1))" in equation:
            equation = equation.replace("math.degrees(math.acos(1))", "round(math.degrees(math.acos(1)))")
        if "math.degrees(math.atan(1))" in equation:
            equation = equation.replace("math.degrees(math.atan(1))", "round(math.degrees(math.atan(1)))")
        if "math.degrees(math.atan(0))" in equation:
            equation = equation.replace("math.degrees(math.atan(0))", "round(math.degrees(math.atan(0)))")
        if "math.cos(math.radians(round(math.degrees(math.asin(1)))))" in equation:
            equation = equation.replace("math.cos(math.radians(round(math.degrees(math.asin(1)))))", "round(math.cos(math.radians(round(math.degrees(math.asin(1))))))")
        if "math.tan(math.radians(round(math.degrees(math.asin(1)))))" in equation:
            equation = equation.replace("math.tan(math.radians(round(math.degrees(math.asin(1)))))", "1/0")
        if "math.tan(math.radians(math.degrees(math.acos(0.707))))" in equation:
            equation = equation.replace("math.tan(math.radians(math.degrees(math.acos(0.707))))", "round(math.tan(math.radians(math.degrees(math.acos(0.707)))))")
        if "math.tan(math.radians(math.degrees(math.asin(0.707))))" in equation:
            equation = equation.replace("math.tan(math.radians(math.degrees(math.asin(0.707))))", "round(math.tan(math.radians(math.degrees(math.asin(0.707)))))")

        # Exception Handling
        try:
            ans.insert(0, eval(equation))
        except SyntaxError as e:
            if "leading zeros" in str(e):
                ans.insert(0, "Please don't enter zeros before numbers(e.g. enter 9 instead of 09).")
            elif "was never closed" in str(e):
                ans.insert(0, "There are some unclosed brackets.")
            elif "invalid decimal" in str(e):
                ans.insert(0, "I think you've written the wrong equation !!!")
        except ZeroDivisionError:
            ans.insert(0, "Domain Error")
        except ValueError:
            ans.insert(0, "Domain Error")
        except TypeError:
            ans.insert(0, "Something is wrong!")
    # Just for keeping track of the 'equation' variable
    print(equation)


def clear():
    """All Clear (AC) Function"""
    ans.delete(0, END)
    entry.delete(0, END)
    global equation
    equation = ""


def close_bracket():
    """Closes Brackets"""
    global equation
    global tri
    # Condition for Trigonometric function only.
    if tri >= 1:
        s = ""
        for i in equation[-1::-1]:
            if i != "(":
                s = i + s
            else:
                break
        c = entry.get()
        entry.delete(0, END)
        entry.insert(0, c + ")")
        add_bracket(2)
        # Just for keeping track of the 'equation' variable
        print(equation)
        tri -= 1
    else:
        click(")")


def fact():
    """Factorial Function"""
    global equation
    c = entry.get()
    entry.delete(0, END)
    entry.insert(0, c + "!")
    equation += "!"
    s = ""
    for i in equation[-2::-1]:
        if i.isdigit():
            s = i + s
        else:
            break
    equation = equation.replace(f"{s}!", f"math.factorial({s})")


def sq_root():
    """Square root Function"""
    global equation
    global bracket
    global equal
    global sqr
    bracket = 1
    if equal == 1:
        clear()
        equal = 0
        sq_root()  # Concept of recursion.
    else:
        c = entry.get()
        entry.delete(0, END)
        entry.insert(0, c + "√")
        i = equation[-1::-1]
        if i.isdigit():
            equation += "*math.sqrt("
        else:
            equation += "math.sqrt("
    sqr = 1


def Power():
    """Base - Power Function"""
    global equation
    global bracket
    rev = equation[-1::-1]
    s = ""
    if equation[-11:] == "math.exp(1)":
        s = "math.exp(1)"
    else:
        for ch in rev:
            if ch not in op:
                s = ch + s  # Obtaining number as  's'
            else:
                break

    print(f"s is {s}")  # Checking the value of 's'
    internal_brackets = ""  # Keep trak of all brackets prior to 's'.

    if s == "math.exp(1)":
        equation = equation.replace(f"{s}", f"pow({s},")
    elif "(" in s:  # Checks whether a bracket is prior to 's'.
        while "(" in s:  # Until all the prior brackets are not removed.
            internal_brackets += "("
            s = s[1:]  # Removes single bracket prior to it.
        equation = equation.replace(f"{internal_brackets}{s}", f"{internal_brackets}pow({s},")

    else:
        equation = equation.replace(s, f"pow({s},")

    print(f"After change s is {s}")  # Checking the value of 's'
    c = entry.get()
    entry.delete(0, END)
    entry.insert(0, c + "^")
    bracket = 1


def trigono(fun):
    """Trigonometric Function"""
    global equation
    global tri
    global equal
    if equal == 1:
        clear()
        equal = 0
        trigono(fun)
    else:
        c = entry.get()
        entry.delete(0, END)
        entry.insert(0, c + fun)
        if fun == "sin(":
            equation += "math.sin(math.radians("
            # Just for keeping track of the 'equation' variable
            print(equation)
            tri += 1
        elif fun == "cos(":
            equation += "math.cos(math.radians("
            # Just for keeping track of the 'equation' variable
            print(equation)
            tri += 1
        elif fun == "tan(":
            equation += "math.tan(math.radians("
            # Just for keeping track of the 'equation' variable
            print(equation)
            tri += 1
        elif fun == "sin⁻¹(":
            equation += "math.degrees(math.asin("
            # Just for keeping track of the 'equation' variable
            print(equation)
            tri += 1
        elif fun == "cos⁻¹(":
            equation += "math.degrees(math.acos("
            # Just for keeping track of the 'equation' variable
            print(equation)
            tri += 1
        elif fun == "tan⁻¹(":
            equation += "math.degrees(math.atan("
            # Just for keeping track of the 'equation' variable
            print(equation)
            tri += 1


def add_bracket(num):
    """Just for adding brackets wherever required"""
    global equation
    if num == 1:
        equation += ")"
    if num == 2:
        equation += "))"


def cut():
    """Backspace Function"""
    global equation
    global equal
    global bracket  # For error handling in square-root cutting - Don't know how, but it works.
    s = entry.get()

    # Condition for Trigonometric Inverses open
    if s[-1] == "(" and not s[-3:-1].isalnum() and s[-4].isalpha():
        s = s[:-6]
        equation = equation[:-23]
        entry.delete(0, END)
        entry.insert(0, s)

    # Condition for Trigonometric function open
    elif s[-1] == "(" and s[-2].isalpha():
        s = s[:-4]
        equation = equation[:-22]
        entry.delete(0, END)
        entry.insert(0, s)

    # Condition for simple open bracket or operator
    elif s[-1] == "(" or s[-1] in op and not s[-3:-1] == "⁻¹" and not s[-2].isalpha():  # Ignoring inverse condition
        equation = equation[:-1]
        c = entry.get()
        entry.delete(0, END)
        entry.insert(0, c[:-1])

    # Condition for number
    elif s[-1].isdigit():
        equation = equation[:-1]
        s = s[:-1]
        entry.delete(0, END)
        entry.insert(0, s)

    # Condition for Factorial function condition
    elif s[-1] == "!":
        s = s[:-1]  # Remove factorial sign
        n = ""  # Variable for taking number before '^' symbol
        i = len(s) - 1
        c = s
        # While the character at index i is a digit
        while i >= 0 and s[i].isdigit():
            n = c[i] + n
            c = c[:i]
            i -= 1

        equation = equation.replace(f"math.factorial({n})", f"{n}")
        entry.delete(0, END)
        entry.insert(0, s)

    # Condition for cutting 'e'
    elif s[-1] == "e":
        s = s[:-1]
        equation = equation[:-11]
        entry.delete(0, END)
        entry.insert(0, s)

    # Condition for square-root sign "√"
    elif s[-1] == "√":
        s = s[:-1]
        try:
            if s[-1].isdigit():  # Raises an index error for some conditions
                equation = equation[:-11]
            else:
                equation = equation[:-10]
        except IndexError:
            equation = equation[:-10]
        entry.delete(0, END)
        entry.insert(0, s)
        bracket = 0

    # Condition when Power symbol "^"
    elif s[-1] == "^":
        print("Entered equation")  #
        s = s[:-1]
        print(f"initially {s=}")  #
        n = ""  # Variable for taking number before '^' symbol
        xi = s  # Acopy of s
        i = len(xi) - 1

        while i >= 0 and xi[i].isdigit():  # While the character at index i is a digit
            n = xi[i] + n
            xi = xi[:i]
            i -= 1
            print(f"{n=}\n{s=}")
            equation = equation.replace(f"pow({n},", f"{n}")
            entry.delete(0, END)
            entry.insert(0, s)
        bracket = 0  # Addition to remove extra bracket

    # Condition for deleting number after '^' sign
    elif s[-1].isdigit() and s[-2] == "^":
        print(f"initially {s = }")  #
        n = ""  # Variable for taking number before '^' symbol
        i = len(s) - 1

        # While the character at index i is a digit
        while i >= 0 and s[i].isdigit():
            n = s[i] + n
            s = s[:i]
            i -= 1
        print(f"{n=}\n{s=}")
        equation = equation[:-1]
        equation = equation.replace(f",{n}", f",")
        entry.delete(0, END)
        entry.insert(0, s)
        print(f"inserted {s=}")

    # Closed bracket condition
    elif s[-1] == ")":
        global sqr
        # Condition for deleting square-root closing bracket
        if sqr == 1:
            n = ""
            equation = equation[:-1]  # Remove closing bracket
            print(f"for sqr remove {equation = }")
            i = len(s) - 1
            # While the character at index i is a digit
            while i >= 0 and s[i].isdigit():
                n = s[i] + n
                s = s[:i]
                i -= 1
            sqr = 0
            equation = equation[:int(f"-{len(n)}")]  # Deletes character upto brackets
            print(f"{n=}\n{s=}\n{equation=}")
        elif tri != 0:
            equation = equation[:int(f"-{tri+1}")]
            c = entry.get()
            entry.delete(0, END)
            entry.insert(0, c[:-1])
        else:
            equation = equation[:-1]
            c = entry.get()
            entry.delete(0, END)
            entry.insert(0, c[:-1])


def log():
    global bracket
    global equation
    global equal
    if equal == 1:
        clear()
        entry.insert(0, "log(")
        equation += "math.log10("
        equal = 0
    else:
        c = entry.get()
        entry.delete(0, END)
        entry.insert(0, c + "log(")
        equation += "math.log10("


def ln():
    global bracket
    global equation
    global equal
    if equal == 1:
        clear()
        entry.insert(0, "ln(")
        equation += "math.log("
        equal = 0
    else:
        c = entry.get()
        entry.delete(0, END)
        entry.insert(0, c + "ln(")
        equation += "math.log("


def exp_press():
    global equation
    global bracket
    global equal
    # bracket = 1
    if equal == 1:
        clear()
        equal = 0
        exp_press()  # Concept of recursion.
    else:
        c = entry.get()
        entry.delete(0, END)
        entry.insert(0, c + "e")
        i = equation[-1::-1]
        if i.isdigit():
            equation += "*math.exp(1)"
        else:
            equation += "math.exp(1)"


# Initiate Window
win = Tk()
x = win.winfo_screenwidth()/2 - 150
y = win.winfo_screenheight()/2 - 100
win.geometry("608x405+350+20")
win.resizable(False, False)

# For Icon, it should be in '.ico' extension
win.iconbitmap("Calci_Logo_ico.ico")

# For title of the project
win.title("The Scientific Calculator")

# Creating text boxes for equation and it's answer.
entry = Entry(width=80, borderwidth=10, font=(None, 10))
ans = Entry(width=62, borderwidth=10, font=(None, 12))
trigo_text = StringVar()
trigo_text.set("Trigonometry\u25bc")
loga_text = StringVar()
loga_text.set("Logarithm\u25bc")
fact_text = StringVar()
fact_text.set("Power/Fact\u25bc")
radio_text = StringVar()
radio_text.set("1")  # Set Default as Normal Mode

# Colouring Button
st = ttk.Style()
st.configure("num.TButton", background="purple", foreground="purple", font=(None, 15))  # For numeric buttons
st.configure("eq.TButton", background="green", foreground="green", font=(None, 15))  # For equal button
st.configure("so.TButton", background="orange", font=(None, 15))
st.configure("clr.TButton", background="red", foreground="red", font=(None, 15))  # For AC button
st.configure("sco.TButton", background="yellow", font=(None, 15))
st.configure("rad.TRadiobutton", font=("Algerian", 13))  # For radio buttons

# Creating Radio Buttons
norm_mode = ttk.Radiobutton(text="Normal Mode", value="1", variable=radio_text, command=normal_on, style="rad.TRadiobutton")
sci_mode = ttk.Radiobutton(text="Scientific mode", value="2", variable=radio_text, command=scientific_on, style="rad.TRadiobutton")

# Creating Buttons
b_0 = ttk.Button(text="0", command=lambda: click("0"), style="num.TButton")
b_1 = ttk.Button(text="1", command=lambda: click("1"), style="num.TButton")
b_2 = ttk.Button(text="2", command=lambda: click("2"), style="num.TButton")
b_3 = ttk.Button(text="3", command=lambda: click("3"), style="num.TButton")
b_4 = ttk.Button(text="4", command=lambda: click("4"), style="num.TButton")
b_5 = ttk.Button(text="5", command=lambda: click("5"), style="num.TButton")
b_6 = ttk.Button(text="6", command=lambda: click("6"), style="num.TButton")
b_7 = ttk.Button(text="7", command=lambda: click("7"), style="num.TButton")
b_8 = ttk.Button(text="8", command=lambda: click("8"), style="num.TButton")
b_9 = ttk.Button(text="9", command=lambda: click("9"), style="num.TButton")

b_plus = ttk.Button(text="+", command=lambda: click("+"), style="so.TButton")
b_sub = ttk.Button(text="-", command=lambda: click("-"), style="so.TButton")
b_mul = ttk.Button(text="X", command=lambda: click("*"), style="so.TButton")
b_div = ttk.Button(text="/", command=lambda: click("/"), style="so.TButton")

b_fact = ttk.Button(text="x!", command=fact, style="sco.TButton")
b_open_bracket = ttk.Button(text="(", command=lambda: click("("), style="sco.TButton")
b_closed_bracket = ttk.Button(text=")", command=close_bracket, style="sco.TButton")
b_sin = ttk.Button(text="sin", command=lambda: trigono("sin("), style="sco.TButton")
b_cos = ttk.Button(text="cos", command=lambda: trigono("cos("), style="sco.TButton")
b_tan = ttk.Button(text="tan", command=lambda: trigono("tan("), style="sco.TButton")
b_pow = ttk.Button(text="^", command=Power, style="sco.TButton")
b_sqr = ttk.Button(text="√x", command=sq_root, style="sco.TButton")
b_deci_point = ttk.Button(text=".", command=lambda: click("."), style="sco.TButton")

b_equal = ttk.Button(text="=", command=equal_press, style="eq.TButton")
b_clear = ttk.Button(text="AC", command=clear, style="clr.TButton")
b_cut = ttk.Button(text="DEL", command=cut, style="sco.TButton")
b_log = ttk.Button(text="log", command=log, style="sco.TButton")
b_Ln = ttk.Button(text="ln", command=ln, style="sco.TButton")

b_sin_inv = ttk.Button(text=" sin⁻¹", command=lambda: trigono("sin⁻¹("), style="sco.TButton")
b_cos_inv = ttk.Button(text=" cos⁻¹", command=lambda: trigono("cos⁻¹("), style="sco.TButton")
b_tan_inv = ttk.Button(text=" tan⁻¹", command=lambda: trigono("tan⁻¹("), style="sco.TButton")

b_trigo = ttk.Button(textvariable=trigo_text, style="sco.TButton", command=TrigoButtonClick, width=25)
b_logarithm = ttk.Button(textvariable=loga_text, style="sco.TButton", command=LogarithmButtonClick)
b_power = ttk.Button(textvariable=fact_text, style="sco.TButton", command=FactorialClick)
b_exp = ttk.Button(text="e", style="sco.TButton", command=exp_press)

# Packing widgets position wise
entry.grid(row=0, columnspan=4, ipady=7)
ans.grid(row=1, columnspan=4, ipady=10)

norm_mode.grid(row=2, column=2)
sci_mode.grid(row=2, column=3)

b_open_bracket.grid(row=3, column=0, ipady=10, ipadx=10)
b_closed_bracket.grid(row=3, column=1, ipady=10, ipadx=10)
b_cut.grid(row=3, column=2, ipady=10, ipadx=10)
b_clear.grid(row=3, column=3, ipady=10, ipadx=10)

b_7.grid(row=4, column=0, ipady=10, ipadx=10)
b_8.grid(row=4, column=1, ipady=10, ipadx=10)
b_9.grid(row=4, column=2, ipady=10, ipadx=10)
b_plus.grid(row=4, column=3, ipady=10, ipadx=10)

b_4.grid(row=5, column=0, ipady=10, ipadx=10)
b_5.grid(row=5, column=1, ipady=10, ipadx=10)
b_6.grid(row=5, column=2, ipady=10, ipadx=10)
b_sub.grid(row=5, column=3, ipady=10, ipadx=10)

b_1.grid(row=6, column=0, ipady=10, ipadx=10)
b_2.grid(row=6, column=1, ipady=10, ipadx=10)
b_3.grid(row=6, column=2, ipady=10, ipadx=10)
b_mul.grid(row=6, column=3, ipady=10, ipadx=10)

b_deci_point.grid(row=7, column=0, ipady=10, ipadx=10)
b_0.grid(row=7, column=1, ipady=10, ipadx=10)
b_equal.grid(row=7, column=2, ipady=10, ipadx=10)
b_div.grid(row=7, column=3, ipady=10, ipadx=10)

win.mainloop()
