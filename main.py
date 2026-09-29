"""
main.py

The calculator window (built with tkinter).
Run with:  python main.py
"""

import tkinter as tk

from calculator_logic import (
    CalculatorError,
    evaluate_expression,
    square,
    square_root,
)

VALID_KEYS = "0123456789+-*/().%"


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x520")
        self.root.resizable(False, False)

        self.build_display()
        self.build_buttons()
        self.root.bind("<Key>", self.on_key_press)

    # ---------- Building the window ----------

    def build_display(self):
        self.display = tk.Entry(
            self.root,
            font=("Arial", 24),
            justify="right",
            bd=10,
            relief=tk.RIDGE,
        )
        self.display.pack(padx=10, pady=20, fill="x")

    def build_buttons(self):
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        # (label, row, column, action)
        layout = [
            ("C", 0, 0, self.clear),
            ("DEL", 0, 1, self.delete_last),
            ("%", 0, 2, lambda: self.press("%")),
            ("÷", 0, 3, lambda: self.press("/")),
            ("7", 1, 0, lambda: self.press("7")),
            ("8", 1, 1, lambda: self.press("8")),
            ("9", 1, 2, lambda: self.press("9")),
            ("×", 1, 3, lambda: self.press("*")),
            ("4", 2, 0, lambda: self.press("4")),
            ("5", 2, 1, lambda: self.press("5")),
            ("6", 2, 2, lambda: self.press("6")),
            ("−", 2, 3, lambda: self.press("-")),
            ("1", 3, 0, lambda: self.press("1")),
            ("2", 3, 1, lambda: self.press("2")),
            ("3", 3, 2, lambda: self.press("3")),
            ("+", 3, 3, lambda: self.press("+")),
            ("0", 4, 0, lambda: self.press("0")),
            (".", 4, 1, lambda: self.press(".")),
            ("x²", 4, 2, self.show_square),
            ("√", 4, 3, self.show_square_root),
            ("(", 5, 0, lambda: self.press("(")),
            (")", 5, 1, lambda: self.press(")")),
            ("=", 5, 2, self.show_result),
            ("EXIT", 5, 3, self.root.destroy),
        ]

        for text, row, column, action in layout:
            tk.Button(
                self.button_frame,
                text=text,
                font=("Arial", 16),
                width=5,
                height=2,
                command=action,
            ).grid(row=row, column=column, padx=4, pady=4)

    # ---------- Display helpers ----------

    def set_display(self, text):
        self.display.delete(0, tk.END)
        self.display.insert(0, str(text))

    def show_error_free(self):
        """If an error message is showing, clear it before typing."""
        current = self.display.get()
        if current in ("Cannot divide by zero", "Invalid input"):
            self.clear()

    # ---------- Button actions ----------

    def press(self, value):
        self.show_error_free()
        self.display.insert(tk.END, value)

    def clear(self):
        self.display.delete(0, tk.END)

    def delete_last(self):
        self.set_display(self.display.get()[:-1])

    def run_calculation(self, calculation):
        """Run a calculation on the display text and show the result or an error."""
        try:
            self.set_display(calculation(self.display.get()))
        except ZeroDivisionError:
            self.set_display("Cannot divide by zero")
        except CalculatorError as error:
            self.set_display(error)

    def show_result(self):
        self.run_calculation(evaluate_expression)

    def show_square(self):
        self.run_calculation(square)

    def show_square_root(self):
        self.run_calculation(square_root)

    # ---------- Keyboard support ----------

    def on_key_press(self, event):
        if event.char and event.char in VALID_KEYS:
            self.press(event.char)
        elif event.keysym == "Return":
            self.show_result()
        elif event.keysym == "BackSpace":
            self.delete_last()
        elif event.keysym == "Escape":
            self.clear()
        return "break"  # stops the Entry adding the key a second time


if __name__ == "__main__":
    window = tk.Tk()
    CalculatorApp(window)
    window.mainloop()
