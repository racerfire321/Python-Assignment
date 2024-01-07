from tkinter import *
from tkinter import ttk, messagebox

from dbms.admin import AdminDatabase
from dbms.updateuser import UpdateDatabase


class ViewDriver:
    def __init__(self, main_frame):

        self.main_frame = main_frame

        self.textField = Frame(self.main_frame, bg="#404040")
        self.textField.place(x=0, y=440, width=1200, height=380)

        self.body = Frame(self.main_frame, bg="#E0F8E0")
        self.body.place(x=0, y=0, height=450, width=1200)

        self.lblFullName = Label(self.textField, text="Full Name:", font=("Arial", 16, "bold"), bg="#E0F8E0",
                                 anchor="w")
        self.lblFullName.place(x=20, y=80, height=30, width=200) # Adjusted y-coordinate
        self.full_name_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                     highlightthickness=2)
        self.full_name_entry.place(x=150, y=80, height=35, width=150)

        self.lblDob = Label(self.textField, text="Date of Birth:", font=("Arial", 16, "bold"), bg="#E0F8E0", anchor="w")
        self.lblDob.place(x=420, y=80, height=30, width=200)  # Adjusted y-coordinate
        self.dob_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                               highlightthickness=2)
        self.dob_entry.place(x=550, y=80, height=35, width=150)

        self.lblPhoneNumber = Label(self.textField, text="Phone No:", font=("Arial", 16, "bold"), bg="#E0F8E0",
                                    anchor="w")
        self.lblPhoneNumber.place(x=20, y=160, height=30, width=200)  # Adjusted y-coordinate
        self.phone_number_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                        highlightthickness=2)
        self.phone_number_entry.place(x=150, y=160, height=35, width=150)

        self.lblGender = Label(self.textField, text="Gender:", font=("Arial", 16, "bold"), bg="#E0F8E0", anchor="w")
        self.lblGender.place(x=420, y=160, height=30, width=200)  # Adjusted y-coordinate
        self.gender_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                  highlightthickness=2)
        self.gender_entry.place(x=550, y=160, height=35, width=150)

        self.lblEmail = Label(self.textField, text="Email:", font=("Arial", 16, "bold"), bg="#E0F8E0", anchor="w")
        self.lblEmail.place(x=20, y=240, height=30, width=200)  # Adjusted y-coordinate
        self.email_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                 highlightthickness=2)
        self.email_entry.place(x=150, y=240, height=35, width=150)

        self.lblPassword = Label(self.textField, text="Password:", font=("Arial", 16, "bold"), bg="#E0F8E0", anchor="w")
        self.lblPassword.place(x=420, y=240, height=30, width=200)  # Adjusted y-coordinate
        self.password_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                  highlightthickness=2)
        self.password_entry.place(x=550, y=240, height=35, width=150)
        self.id_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                    highlightthickness=2)
        self.id_entry.place(x=550, y=440, height=35, width=150)

        self.btnUpdate = Button(self.textField, text="Update", bg="green", fg="white", font=('Arial', 20, 'bold'),
                                bd=0, activebackground='green', activeforeground="white", command=self.update_booking)
        self.btnUpdate.place(x=850, y=100, height=55, width=150)
        self.btnDelete = Button(self.textField, text="Delete", bg="red", fg="white", font=('Arial', 20, 'bold'),
                                bd=0, activebackground='red', activeforeground="white",command=self.delete)
        self.btnDelete.place(x=850, y=200, height=55, width=150)
        # Adjusted y-coordinate

        self.tree = ttk.Treeview(self.body, columns=(
            "driver_id", "full_name", "dob", "phone_number", "gender", "user_type", "email", "password",
            "license_number", "vehicle_number"),
                                 show="headings")

        # Set the headings for each column
        self.tree.heading("driver_id", text="Driver ID")
        self.tree.heading("full_name", text="Full Name")
        self.tree.heading("dob", text="Date of Birth")
        self.tree.heading("phone_number", text="Phone Number")
        self.tree.heading("gender", text="Gender")
        self.tree.heading("user_type", text="User Type")
        self.tree.heading("email", text="Email")
        self.tree.heading("password", text="Password")
        self.tree.heading("license_number", text="License Number")
        self.tree.heading("vehicle_number", text="Vehicle Number")

        self.tree.place(x=50, y=50, height=380, width=1000)
        self.tree.bind("<<TreeviewSelect>>", self.selectedRow)

        column_width = 1000 // 10
        for column in (
                "driver_id", "full_name", "dob", "phone_number", "gender", "user_type", "email", "password",
                "license_number", "vehicle_number"):
            self.tree.column(column, width=column_width)

        db = AdminDatabase()
        data = db.driverTable()  # Assuming you have a method named driverTable in your AdminDatabase class
        # Insert data into Treeview
        for row in data:
            self.tree.insert("", "end", values=row)
    def selectedRow(self, event):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")

        if values:
            self.full_name_entry.delete(0, "end")
            self.full_name_entry.insert(0, values[1])

            self.dob_entry.delete(0, "end")
            self.dob_entry.insert(0, values[2])

            self.phone_number_entry.delete(0, "end")
            self.phone_number_entry.insert(0, values[3])

            self.gender_entry.delete(0, "end")
            self.gender_entry.insert(0, values[4])

            self.email_entry.delete(0, "end")
            self.email_entry.insert(0, values[6])

            self.password_entry.delete(0, "end")
            self.password_entry.insert(0, values[7])

            self.id_entry.delete(0, "end")
            self.id_entry.insert(0, values[0])

    def update_booking(self):

        driver_id = self.id_entry.get()
        full_name = self.full_name_entry.get()
        dob = self.dob_entry.get()
        phone_number = self.phone_number_entry.get()
        gender = self.gender_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        db = AdminDatabase()
        db.updateDriver(driver_id, full_name, dob, phone_number, gender, email, password)

        db.close_connection()
        self.update_treeview()
        messagebox.showinfo("Success", "Driver updated successfully!")


    def delete(self):
        pass
        db = AdminDatabase()
        driver_id = self.id_entry.get()

        # Call the delete_booking method from BookingDatabase
        db.delete_driver(driver_id)
        db.close_connection()
        self.update_treeview()
        messagebox.showinfo("Success", "Deleted Driver successfully!")


    def update_treeview(self):
        # Clear the existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch the updated data from the database for bookings
        db = AdminDatabase()
        updated_data = db.driverTable()

        # Insert the updated data into the Treeview for bookings
        for row in updated_data:
            self.tree.insert("", "end", values=row)


