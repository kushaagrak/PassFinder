from PassfinderLogic import accountmanager
import customtkinter as ctk
from tkinter import messagebox
from UserInterface.UI import PassFinder
from UserInterface import MainUI, CreateAccountUI
from PIL import Image

def loginUI(app: PassFinder):
    frame = ctk.CTkFrame(master=app.root, corner_radius=15)
    frame.pack(pady=40, padx=60, fill="both", expand=True)
    
    label = ctk.CTkLabel(master=frame, text="Login", font=("Arial", 24)) # text at the top
    label.pack(pady=12, padx=10)
    
    UsernameEntry = ctk.CTkEntry(master=frame, placeholder_text="Username") # username text box
    UsernameEntry.pack(pady=12, padx=10)
    
    PasswordEntry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*") # password textbox
    PasswordEntry.pack(pady=12, padx=10)

    def login():
        username = UsernameEntry.get()
        password = PasswordEntry.get()
        is_logged_in = app.account_manager.login(username, password) # verify creditials in account manager python file
        if is_logged_in:
            app.destroy_frames()
            MainUI.mainUI(app)
        else: # popup saying invalid details
            messagebox.showerror("Popup", "Invalid username or password. Please try again.") # intentionally vague for security purposes

    button = ctk.CTkButton(master=frame, text="Login", command=login)
    button.pack(pady=12, padx=10)

    canvas = ctk.CTkCanvas(master=frame, height=1)
    canvas.pack(fill='x', padx=10, pady=10)
    canvas.create_line(0, 1, frame.winfo_width() * 0.5, 1, fill='black')

    
    def create_account():
        app.destroy_frames()
        CreateAccountUI.createAccountUI(app)


    button = ctk.CTkButton(master=frame, text="Create Account", command=create_account)
    button.pack(pady=12, padx=10)