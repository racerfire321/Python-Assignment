import tkinter as tk
from tkinter import ttk
from dbms.bookingdb import BookingDatabase
from dbms import Global
from component.billing import Bill

class RideHistory:
    def __init__(self, main_frame, ride_data):
        self.sub_frame = main_frame

        style = ttk.Style()
        style.configure("Treeview.Treeview", rowheight=40, padding=(10, 10))
        header_font = ('TkDefaultFont', 16, 'bold')
        # Adjust the padding value as needed
        self.ridehistory_tree = ttk.Treeview(self.sub_frame, columns=(
        "Booking Id", "Pickup Date", "Pickup Time", "Origin", "Destination", "Status", "Customer Id","Driver Id"), show="headings",style="Treeview.Treeview")

        # Add column headings
        self.ridehistory_tree.heading("Booking Id", text="Booking Id")
        self.ridehistory_tree.heading("Pickup Date", text="Pickup Date")
        self.ridehistory_tree.heading("Pickup Time", text="Pickup Time")
        self.ridehistory_tree.heading("Origin", text="Origin")
        self.ridehistory_tree.heading("Destination", text="Destination")
        self.ridehistory_tree.heading("Status", text="Status")
        self.ridehistory_tree.heading("Customer Id", text="Customer Id")
        self.ridehistory_tree.heading("Driver Id", text="Driver Id")
        self.ridehistory_tree.place(x=50, y=50, height=700, width=1000)


        # Set up column widths
        column_width = 1000 // 8
        for column in ("Booking Id", "Pickup Date", "Pickup Time", "Origin", "Destination", "Status",
                       "Customer Id", "Driver Id"):
            self.ridehistory_tree.column(column, width=column_width)

        # Configure tags for bold text and green color
        self.ridehistory_tree.tag_configure('bold', font=('TkDefaultFont', 12, 'bold'))
        self.ridehistory_tree.tag_configure('header', font=('TkDefaultFont', 12, 'bold'))

        # Configure a tag for larger font
        self.ridehistory_tree.tag_configure('larger_font',font=('TkDefaultFont', 14))

        self.ride_data = ride_data
        # Insert data into Treeview
        for row in self.ride_data:
            self.ridehistory_tree.insert("", "end", values=row, tags=('green' if row[5] == 'Completed' else '','larger_font'))
