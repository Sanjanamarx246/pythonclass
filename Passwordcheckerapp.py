import customtkinter as ctk
def enter_clicked():
    print("enter clicked")
    name=namEntry.get()
    Password = PasswordEntry.get()
    print(name)
    print(Password)
    infolabel.configure(text=name)
    strList = [name, Address]
    info='\n'.join(strList)
    infolabel.configure(text=info)


app = ctk.CTk()
app.geometry("500x500")
app.title("Password Checker")

nameLabel = ctk.CTkLabel(app, text="Name: ")
nameLabel.grid(row=0, column=0)


namEntry = ctk.CTkEntry(app, placeholder_text="Enter your name")
namEntry.grid(row=0, column=1)


PasswordLabel = ctk.CTkLabel(app, text="password: ")
PasswordLabel.grid(row=1, column=0)

PasswordEntry = ctk.CTkEntry(app, placeholder_text="Enter Password")
PasswordEntry.grid(row=1, column=1)

enterbutton = ctk.CTkButton(app, text="Enter", command= enter_clicked)
enterbutton.grid(row=2, column=1)

infolabel=ctk.CTkLabel(app, text=" ")
infolabel.grid(row=4, column=1)

app.mainloop()
