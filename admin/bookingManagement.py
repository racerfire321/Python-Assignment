from tkinter import *
from tkinter import ttk, messagebox
from dbms import Global
from dbms.admin import AdminDatabase
from dbms.bookingdb import BookingDatabase


class ViewBooking:
    def __init__(self, main_frame):

        self.main_frame = main_frame

        self.textField = Frame(self.main_frame, bg="#404040")
        self.textField.place(x=0, y=440, width=1200, height=380)

        self.body = Frame(self.main_frame, bg="#E0F8E0")
        self.body.place(x=0, y=0, height=450, width=1200)

        self.lblorigin = Label(self.textField, text="Origin ", font=("Arial", 16, "bold"), bg="#E0F8E0",
                               anchor="w")
        self.lblorigin.place(x=20, y=80, height=30, width=200)
        self.origin_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                  highlightthickness=2)
        self.origin_entry.place(x=150, y=80, height=35, width=150)

        self.lbldestination = Label(self.textField, text="Destination", font=("Arial", 16, "bold"), bg="#E0F8E0",
                                    anchor="w")
        self.lbldestination.place(x=420, y=80, height=30, width=200)
        self.destination_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                       highlightthickness=2)
        self.destination_entry.place(x=550, y=80, height=35, width=150)

        self.lblTime = Label(self.textField, text="Pickup-Time:", font=("Arial", 16, "bold"), bg="#E0F8E0", anchor="w")
        self.lblTime.place(x=20, y=160, height=30, width=200)  # Adjusted y-coordinate
        self.time_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                highlightthickness=2)
        self.time_entry.place(x=150, y=160, height=35, width=150)

        self.lblDate = Label(self.textField, text="Pickup-Date:", font=("Arial", 16, "bold"), bg="#E0F8E0", anchor="w")
        self.lblDate.place(x=420, y=160, height=30, width=200)  # Adjusted y-coordinate
        self.date_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                highlightthickness=2)
        self.date_entry.place(x=550, y=160, height=35, width=150)

        self.lblStatus = Label(self.textField, text="Status:", font=("Arial", 16, "bold"), bg="#E0F8E0", anchor="w")
        self.lblStatus.place(x=20, y=240, height=30, width=200)  # Adjusted y-coordinate
        self.bookingstatus_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                         highlightthickness=2)
        self.bookingstatus_entry.place(x=150, y=240, height=35, width=150)  # Adjusted width

        self.bookingid_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                     highlightthickness=2)
        self.bookingid_entry.place(x=220, y=400, height=35, width=150)  # Adjusted y-coordinate
        self.lbldriver = Label(self.textField, text="Driver:", font=("Arial", 16, "bold"), bg="#E0F8E0", anchor="w")
        self.lbldriver.place(x=420, y=240, height=30, width=200)
        self.driverid_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                    highlightthickness=2)
        self.driverid_entry.place(x=550, y=240, height=35, width=150)
        self.cusid_entry = Entry(self.textField, font=("Arial", 14, "bold"), highlightcolor="orange",
                                    highlightthickness=2)
        self.cusid_entry.place(x=950, y=1040, height=1, width=1)
        # Adjusted y-coordinate

        self.btnUpdate = Button(self.textField, text="Update", bg="green", fg="white", font=('Arial', 20, 'bold'),
                                bd=0, activebackground='green', activeforeground="white",command=self.update_booking)
        self.btnUpdate.place(x=850, y=100, height=55, width=150)
        self.btnDelete = Button(self.textField, text="Delete", bg="red", fg="white", font=('Arial', 20, 'bold'),
                                bd=0, activebackground='red', activeforeground="white",command=self.delete)
        self.btnDelete.place(x=850, y=200, height=55, width=150)
        # Adjusted y-coordinate
        self.tree = ttk.Treeview(self.body, columns=(
            "booking_id", "date", "time", "origin", "destination", "bookingstatus", "customersid", "driverid"),
                                 show="headings")

        # Set the headings for each column
        self.tree.heading("booking_id", text="booking_id")
        self.tree.heading("date", text="date")
        self.tree.heading("time", text="time")
        self.tree.heading("origin", text="origin")
        self.tree.heading("destination", text="destination")
        self.tree.heading("bookingstatus", text="bookingstatus")
        self.tree.heading("customersid", text="customersid")
        self.tree.heading("driverid", text="driverid")

        self.tree.place(x=50, y=50, height=380, width=900)
        self.tree.bind("<<TreeviewSelect>>", self.selectedRow)

        column_width = 900 // 8
        for column in ("booking_id", "date", "time", "origin", "destination", "bookingstatus", "customersid", "driverid"):
            self.tree.column(column, width=column_width)

        db = AdminDatabase()
        data = db.bookingTable()
    # Insert data into Treeview
        for row in data:
            self.tree.insert("", "end", values=row)
        self.tree2 = ttk.Treeview(self.body, columns=("driverid"), show="headings")

        self.tree2.heading("driverid", text="driverid")

        self.tree2.place(x=1000, y=50, height=380, width=100)
        self.tree2.bind("<<TreeviewSelect>>")

        column_width2 = 100 // 1
        for column2 in ("driverid",):
            self.tree2.column(column2, width=column_width2)

        db = AdminDatabase()
        datas = db.availableDriver()
        # Insert data into Treeview
        for rows in datas:
            self.tree2.insert("", "end", values=rows)

    def selectedRow(self, event):
        selected_item = self.tree.focus()
        values = self.tree.item(selected_item, "values")

        if values:
            self.origin_entry.delete(0, "end")
            self.origin_entry.insert(0, values[3])

            self.destination_entry.delete(0, "end")
            self.destination_entry.insert(0, values[4])

            self.time_entry.delete(0, "end")
            self.time_entry.insert(0, values[2])

            self.date_entry.delete(0, "end")
            self.date_entry.insert(0, values[1])

            self.bookingstatus_entry.delete(0, "end")
            self.bookingstatus_entry.insert(0, values[5])

            self.bookingid_entry.delete(0, "end")
            self.bookingid_entry.insert(0, values[0])
            self.cusid_entry.delete(0, "end")
            self.cusid_entry.insert(0, values[6])

            self.driverid_entry.delete(0, "end")
            self.driverid_entry.insert(0, values[7])

    def update_booking(self):
        db = AdminDatabase()
        date = self.date_entry.get()
        time = self.time_entry.get()
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()
        bookingstatus = self.bookingstatus_entry.get()
        driverid = self.driverid_entry.get()
        adminid = Global.adminid
        customersid = self.cusid_entry.get()
        booking_id = self.bookingid_entry.get()

        db.updatebooking(booking_id, date, time, origin, destination, bookingstatus,customersid, driverid, adminid)
        db.close_connection()

        self.update_treeview()
        messagebox.showinfo("Success", "Booking updated successfully!")

    def delete(self):
        pass
        db = BookingDatabase()
        booking_id = self.bookingid_entry.get()

        # Call the delete_booking method from BookingDatabase
        db.delete_booking(booking_id)
        db.close_connection()

        self.update_treeview()
        messagebox.showinfo("Success", "Booking deleted successfully!")

    def update_treeview(self):
        # Clear the existing data in the Treeview
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Fetch the updated data from the database for bookings
        db = AdminDatabase()
        updated_data = db.bookingTable()

        # Insert the updated data into the Treeview for bookings
        for row in updated_data:
            self.tree.insert("", "end", values=row)

        # Clear the existing data in the Treeview for available drivers
        for item in self.tree2.get_children():
            self.tree2.delete(item)

        # Fetch the updated data from the database for available drivers
        updated_datadriver = db.availableDriver()

        # Insert the updated data into the Treeview for available drivers
        for row in updated_datadriver:
            self.tree2.insert("", "end", values=row)