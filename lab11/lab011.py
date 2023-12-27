from tkinter import *
from tkinter import messagebox
import random
import string
import os

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        
        self.folder_path = os.getcwd() + "/passwords"
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

        self.login_label = Label(self.master, text="Login: ")
        self.login_label.pack()
        self.login_entry = Entry(self.master)
        self.login_entry.pack()

        self.platform_label = Label(self.master, text="Social Media Platform: ")
        self.platform_label.pack()
        self.platform_entry = Entry(self.master)
        self.platform_entry.pack()

        self.password_label = Label(self.master, text="Password: ")
        self.password_label.pack()
        self.password_entry = Entry(self.master, show="*")
        self.password_entry.pack()

        self.generate_button = Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.save_button = Button(self.master, text="Save Password", command=self.save_password)
        self.save_button.pack()

    def generate_password(self):
        letters = string.ascii_letters
        digits = string.digits
        symbols = string.punctuation

        password_length = random.randint(8, 12)
        password = ''.join(random.choice(letters + digits + symbols) for i in range(password_length))
        self.password_entry.delete(0, END)
        self.password_entry.insert(END, password)

    def save_password(self):
        login = self.login_entry.get()
        platform = self.platform_entry.get().capitalize()
        password = self.password_entry.get()

        if login and platform and password:
            filename = f"{self.folder_path}/{platform}.txt"
            with open(filename, "w") as file:
                file.write(f"Login: {login}\n")
                file.write(f"Password: {password}\n")
            messagebox.showinfo("Success", f"Password for {platform} saved successfully!")
        else:
            messagebox.showerror("Error", "Please enter a login, platform, and password.")

if __name__ == "__main__":
    root = Tk()
    app = PasswordManager(root)
    root.mainloop()
