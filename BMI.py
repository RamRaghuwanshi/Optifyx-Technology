import tkinter as tk
from tkinter import messagebox as tsmg

def calculation():
    try:
        a = float(Height_entry.get())
        b = int(Weight_entry.get())
        result = b / (a * a)

        if result < 18.5:
            category = "Underweight"
        elif 18.5 <= result < 25:
            category = "Normal"
        elif 25 <= result < 30:
            category = "Overweight"
        else:
            category = "Obesity"

        tsmg.showinfo("Your Result", category)
        
    except ValueError:
        tsmg.showwarning("Input Error", "Please enter valid numbers for height and weight.")

def Bmi():
    root.title('BMI Calculator')
    root.geometry('400x400')
    
    tk.Label(root, text="Body Mass Index Calculator").grid(row=0, column=1)

    tk.Label(root, text="Height (m)").grid(row=1, column=0)
    tk.Label(root, text="Weight (kg)").grid(row=2, column=0)

    global Height_entry, Weight_entry
    Height_entry = tk.Entry(root)
    Height_entry.grid(row=1, column=1)

    Weight_entry = tk.Entry(root)
    Weight_entry.grid(row=2, column=1)

    Submit = tk.Button(root, text="Submit", command=calculation)
    Submit.grid(row=3, column=1)

    return_button = tk.Button(root, text="Return to Main", command=root.quit)
    return_button.grid(row=4, column=1)

root = tk.Tk()
Bmi()

root.mainloop()
