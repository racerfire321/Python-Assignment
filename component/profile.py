import tkinter as tk
from tkinter import ttk, Entry, StringVar, Button, Checkbutton
from PIL import Image, ImageTk
from dbms.updateuser import UpdateDatabase
import tkinter.messagebox as messagebox
from dbms import Global

class Profile:
    def __init__(self,main_frame,data):
        self.main_frame = main_frame
        # Create a frame for the image
        self.image_frame = tk.Frame(self.main_frame)
        self.image_frame.place(x=80,y=0)

        # Add an image (replace "path_to_image.png" with the actual path to your image file)
        self.image_path = "../img/user.jpg"
        original_image = Image.open(self.image_path)
        resized_image = original_image.resize((400,300))
        self.img = ImageTk.PhotoImage(resized_image)

        # Create a label for the image and place it at the center-top
        self.image_label = tk.Label(self.main_frame, image=self.img)
        self.image_label.place(x=450,y=70)
        self.cid = Global.customerid

        self.full_name_label = tk.Label(self.main_frame, text="Full Name", width=15, font=("Helvetica", 18, "bold"),
                                        bg="white", fg="black")
        self.full_name_label.place(x=110, y=400)
        self.entry_full_name = Entry(self.main_frame, width=20, font=("bold", 15), bg="white",highlightcolor="green",highlightthickness=3)
        self.entry_full_name.place(x=350, y=400)
        self.entry_full_name.insert(0, data[1])
        self.entry_full_name.config(state=tk.DISABLED)

        self.dob_label = tk.Label(self.main_frame, text="Date of Birth", width=15, font=("Helvetica", 18, "bold"),
                                  bg="white", fg="black")
        self.dob_label.place(x=610, y=400)
        self.entry_dob = Entry(self.main_frame, width=20, font=("bold", 15), bg="white",highlightcolor="green",highlightthickness=3)
        self.entry_dob.place(x=850, y=400)
        self.entry_dob.insert(0, data[2])
        self.entry_dob.config(state=tk.DISABLED)

        self.phoneNumber_label = tk.Label(self.main_frame, text="Phone Number", width=15,
                                          font=("Helvetica", 18, "bold"), bg="white", fg="black")
        self.phoneNumber_label.place(x=120, y=480)
        self.entry_phone_number = Entry(self.main_frame, width=20, font=("bold", 15), bg="white",highlightcolor="green",highlightthickness=3)
        self.entry_phone_number.place(x=350, y=480)
        self.entry_phone_number.insert(0, data[3])
        self.entry_phone_number.config(state=tk.DISABLED)

        self.email_label = tk.Label(self.main_frame, text="Email", width=15, font=("Helvetica", 18, "bold"), bg="white",
                                    fg="black")
        self.email_label.place(x=610, y=480)
        self.entry_email = Entry(self.main_frame, width=20, font=("bold", 15), bg="white",highlightcolor="green",highlightthickness=3)
        self.entry_email.place(x=850, y=480)
        self.entry_email.insert(0, data[6])
        self.entry_email.config(state=tk.DISABLED)

        self.gender_label = tk.Label(self.main_frame, text="Gender", width=15, font=("Helvetica", 18, "bold"),
                                     bg="white", fg="black")
        self.gender_label.place(x=100, y=550)

        self.var_gender = StringVar()
        gender_options = ["Male", "Female"]

        # Create a Combobox for gender selection
        self.gender_combobox = ttk.Combobox(self.main_frame, textvariable=self.var_gender, values=gender_options,
                                            state="readonly", font=("bold", 12))
        self.gender_combobox.place(x=350, y=550)
        self.gender_combobox.set(data[4])
        self.gender_combobox.config(state=tk.DISABLED)

        self.password_label = tk.Label(self.main_frame, text="Password:",width=15, font=("Helvetica", 18, "bold"),
                                       bg="white", fg="black")
        self.password_label.place(x=620, y=550)
        self.password_entry = Entry(self.main_frame, show="*", width=20, font=("bold", 15), bg="white",highlightcolor="green",highlightthickness=3)
        self.password_entry.place(x=850, y=550)
        self.password_entry.insert(0, data[7])
        self.password_entry.config(state=tk.DISABLED)

        self.usertype = data[5]

        self.toggle_button = Checkbutton(self.main_frame, text="show Password", background="white",
                                         command=self.toggle_password_visibility)
        self.toggle_button.place(x=900, y=590)

        self.update_button = Button(self.main_frame, bg="green", fg="white", text="update", width=15,
                                    font=("bold", 15), command=self.diaplay_submit)
        self.update_button.place(x=850, y=660)
        self.submit_button = Button(self.main_frame, bg="green", fg="white", text="Submit", width=15,
                                    font=("bold", 15), command=self.update_profile)
        self.submit_button.place_forget()

    def toggle_password_visibility(self):
        current_state = self.password_entry.cget("show")
        if current_state == "*":
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def diaplay_submit(self):
        self.entry_full_name.config(state=tk.NORMAL)
        self.entry_dob.config(state=tk.NORMAL)
        self.entry_phone_number.config(state=tk.NORMAL)
        self.entry_email.config(state=tk.NORMAL)
        self.gender_combobox.config(state=tk.NORMAL)
        self.password_entry.config(state=tk.NORMAL)
        self.submit_button.place(x=850, y=660)
        self.update_button.place_forget()


    def update_profile(self):
        self.entry_full_name.config(state=tk.DISABLED)
        self.entry_dob.config(state=tk.DISABLED)
        self.entry_phone_number.config(state=tk.DISABLED)
        self.entry_email.config(state=tk.DISABLED)
        self.gender_combobox.config(state=tk.DISABLED)
        self.password_entry.config(state=tk.DISABLED)
        self.update_button = Button(self.main_frame, bg="green", fg="white", text="update", width=15,
                                    font=("bold", 15), command=self.diaplay_submit)
        self.update_button.place(x=850, y=660)
        db = UpdateDatabase()
        full_name = self.entry_full_name.get()
        dob = self.entry_dob.get()
        phone_number = self.entry_phone_number.get()
        gender = self.gender_combobox.get()
        email = self.entry_email.get()
        password = self.password_entry.get()
        customer_id = Global.customerid
        driver_id = Global.driverid
        db = UpdateDatabase()
        if(self.usertype == "Customer"):
          db.update_customer(full_name,dob,phone_number,gender,email,password,customer_id)

        elif(self.usertype == "Driver"):
            db.update_driver(full_name, dob, phone_number, gender, email, password,driver_id)
        self.submit_button.place_forget()

        self.update_button.place(x=850, y=660)
        messagebox.showinfo("Profile Updated", "Your profile has been updated successfully!")