from tkinter import *
import random
import string

def update_characterlist():
    characterlist = ""
    if Capitalval.get():
        characterlist += string.ascii_uppercase
    if Smallval.get():
        characterlist += string.ascii_lowercase
    if Numberval.get():
        characterlist += string.digits
    if Symbolval.get():
        characterlist += string.punctuation
    return characterlist

def generate_password():
    characterlist = update_characterlist()
    length = lengthval.get()  # Get the password length from entry
    password = []
    if characterlist:  # Ensure there's a character to choose from
        for i in range(length):
            password.append(random.choice(characterlist))
        result_label.config(text="Generated Password: " + "".join(password))
    else:
        result_label.config(text="Please select at least one character type!")

root = Tk()
root.title("Random Password Generator")
root.geometry("455x455")

# Create and set variables for password options
lengthval = IntVar()  # Use IntVar for the length of the password
Capitalval = BooleanVar()
Smallval = BooleanVar()
Numberval = BooleanVar()
Symbolval = BooleanVar()

Label(root, text="Password Length").grid(row=0, column=1)
lengthentry = Entry(root, textvariable=lengthval)
lengthentry.grid(row=0, column=2)

Label(root, text="Select conditions for your password").grid(row=1, column=1)
Capital = Checkbutton(root, text="Capital Alphabet", variable=Capitalval)
Capital.grid(row=2, column=1)
Small = Checkbutton(root, text="Small Alphabet", variable=Smallval)
Small.grid(row=3, column=1)
Number = Checkbutton(root, text="Numbers", variable=Numberval)
Number.grid(row=4, column=1)
Symbol = Checkbutton(root, text="Symbols", variable=Symbolval)
Symbol.grid(row=5, column=1)

Button(root, text="Generate Password", command=generate_password).grid(row=6, column=2)

# Label to show the generated password
result_label = Label(root, text="", font="comicsansns 10", justify=LEFT)
result_label.grid(row=7, column=0, columnspan=3, padx=10, pady=20, sticky=W)

root.mainloop()

