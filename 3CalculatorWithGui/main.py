# Import necessary libraries
import math
import tkinter as tk
from tkinter import messagebox

# Define functions for various mathematical operations


def add(x, y):
    """
    Perform addition operation.
    """
    return x + y


def subtract(x, y):
    """
    Perform subtraction operation.
    """
    return x - y


def multiply(x, y):
    """
    Perform multiplication operation.
    """
    return x * y


def divide(x, y):
    """
    Perform division operation.
    """
    # Check for division by zero
    if y == 0:
        return "Cannot divide by zero"
    return x / y


def find_hcf(x, y):
    """
    Calculate the Highest Common Factor (HCF) of two numbers.
    """
    # Calculate the greatest common divisor (HCF/GCD) using math.gcd
    return math.gcd(x, y)


def find_lcm(x, y):
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    """
    # Calculate the least common multiple (LCM) using the product and GCD
    return (x * y) // math.gcd(x, y)


def find_power(x, y):
    """
    Calculate x raised to the power of y.
    """
    return x ** y

# Define a function to perform calculations based on user input


def calculate():
    """
    Perform the selected mathematical operation based on user input.
    """
    choice = operation_var.get()  # Get the selected operation
    num1 = float(entry_num1.get())  # Get the first number from the user
    num2 = float(entry_num2.get())  # Get the second number from the user

    if choice == '1':
        result = add(num1, num2)
    elif choice == '2':
        result = subtract(num1, num2)
    elif choice == '3':
        result = multiply(num1, num2)
    elif choice == '4':
        result = divide(num1, num2)
    elif choice == '5':
        result = find_hcf(int(num1), int(num2))
    elif choice == '6':
        result = find_lcm(int(num1), int(num2))
    elif choice == '7':
        result = find_power(num1, num2)
    else:
        result = "Invalid choice"

    # Display the result on the GUI
    result_label.config(text="Result: " + str(result))

# Define a function to clear input fields and reset the result label


def clear_fields():
    """
    Clear the input fields and reset the result label.
    """
    entry_num1.delete(0, tk.END)  # Clear the first number entry field
    entry_num2.delete(0, tk.END)  # Clear the second number entry field
    result_label.config(text="Result: ")  # Reset the result label


# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create a label for operation selection
operation_label = tk.Label(window, text="Select operation:")
operation_label.pack()

# Create a variable to hold the selected operation (initialized with '1')
operation_var = tk.StringVar()
operation_var.set('1')

# Create radio buttons for operation selection
operation_radio_buttons = [
    ("Addition", '1'),
    ("Subtraction", '2'),
    ("Multiplication", '3'),
    ("Division", '4'),
    ("HCF (GCD)", '5'),
    ("LCM", '6'),
    ("Power", '7')
]

# Create and display the radio buttons for each operation
for text, val in operation_radio_buttons:
    operation_radio_button = tk.Radiobutton(
        window, text=text, variable=operation_var, value=val)
    operation_radio_button.pack()

# Create entry fields for number input
entry_num1 = tk.Entry(window)
entry_num1.pack()
entry_num2 = tk.Entry(window)
entry_num2.pack()

# Create a button to calculate the result, with the 'calculate' function as the callback
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create a label to display the result (initialized as "Result: ")
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Create a button to clear input fields, with the 'clear_fields' function as the callback
clear_button = tk.Button(window, text="Clear", command=clear_fields)
clear_button.pack()

# Run the tkinter main loop
window.mainloop()
