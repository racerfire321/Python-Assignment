import tkinter as tk
from tkinter import ttk

import win32print

from dbms.bookingdb import BookingDatabase

class Bill:
    def __init__(self, main_frame, bookingid):
        self.main_frame = main_frame
        self.bookingid = bookingid
        self.create_frame()

    def create_frame(self):
        billing_frame = tk.Frame(self.main_frame, width=400, height=200, background="#D3E3D3")
        billing_frame.place(x=20, y=20)

        # Add a heading to the billing frame
        # heading_label = tk.Label(billing_frame, text="Taxi Booking Service", font=("Helvetica", 16, "bold"),
        #                          background="#D3E3D3")
        # heading_label.place(x=10, y=5)
        db = BookingDatabase()
        records = db.display_bill(self.bookingid)
        record = records[0]
        print(record)

        # Create a Treeview widget for the billing information
        billing_table = ttk.Treeview(billing_frame, columns=("Service Description", "Amount"), show="headings", height=5)
        billing_table.heading("Service Description", text="Service Description")
        billing_table.heading("Amount", text="Amount")
        billing_table.place(x=20, y=150)
        billing_table.grid(row=0, column=2, padx=5, pady=3, columnspan=2, sticky="w")

        # Add billing data to the table based on the record
        billing_data = [
            ("Ride Fare", f"${record[1]:,.2f}"),    # Assuming record[1] contains the amount
            ("Discount", f"${record[3]:,.2f}"),     # Assuming record[2] contains the discount
            ("VAT", f"${record[2]:,.2f}")           # Assuming record[3] contains the VAT
        ]

        for label, value in billing_data:
            billing_table.insert("", "end", values=(label, value))

        # Draw a line
        line = tk.Frame(billing_frame, height=2, width=300, bg="black")
        line.grid(row=1, column=2, columnspan=2, pady=5)

        # Calculate and display total amount
        total_amount = record[4]  # Assuming record[4] contains the total amount as a float
        total_amount_label = tk.Label(billing_frame, text=f"Total Amount: ${total_amount:.2f}",
                                      background="#D3E3D3", font=("Helvetica", 10, "bold"))
        total_amount_label.grid(row=2, column=2, columnspan=2, pady=5)

        billing_frame.pack(pady=10)

    def update_booking_id(self, new_bookingid):
        # Update the booking ID and recreate the frame with the new ID
        self.bookingid = new_bookingid
        self.create_frame()
