import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    pass            # TODO: Implement login functionality


# Create the frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Title
label = customtkinter.CTkLabel(master=frame, text="Login System")
label.pack(pady=12, padx=10)

# Username and password
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")   # Placeholder text for username
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")   # Placeholder text for password
entry2.pack(pady=12, padx=10)

# Login button
button = customtkinter.CTkButton(master=frame, text="Login", command=login)  
button.pack(pady=12, padx=10)

# Remember me checkbox
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
checkbox.pack(pady=12, padx=10)

root.mainloop()