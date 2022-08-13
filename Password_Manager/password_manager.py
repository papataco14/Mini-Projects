from tkinter import *
from tkinter import messagebox
import random
import string

# randomly generate password using symbols and letters
def password_generator():

    all_characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")
    random.shuffle(all_characters)

    password = []
    for i in range(15):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    rand_password = "".join(password)
    password_entry.insert(0, rand_password)

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    # if nothing is entered
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="got error", message="don't leave any fields blank")
    else:
        # confirmation message
        confem = messagebox.askokcancel(
            title="Confirm?",
            message=f"Confem the details below are ok?"
            f"\n{website}\n{email}\n{password}",
        )

        if confem:
            with open("data.txt", "a") as file:
                data = file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# creating widget design
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file= "logo.png")  
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "") # insert email here to autofill when running program

password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

generate_password_button = Button(text="Generate Password", command=password_generator)
generate_password_button.grid(row=3, column=2, sticky="EW")
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
