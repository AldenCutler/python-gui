import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")   # available themes: dark, light, system, green, blue
root = customtkinter.CTk()
root.geometry("1000x700")
root.title("App")

logins = {"hello": "world", "test": "1234", "user": "pass"}

# Very crude and simple login system, I might implement a better one in the future. Currently, it only checks if the username and password are in the dictionary and if they are,
# it simply prints "Login successful!" and breaks out of the loop. If the username and password are not in the dictionary, it does nothing.
def login():                
    for login in logins:
        if login_frame.entry1.get() == login and login_frame.entry2.get() == logins[login]:
            print("Login successful!")
            
            # Clear the window
            for widget in root.winfo_children():
                widget.destroy()
                
            break
    else:
        print("Login failed!")



# Create the login frame
class LoginFrame():
    
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

    # Remember me checkbox (doesn't do anything yet)
    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember me")
    checkbox.pack(pady=12, padx=10)    

    # If the user presses the enter key, it will call the login function
    root.bind("<Return>", lambda event: login())



login_frame = LoginFrame()
root.mainloop()