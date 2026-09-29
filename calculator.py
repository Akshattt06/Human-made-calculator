import tkinter as tk
import math


# -----------------------------
# Calculator Functions
# -----------------------------

def press(value):
    """Add a number or operator to the display."""
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(value))


def clear():
    """Clear the calculator display."""
    display.delete(0, tk.END)


def delete():
    """Delete the last character."""
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])


def calculate():
    """Calculate the mathematical expression."""
    expression = display.get()

    try:
        # Allow only calculator-related characters
        allowed = "0123456789+-*/().% "
        if any(char not in allowed for char in expression):
            raise ValueError

        # Percentage conversion
        expression = expression.replace("%", "/100")

        result = eval(expression, {"__builtins__": None}, {})

        # Display integer without .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by zero")

    except:
        display.delete(0, tk.END)
        display.insert(0, "Invalid input")


def square_root():
    """Calculate square root."""
    try:
        number = float(display.get())

        if number < 0:
            raise ValueError

        result = math.sqrt(number)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Invalid input")


def square():
    """Calculate square of a number."""
    try:
        number = float(display.get())
        result = number ** 2

        if result.is_integer():
            result = int(result)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except:
        display.delete(0, tk.END)
        display.insert(0, "Invalid input")


# -----------------------------
# Main Window
# -----------------------------

root = tk.Tk()
root.title("Human Made Calculator")
root.geometry("360x520")
root.resizable(False, False)

# -----------------------------
# Display
# -----------------------------

display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10,
    relief=tk.RIDGE
)

display.pack(
    padx=10,
    pady=20,
    fill="x"
)

# -----------------------------
# Button Frame
# -----------------------------

button_frame = tk.Frame(root)
button_frame.pack()

# -----------------------------
# Button Creation Function
# -----------------------------

def create_button(text, row, column, command):
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 16),
        width=5,
        height=2,
        command=command
    )

    button.grid(
        row=row,
        column=column,
        padx=4,
        pady=4
    )


# -----------------------------
# Calculator Buttons
# -----------------------------

# Row 0
create_button("C", 0, 0, clear)
create_button("DEL", 0, 1, delete)
create_button("%", 0, 2, lambda: press("%"))
create_button("÷", 0, 3, lambda: press("/"))

# Row 1
create_button("7", 1, 0, lambda: press("7"))
create_button("8", 1, 1, lambda: press("8"))
create_button("9", 1, 2, lambda: press("9"))
create_button("×", 1, 3, lambda: press("*"))

# Row 2
create_button("4", 2, 0, lambda: press("4"))
create_button("5", 2, 1, lambda: press("5"))
create_button("6", 2, 2, lambda: press("6"))
create_button("−", 2, 3, lambda: press("-"))

# Row 3
create_button("1", 3, 0, lambda: press("1"))
create_button("2", 3, 1, lambda: press("2"))
create_button("3", 3, 2, lambda: press("3"))
create_button("+", 3, 3, lambda: press("+"))

# Row 4
create_button("0", 4, 0, lambda: press("0"))
create_button(".", 4, 1, lambda: press("."))
create_button("x²", 4, 2, square)
create_button("√", 4, 3, square_root)

# Row 5
create_button("(", 5, 0, lambda: press("("))
create_button(")", 5, 1, lambda: press(")"))
create_button("=", 5, 2, calculate)

# Exit button
exit_button = tk.Button(
    button_frame,
    text="EXIT",
    font=("Arial", 16),
    width=5,
    height=2,
    command=root.destroy
)

exit_button.grid(
    row=5,
    column=3,
    padx=4,
    pady=4
)


# -----------------------------
# Keyboard Support
# -----------------------------

def keyboard_input(event):
    key = event.char

    if key in "0123456789+-*/().%":
        press(key)

    elif event.keysym == "Return":
        calculate()

    elif event.keysym == "BackSpace":
        delete()

    elif event.keysym == "Escape":
        clear()


root.bind("<Key>", keyboard_input)

# -----------------------------
# Start Calculator
# -----------------------------

root.mainloop()
