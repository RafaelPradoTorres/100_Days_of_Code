from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    pword_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    site = website_entry.get()
    email = email_entry.get()
    pword = pword_entry.get()

    if site == "" or email == "" or pword == "":
        messagebox.showinfo(title="Oops", message="Empty field detected")

    else:
        is_ok = messagebox.askokcancel(title=site, message=f"You've entered: \nEmail: {email} \nPassword: {pword} "
                                                            f"\nDo you really want to save?")

        if is_ok:
            with open('data.txt', 'a') as file:
                file.write(f"{site} | {email} | {pword}\n")

                website_entry.delete(0, END)
                pword_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.configure(background="white", padx=20, pady=20)
window.title("Gosto de gostar")

canva = Canvas(background="white", width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canva.create_image(100, 100, image = logo_img)
canva.grid(row=0, column=1)

# --------------------------------------------------
website_label = Label(text="Website: ", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=40)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
# --------------------------------------------------
email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "rafael@gmail.com")
# --------------------------------------------------
pword_label = Label(text="Password: ", bg="white")
pword_label.grid(column=0, row=3)

pword_entry = Entry(width=22)
pword_entry.grid(column=1, row=3)

gen_pword_button = Button(text="Generate Password", command=generate_password)
gen_pword_button.grid(column=2, row=3)
# ---------------------------------------------------
add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()