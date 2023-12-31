import tkinter as tk
from tkinter import ttk, Entry, StringVar, Button, Checkbutton
from tkinter import messagebox
from tkcalendar import DateEntry
from dbms.userdb import UserDatabase
from PIL import Image, ImageTk



class RegistrationForm:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")

        # Create a frame for the image

        # Create a main frame
        self.frame = tk.Frame(root,bg="white")
        self.frame.pack(expand=True, fill='both')

        self.image_frame = tk.Frame(self.frame)
        self.image_frame.pack(side=tk.LEFT, pady=0)

        # Add an image (replace "path_to_image.png" with the actual path to your image file)
        # self.image_path = "../img/cab_driver_device_1.jpg"
        # self.img = Image.open(self.image_path)
        # self.img = ImageTk.PhotoImage(self.img)
        # self.image_label = tk.Label(self.image_frame, image=self.img)
        # self.image_label.pack(side=tk.LEFT)

        original_image = Image.open("../img/cab_driver_device_1.jpg")
        resized_image = original_image.resize((900, 720))
        img = ImageTk.PhotoImage(resized_image)
        self.image_label = tk.Label(self.image_frame, image=img)
        self.image_label.pack(side=tk.LEFT)
        self.image_label.image = img

        self.main_frame = tk.Frame(self.frame, background="#c3ecb2")
        self.main_frame.place(x=900,y=0,height=750,width=700)

        self.header = tk.Label(self.main_frame, text="Registration Form", background="#c3ecb2",   foreground="green", font=("Times New Roman", 34, "bold"))
        self.header.place(x=150, y=40)

        self.full_name_label = tk.Label(self.main_frame, text="Full Name", width=20, font=("bold", 15), background="#c3ecb2")
        self.full_name_label.place(x=60, y=150)
        self.entry_full_name = Entry(self.main_frame, width=20, font=("bold", 15),highlightcolor="green",highlightthickness=3)
        self.entry_full_name.place(x=260, y=150)

        self.dob_label = tk.Label(self.main_frame, text="Date of Birth", width=20, font=("bold", 15), background="#c3ecb2")
        self.dob_label.place(x=60, y=210)
        self.entry_dob = DateEntry(self.main_frame, width=20, font=("bold", 15),highlightcolor="green",highlightthickness=3)
        self.entry_dob.place(x=260, y=210)

        self.phoneNumber_label = tk.Label(self.main_frame, text="Phone Number", width=20, font=("bold", 15), background="#c3ecb2")
        self.phoneNumber_label.place(x=60, y=270)
        self.entry_phone_number = Entry(self.main_frame, width=20, font=("bold", 15),highlightcolor="green",highlightthickness=3)
        self.entry_phone_number.place(x=260, y=270)

        self.email_label = tk.Label(self.main_frame, text="Email", width=20, font=("bold", 15), background="#c3ecb2")
        self.email_label.place(x=60, y=330)
        self.entry_email = Entry(self.main_frame, width=20, font=("bold", 15),highlightcolor="green",highlightthickness=3)
        self.entry_email.place(x=260, y=330)

        self.root.style = ttk.Style()
        self.root.style.configure("TRadiobutton", background="#c3ecb2",font=("bold", 15),highlightcolor="green",highlightthickness=3)

        self.gender_label = tk.Label(self.main_frame, text="Gender", width=20, font=("bold", 15), background="#c3ecb2")
        self.gender_label.place(x=60, y=390)
        self.var_gender = StringVar()
        self.R1 = ttk.Radiobutton(self.main_frame, text="Male", variable=self.var_gender, value="Male",
                                  style="TRadiobutton")
        self.R1.place(x=250, y=390)

        self.R2 = ttk.Radiobutton(self.main_frame, text="Female", variable=self.var_gender, value="Female",
                                  style="TRadiobutton")
        self.R2.place(x=360, y=390)

        self.user_type_label = tk.Label(self.main_frame, text="Type", width=20, font=("bold", 15), background="#c3ecb2")
        self.user_type_label.place(x=60, y=450)
        self.user_types = ["Customer", "Driver"]
        self.var_user_type = StringVar()
        self.user_type_combobox = ttk.Combobox(self.main_frame, textvariable=self.var_user_type, values=self.user_types, state="readonly", font=("bold", 12))
        self.user_type_combobox.place(x=260, y=450)

        self.license_label = tk.Label(self.main_frame, text="License No", width=20, font=("bold", 15), background="#c3ecb2")
        self.entry_license = Entry(self.main_frame, width=20, font=("bold", 15),highlightcolor="green",highlightthickness=3)

        self.vehicleNo_label = tk.Label(self.main_frame, text="Vehicle No", width=20, font=("bold", 15), background="#c3ecb2")
        self.entry_vehicleNo = Entry(self.main_frame, width=20, font=("bold", 15),highlightcolor="green",highlightthickness=3)

        self.payment_label = tk.Label(self.main_frame, text="Payment", width=20, font=("bold", 15), background="#c3ecb2")
        self.payment_label.place(x=60, y=510)
        self.payment_types = ["Credit Card", "Mobile Banking","Online Payment","Cash"]
        self.var_payment_types = StringVar()
        self.payment_types_combobox = ttk.Combobox(self.main_frame, textvariable=self.var_payment_types, values=self.payment_types,
                                               state="readonly", font=("bold", 12))
        self.payment_types_combobox.place(x=260, y=510)
        self.credit_label = tk.Label(self.main_frame, text="CreditCard No:", width=20, font=("bold", 15),
                                        background="#c3ecb2")
        self.credit_label.place(x=60, y=570)
        self.entry_credit = Entry(self.main_frame, width=20, font=("bold", 15),highlightcolor="green",highlightthickness=3)
        self.entry_credit.place(x=260, y=570)


        self.password_label = tk.Label(self.main_frame, text="Password:", width=20, font=("bold", 15),background="#c3ecb2")
        self.password_label.place(x=60, y=630)

        self.password_entry = Entry(self.main_frame, show="*", width=20, font=("bold", 15),highlightcolor="green",highlightthickness=3)
        self.password_entry.place(x=260, y=630)

        self.toggle_button = Checkbutton(self.main_frame, text="show Password",background="#c3ecb2")
        self.toggle_button.place(x=490, y=630)

        self.submit_button = Button(self.main_frame, bg="green", fg="white", text="Submit", width=14, command=self.submit,font=("bold", 14))
        self.submit_button.place(x=430, y=690)

        self.login_button = Button(self.main_frame, bg="red",
                                   fg="white", text="Login", width=14,font=("bold", 15), command=self.login)
        self.login_button.place(x=40, y=690)


        self.lbl = tk.Label(self.frame, text="_🚕____________________🚗___________________🚓_________________🚙___________🚜_________________🚕____________________🚗___________________🏎️_________________🚙____________________🚜_________________🚕____________________🚗___________________🚓_________________🚙________________🚜________________",
                             width=400, font=("bold", 35), background="white")
        self.lbl.place(x=0, y=750)


        # Update layout for additional fields based on user type
        self.update_layout()
        self.animate_label()

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
      elif user_type == "Customer":
        payment_method = self.var_payment_types.get()
        creditcard_No = self.entry_credit.get()

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
          db.insert_customers(full_name, dob, phone_number, gender, user_type, email, password,payment_method,creditcard_No)
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
            self.license_label.place(x=60, y=510)
            self.entry_license.place(x=260, y=510)
            self.vehicleNo_label.place(x=60, y=570)
            self.entry_vehicleNo.place(x=260, y=570)
            self.payment_label.place_forget()
            self.payment_types_combobox.place_forget()
            self.credit_label.place_forget()
            self.entry_credit.place_forget()

        else:
            self.license_label.place_forget()
            self.entry_license.place_forget()
            self.vehicleNo_label.place_forget()
            self.entry_vehicleNo.place_forget()
            self.credit_label.place(x=60, y=570)
            self.entry_credit.place(x=260, y=570)
            self.payment_label.place(x=60, y=510)
            self.payment_types_combobox.place(x=260, y=510)

    def login(self):

        self.root.destroy()

        from home import Login
        login_window = tk.Tk()
        Login(login_window)
        login_window.mainloop()
    def animate_label(self):
      def update_animation():
        x = self.lbl.winfo_x()
        if x < -self.lbl.winfo_reqwidth():
            x = self.main_frame.winfo_width()
        else:
            x -= 1  # Adjust the speed of the animation by changing this value

        self.lbl.place(x=x, y=740)
        self.main_frame.after(5, update_animation)  # Use a nested function for the loop

      update_animation()

        
if __name__ == "__main__":
    root = tk.Tk()

    registration_form = RegistrationForm(root)


    root.mainloop()

