import tkinter as tk
from tkinter import messagebox

class PasswordManager:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")

        self.login_label = tk.Label(self.master, text="Login: ")
        self.login_label.pack()
        self.login_entry = tk.Entry(self.master)
        self.login_entry.pack()

        self.password_label = tk.Label(self.master, text="Password: ")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()

        self.save_button = tk.Button(self.master, text="Save Password", command=self.save_password)
        self.save_button.pack()

    def save_password(self):
        login = self.login_entry.get()
        password = self.password_entry.get()

        if login and password:
            # Save the login and password to a file or database
            messagebox.showinfo("Success", "Password saved successfully!")
        else:
            messagebox.showerror("Error", "Please enter a login and password.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManager(root)
    root.mainloop()