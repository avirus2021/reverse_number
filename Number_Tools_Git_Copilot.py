import tkinter as tk
from tkinter import messagebox

## Number_Tools ##

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        digit = n % 10
        reversed_num = (reversed_num * 10) + digit
        n //= 10
    return reversed_num

def is_palindrome(n):
    return n == reverse_number(n)

def check_palindrome():
    try:
        Z = int(entry.get())
        reversed_num = reverse_number(Z)
        
        if is_palindrome(Z):
            messagebox.showinfo("Result", f"{Z} is a palindrome!\nReversed: {reversed_num}")
        else:
            messagebox.showinfo("Result", f"{Z} is not a palindrome.\nReversed: {reversed_num}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Create main window
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("300x150")

# Label
label = tk.Label(root, text="Enter a number:", font=("Arial", 12))
label.pack(pady=10)

# Entry field
entry = tk.Entry(root, font=("Arial", 12), width=20)
entry.pack(pady=5)

# Check button
button = tk.Button(root, text="Check Palindrome", command=check_palindrome, bg="lightblue", font=("Arial", 10))
button.pack(pady=10)

# Run the app
root.mainloop()