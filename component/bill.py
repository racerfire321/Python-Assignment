import tkinter as tk
from tkinter import ttk
from dbms.bookingdb import BookingDatabase
from dbms import Global
from component.billing import Bill

class DisplayBill:
    def __init__(self, main_frame, ride_data):
        self.sub_frame = main_frame
        style = ttk.Style()
        style.configure("Treeview.Treeview", rowheight=40, padding=(10, 10))

        self.ridehistory_tree = ttk.Treeview(self.sub_frame, columns=(
            "Booking Id", "Pickup Date", "Pickup Time", "Origin", "Destination", "Status","Customer Id" ,"Driver Id"),
                                             show="headings", style="Treeview.Treeview")

        # Add column headings
        self.ridehistory_tree.heading("Booking Id", text="Booking Id")
        self.ridehistory_tree.heading("Pickup Date", text="Pickup Date")
        self.ridehistory_tree.heading("Pickup Time", text="Pickup Time")
        self.ridehistory_tree.heading("Origin", text="Origin")
        self.ridehistory_tree.heading("Destination", text="Destination")
        self.ridehistory_tree.heading("Status", text="Status")
        self.ridehistory_tree.heading("Customer Id", text="Customer Id")
        self.ridehistory_tree.heading("Driver Id", text="Driver Id")
        self.ridehistory_tree.place(x=50, y=50, height=400, width=900)
        self.ridehistory_tree.bind("<<TreeviewSelect>>", self.selectedRow)

        # Set up column widths
        column_width = 900 // 8
        for column in ("Booking Id", "Pickup Date", "Pickup Time", "Origin", "Destination", "Status","Customer Id", "Driver Id"):
            self.ridehistory_tree.column(column, width=column_width)

        # Configure tags for bold text and green color
        self.ridehistory_tree.tag_configure('bold', font=('TkDefaultFont', 12, 'bold'))
        self.ridehistory_tree.tag_configure('header', font=('TkDefaultFont', 12, 'bold'))
        self.ridehistory_tree.tag_configure('larger_font', font=('TkDefaultFont', 14))

        self.ride_data = ride_data
        # Insert data into Treeview
        for row in self.ride_data:
            self.ridehistory_tree.insert("", "end", values=row, tags=('green' if row[5] == 'Completed' else '','larger_font'))

        generate_bill_button = tk.Button(self.sub_frame,width=15,background="#E0F8E0",foreground="Black", font=('Times New Roman', 14, 'bold') ,text=f"Generate Bill", command = self.generate_bill)
        generate_bill_button.place(x=800, y=550)

        printe_bill_button = tk.Button(self.sub_frame, width=15, background="#E0F8E0", foreground="Black",
                                         font=('Times New Roman', 14, 'bold'), text=f"Print Bill",)
        printe_bill_button.place(x=800, y=620)

        self.label = tk.Label(self.sub_frame,text="Bill:", font=('Times New Roman', 26, 'bold'))
        self.label.place(x=150,y= 550)
        self.label = tk.Label(self.sub_frame, text="Select the booking from above to generate bill ",background="white" ,font=('Times New Roman', 18, 'bold'))
        self.label.place(x=250, y=470)
        self.bill_frame = tk.Frame(self.sub_frame, width=420, height=200,background="#E0F8E0")
        self.bill_frame.place(x=290, y=520)

    def selectedRow(self, event):
        selected_item = self.ridehistory_tree.focus()
        values = self.ridehistory_tree.item(selected_item, "values")

        if values:
            self.bookingid = values[0]
            print("Selected Booking ID:", self.bookingid)

    def generate_bill(self):
        # Create a frame to display the bill
        self.bill_frame = tk.Frame(self.sub_frame, width=420, height=200, background="#E0F8E0")
        self.bill_frame.place(x=290, y=520)

        # If it doesn't exist, create a new instance of the Bill class
        self.bill_instance = Bill(self.bill_frame, self.bookingid)

        # Add a button to close the window
        close_button = tk.Button(self.bill_frame, text="Close", command=self.close_bill_frame)
        close_button.place(x=290, y=300)



    def close_bill_frame(self):
            # Destroy the bill frame when the close button is clicked
            self.bill_frame.destroy()

    def update_booking_id(self, new_bookingid):
        self.bookingid = new_bookingid

    def sort_treeview(self, column):
        # Sorting logic goes here
        items = [(self.ridehistory_tree.set(k, column), k) for k in self.ridehistory_tree.get_children("")]
        items.sort()
        for index, (val, k) in enumerate(items):
            self.ridehistory_tree.move(k, "", index)
        self.ridehistory_tree.heading(column, command=lambda: self.reverse_sort_treeview(column))

    def reverse_sort_treeview(self, column):
        # Reverse sorting logic goes here
        items = [(self.ridehistory_tree.set(k, column), k) for k in self.ridehistory_tree.get_children("")]
        items.sort(reverse=True)
        for index, (val, k) in enumerate(items):
            self.ridehistory_tree.move(k, "", index)
        self.ridehistory_tree.heading(column, command=lambda: self.sort_treeview(column))

