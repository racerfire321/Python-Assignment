import tkinter as tk
from tkinter import ttk, Entry, StringVar, Button, Checkbutton
from tkinter import messagebox
from tkcalendar import DateEntry
from dbms.userdb import UserDatabase


class RegistrationForm:
    def __init__(self, root):
        self.root = root



        # Create a main frame
        self.main_frame = tk.Frame(root, background="#E0F8E0")
        self.main_frame.pack(expand=True, fill='both')

        self.header = tk.Label(self.main_frame, text="Registration Form",  font=("bold", 40),foreground="red", background="#E0F8E0")
        self.header.place(x=480, y=50)           

        self.full_name_label = tk.Label(self.main_frame, text="Full Name", width=20, font=("bold", 15), background="#E0F8E0")
        self.full_name_label.place(x=450, y=170)
        self.entry_full_name = Entry(self.main_frame, width=20, font=("bold", 15))
        self.entry_full_name.place(x=650, y=170)

        self.dob_label = tk.Label(self.main_frame, text="Date of Birth", width=20, font=("bold", 15), background="#E0F8E0")
        self.dob_label.place(x=450, y=240)
        self.entry_dob = DateEntry(self.main_frame, width=20, font=("bold", 15))
        self.entry_dob.place(x=650, y=240)

        self.phoneNumber_label = tk.Label(self.main_frame, text="Phone Number", width=20, font=("bold", 15), background="#E0F8E0")
        self.phoneNumber_label.place(x=450, y=310)
        self.entry_phone_number = Entry(self.main_frame, width=20, font=("bold", 15))
        self.entry_phone_number.place(x=650, y=310)

        self.email_label = tk.Label(self.main_frame, text="Email", width=20, font=("bold", 15), background="#E0F8E0")
        self.email_label.place(x=450, y=380)
        self.entry_email = Entry(self.main_frame, width=20, font=("bold", 15))
        self.entry_email.place(x=650, y=380)

        self.gender_label = tk.Label(self.main_frame, text="Gender", width=20, font=("bold", 15), background="#E0F8E0")
        self.gender_label.place(x=450, y=450)
        self.var_gender = StringVar()
        self.R1 = ttk.Radiobutton(self.main_frame, text="Male", variable=self.var_gender, value="Male", style="TRadiobutton")
        self.R1.place(x=650, y=450)
        self.R2 = ttk.Radiobutton(self.main_frame, text="Female", variable=self.var_gender, value="Female", style="TRadiobutton")
        self.R2.place(x=720, y=450)

        self.user_type_label = tk.Label(self.main_frame, text="Type", width=20, font=("bold", 15), background="#E0F8E0")
        self.user_type_label.place(x=450, y=520)
        self.user_types = ["Customer", "Driver"]
        self.var_user_type = StringVar()
        self.user_type_combobox = ttk.Combobox(self.main_frame, textvariable=self.var_user_type, values=self.user_types, state="readonly", font=("bold", 12))
        self.user_type_combobox.place(x=650, y=520)

        self.license_label = tk.Label(self.main_frame, text="License Number", width=20, font=("bold", 15), background="#E0F8E0")
        self.entry_license = Entry(self.main_frame, width=20, font=("bold", 15))

        self.vehicleNo_label = tk.Label(self.main_frame, text="Vehicle Number", width=20, font=("bold", 15), background="#E0F8E0")
        self.entry_vehicleNo = Entry(self.main_frame, width=20, font=("bold", 15))

        self.password_label = tk.Label(self.main_frame, text="Password:", width=20, font=("bold", 15),background="#E0F8E0")
        self.password_label.place(x=450, y=590)

        self.password_entry = Entry(self.main_frame, show="*", width=20, font=("bold", 15))
        self.password_entry.place(x=650, y=590)

        self.toggle_button = Checkbutton(self.main_frame, text="show Password",background="#E0F8E0")
        self.toggle_button.place(x=800, y=590)

        self.submit_button = Button(self.main_frame, bg="green", fg="white", text="Submit", width=15, command=self.submit,font=("bold", 15))
        self.submit_button.place(x=850, y=660)

        self.login_button = Button(self.main_frame, bg="red", fg="white", text="Login", width=15,font=("bold", 15), command=self.login)
        self.login_button.place(x=400, y=660)


        self.lbl = tk.Label(self.main_frame, text="_🚕____________________🚗___________________🚓_________________🚙___________🚜_________________🚕____________________🚗___________________🏎️_________________🚙____________________🚜_________________🚕____________________🚗___________________🚓_________________🚙________________🚜________________",
                             width=300, font=("bold", 40), background="#E0F8E0")
        self.lbl.place(x=500, y=560)

        # Update layout for additional fields based on user type
        self.update_layout()

        # Trace user_type variable to update layout dynamically
        self.var_user_type.trace("w", lambda *args: self.update_layout())

    def submit(self):
    # Your existing submit method here...
      full_name = self.entry_full_name.get()
      dob = self.entry_dob.get_date()
      phone_number = self.entry_phone_number.get()
      gender = self.var_gender.get()
      user_type = self.var_user_type.get()
      email = self.entry_email.get()
      license_number = ""
      vehicle_number = ""
      password = self.password_entry.get()
      db = UserDatabase()

    # Additional fields for drivers
      if user_type == "Driver":
        license_number = self.entry_license.get()
        vehicle_number = self.entry_vehicleNo.get()
        # You can process the additional driver fields as needed

    # Basic validation
      if (
         (full_name == '')
        or (dob == '')
        or (phone_number == '')  # Validation for phone number length
        or (gender == '')
        or (user_type == '')
        or (email == '')
        or (password == '')  # Validation for password length
       ):
         messagebox.showwarning("Taxi Booking System", "Please enter all the fields correctly!")
      elif len(phone_number) < 10:
           messagebox.showwarning("Taxi Booking System", "Phone number should be at least 10 digits!")
      elif len(password) < 6:
       messagebox.showwarning("Taxi Booking System", "Password should be at least 6 characters!")
    #   elif not validate_email(email):
    #     messagebox.showwarning("Taxi Booking System", "Please enter a valid email address")
      elif user_type == "Driver" and (license_number == '' or vehicle_number == ''):
        messagebox.showwarning("Taxi Booking System", "Please enter licence number and vehicle number")
      elif db.search_user(phone_number, email):
        warning = messagebox.showwarning("Taxi Booking System", "Email or mobile number already registered!")
      else:
         db.connect()  # Ensure the database connection is opened
         if user_type == "Customer":
          db.insert_customers(full_name, dob, phone_number, gender, user_type, email, password)
         else:
          db.insert_drivers(full_name, dob, phone_number, gender, user_type, email, license_number, vehicle_number, password)
         db.close_connection()  # Close the connection after use
        # Close the connection after use
         messagebox.showwarning("Taxi Booking System", "Registration completed!")
         self.clear()


    def clear(self):
        self.entry_full_name.delete(0, 'end')
        self.entry_dob.delete(0, 'end')
        self.entry_phone_number.delete(0, 'end')
        self.var_gender.set('')
        self.var_user_type.set('')
        self.entry_email.delete(0, 'end')
        self.entry_license.delete(0, 'end')
        self.entry_vehicleNo.delete(0, 'end')
        self.password_entry.delete(0, 'end')
    def update_layout(self):
        if self.var_user_type.get() == "Driver":
            self.license_label.place(x=830, y=470)
            self.entry_license.place(x=1020, y=470)

            self.vehicleNo_label.place(x=830, y=540)
            self.entry_vehicleNo.place(x=1020, y=540)
        elif self.var_user_type.get() == "Customer":
            self.license_label.place_forget()
            self.entry_license.place_forget()
            self.vehicleNo_label.place_forget()
            self.entry_vehicleNo.place_forget()
    def login(self):

        self.root.destroy()

        from home import Login

        login = Login(root)
        Login.mainloop()
    def animate_label(self):
      def update_animation():
        x = self.lbl.winfo_x()
        if x < -self.lbl.winfo_reqwidth():
            x = self.main_frame.winfo_width()
        else:
            x -= 1  # Adjust the speed of the animation by changing this value

        self.lbl.place(x=x, y=720)
        self.main_frame.after(5, update_animation)  # Use a nested function for the loop

      update_animation()

        


root = tk.Tk()
app = RegistrationForm(root)
root.title("Taxi Booking System")
app.animate_label()
root.state("zoomed")
root.mainloop()
