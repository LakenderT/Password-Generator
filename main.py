from tkinter import *
import secrets
import string
import pyperclip

def generate_password():
    num_characters = int(entry2.get())
    include_letter = case_cochee1.get()
    include_digit = case_cochee2.get()
    include_punctuation = case_cochee3.get()

    password_chars = (
        string.ascii_letters if include_letter else '',
        string.digits if include_digit else '',
        string.punctuation if include_punctuation else ''
    )

    password_alphabet = ''.join(password_chars)
    password = ''.join(secrets.choice(password_alphabet) for _ in range(num_characters))
    
    entry.delete(0, END)
    entry.insert(0, password)
    
    # Enable the "Copy to Clipboard" button and reset its color
    copy_button.config(state=NORMAL, bg='#2e83ef')

    # Copy the generated password to the clipboard
    pyperclip.copy(password)

def copy_to_clipboard():
    # Copy the generated password to the clipboard
    password = entry.get()
    pyperclip.copy(password)

    # Change the color of the "Copy to Clipboard" button to indicate the copy action
    copy_button.config(bg='#4CAF50')
    copy_button.after(1000, lambda: copy_button.config(bg='#2e83ef'))

fenetre = Tk()
fenetre.title("Password generator")
fenetre.geometry('900x600')
fenetre.minsize(700, 300)
fenetre.config(background='#f2f2f2')

frame = Frame(fenetre, bg='#f2f2f2')

# Title
label_title = Label(frame, text='1. Enter the number of characters you want.', font=("Arial", 20), bg='#f2f2f2', fg='#000000')
label_title.pack()

# Entry
entry2 = Entry(frame, font=("Arial", 25), bg='#ececec', fg='#000000')
entry2.pack(fill=X)

# Checkbuttons
case_cochee1 = IntVar()
case = Checkbutton(frame, text="Letter", variable=case_cochee1, font=("Arial", 15), onvalue=1, offvalue=0)
case.pack()

case_cochee2 = IntVar()
case1 = Checkbutton(frame, text="Digits", variable=case_cochee2, font=("Arial", 15), onvalue=1, offvalue=0)
case1.pack()

case_cochee3 = IntVar()
case2 = Checkbutton(frame, text="Punctuation", variable=case_cochee3, font=("Arial", 15), onvalue=1, offvalue=0)
case2.pack()

# Button to Generate Password
generate_button = Button(frame, text="2. Generate password", font=("Arial", 20), bg='#2e83ef', fg='#000000', command=generate_password)
generate_button.pack(fill=X)

# Result Entry
entry = Entry(frame, font=("Arial", 25), bg='#a7a7a7', fg='#000000')
entry.pack(fill=X)

# Button to Copy to Clipboard
copy_button = Button(frame, text="Copy to Clipboard", font=("Arial", 20), bg='#2e83ef', fg='#000000', state=DISABLED, command=copy_to_clipboard)
copy_button.pack(fill=X)

frame.pack(expand=YES)
fenetre.mainloop()
