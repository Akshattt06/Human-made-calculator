# 🧮 Human Made Calculator

## 1. About the Project

This is a simple calculator project made using **Python**.

I made this project as a student to understand how Python can be used to create a simple **Graphical User Interface (GUI)**.

The calculator looks like a normal calculator and can be used to perform basic mathematical calculations.

---

## 2. What I Used

For making this project, I used:

- **Python**
- **Tkinter** – to create the calculator window and buttons
- **Math module** – to calculate square roots

I did not use any external library, so there is no complicated installation required.

---

## 3. What Can This Calculator Do?

The calculator can perform:

- Addition `+`
- Subtraction `-`
- Multiplication `×`
- Division `÷`
- Percentage `%`
- Square `x²`
- Square root `√`
- Decimal calculations
- Brackets `( )`
- Clear `C`
- Delete `DEL`
- Exit the calculator

It also supports using the **keyboard** for entering numbers and operators.

---

## 4. Requirements

Before running the project, make sure Python is installed on your computer.

You can check Python by opening Command Prompt and typing:

```bash
python --version
```

Tkinter usually comes with Python, so no separate installation is needed.

---

## 5. How to Run the Project

### Step 1
Download or copy the project file.

The main file is:

```text
calculator.py
```

### Step 2
Open the folder where `calculator.py` is saved.

### Step 3
Open Command Prompt or Terminal in that folder.

### Step 4
Run:

```bash
python calculator.py
```

### Step 5
The calculator window will open.

---

## 6. How to Use It

For example, to calculate:

```text
10 + 20
```

Press:

```text
1 → 0 → + → 2 → 0 → =
```

The answer will be:

```text
30
```

### Square

Enter `5` and press `x²`.

The answer will be:

```text
25
```

### Square Root

Enter `25` and press `√`.

The answer will be:

```text
5
```

---

## 7. Main Functions

### `press()`
Adds the number or operator pressed to the calculator display.

### `clear()`
Removes everything from the calculator display.

### `delete()`
Removes the last character from the display.

### `calculate()`
Performs the calculation when `=` is pressed and handles simple errors.

### `square_root()`
Calculates the square root of a number.

### `square()`
Calculates the square of a number.

---

## 8. Calculator Interface

The project creates a window using Tkinter.

The window contains:

- Display box
- Number buttons
- Mathematical operators
- Clear button
- Delete button
- Square button
- Square root button
- Equal button
- Exit button

---

## 9. Keyboard Support

The calculator also supports keyboard input.

For example:

- Number keys → enter numbers
- `+`, `-`, `*`, `/` → mathematical operations
- `Enter` → calculate
- `Backspace` → delete
- `Escape` → clear

---

## 10. Error Handling

The calculator shows simple messages when something goes wrong.

### Dividing by zero

```text
Cannot divide by zero
```

### Invalid calculation

```text
Invalid input
```

---

## 11. Project Structure

```text
Human-Made-Calculator/
│
├── calculator.py
│
└── README.md
```

### `calculator.py`
This is the main Python program containing the calculator code.

### `README.md`
This file explains what the project is and how to run it.

---

## 12. What I Learned

While making this project, I learned:

- Basic Python programming
- How to create functions
- How buttons work in Python
- How to use Tkinter
- How to create a GUI
- How to take user input
- How to perform mathematical calculations
- Basic error handling
- How keyboard events work
- How to organize a small Python project

---

## 13. Future Improvements

In the future, I can improve this project by adding:

- A better calculator design
- Scientific calculator functions
- Calculation history
- Dark mode
- More keyboard shortcuts
- Memory buttons such as `M+`, `M-`, and `MR`
- Better error messages

---

## 14. Conclusion

This is a simple calculator project made using Python.

The main purpose of this project was to understand the basics of **Python GUI programming**.

Even though it is a small project, it helped me understand how functions, buttons, user input, calculations, and graphical interfaces work together.

I can improve this project further as I learn more Python.

---

## 15. Author

**Student Project**

Made using:

**Python + Tkinter**

**Level:** Beginner
