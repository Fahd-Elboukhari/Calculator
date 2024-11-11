import tkinter as tk
import math

# Create the main application window
root = tk.Tk()
root.title("Calculator")
root.geometry("500x600")

# StringVar to store and display input
input_text = tk.StringVar()

# Function to update the display when buttons are pressed
def click(button_text):
    current = input_text.get()
    input_text.set(current + str(button_text))

# Function to evaluate the expression in the display
def calculate():
    try:
        result = eval(input_text.get())
        input_text.set(result)
    except:
        input_text.set("Error")

# Function to clear the display
def clear():
    input_text.set("")

# Function for advanced operations
def sqrt():
    try:
        result = math.sqrt(float(input_text.get()))
        input_text.set(result)
    except:
        input_text.set("Error")

def square():
    try:
        result = float(input_text.get()) ** 2
        input_text.set(result)
    except:
        input_text.set("Error")

def inverse():
    try:
        result = 1 / float(input_text.get())
        input_text.set(result)
    except:
        input_text.set("Error")

# Function for trigonometric operations
def sin():
    try:
        result = math.sin(math.radians(float(input_text.get())))
        input_text.set(result)
    except:
        input_text.set("Error")

def cos():
    try:
        result = math.cos(math.radians(float(input_text.get())))
        input_text.set(result)
    except:
        input_text.set("Error")

def tan():
    try:
        result = math.tan(math.radians(float(input_text.get())))
        input_text.set(result)
    except:
        input_text.set("Error")

# Creating the display entry widget
display = tk.Entry(root, font=("Arial", 24), textvariable=input_text, borderwidth=5, relief="sunken")
display.grid(row=0, column=0, columnspan=5, pady=20, padx=10, sticky="we")

# Define button layout and functionality
button_config = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("sqrt", 1, 4),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("x^2", 2, 4),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("1/x", 3, 4),
    ("0", 4, 0), (".", 4, 1), ("%", 4, 2), ("+", 4, 3), ("=", 4, 4),
    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("C", 5, 3)
]

# Create buttons
for (text, row, col) in button_config:
    if text.isdigit() or text == ".":
        action = lambda x=text: click(x)
    elif text == "=":
        action = calculate
    elif text == "C":
        action = clear
    elif text == "sqrt":
        action = sqrt
    elif text == "x^2":
        action = square
    elif text == "1/x":
        action = inverse
    elif text == "sin":
        action = sin
    elif text == "cos":
        action = cos
    elif text == "tan":
        action = tan
    elif text == "%":
        action = lambda: click("/100")
    else:
        action = lambda x=text: click(x)

    # Creating and placing each button
    button = tk.Button(root, text=text, font=("Arial", 18), command=action, width=5, height=2)
    button.grid(row=row, column=col, padx=5, pady=5)

# Run the application loop
root.mainloop()
