import tkinter as tk
from tkinter import Entry, Button
from dbms.bookingdb import BookingDatabase
from dbms import Global
from component.billing import Bill



class updateBooking:
    def __init__(self, main_frame,data):
        self.main_frame = main_frame
        self.entry_frames = []
        Button = []# Store frames for each data record

        self.data = data
        for index, record in enumerate(self.data):
            entry_frame_id = f"entry_frame_{index}"
            entry_frame = tk.Frame(self.main_frame, width=1000, height=200, background="#E0F8E0", name=entry_frame_id)
            entry_frame.place(x=10, y=80)
            self.origin_label = tk.Label(entry_frame, text="Pickup", background="#E0F8E0", fg="dark green",
                                         font=("Helvetica", 16, "bold"))
            self.origin_label.place(x=30, y=50)
            self.origin_entry = tk.Entry(entry_frame, bg="white", font=("Helvetica", 16, "bold"))
            self.origin_entry.place(x=150, y=50)
            self.origin_entry.insert(0, record[3])


            destination_label = tk.Label(entry_frame, text="Destination", background="#E0F8E0",
                                         fg="dark green", font=("Helvetica", 16, "bold"))
            destination_label.place(x=30, y=100)
            self.destination_entry = tk.Entry(entry_frame, bg="white", font=("Helvetica", 16, "bold"))
            self.destination_entry.place(x=150, y=100)
            self.destination_entry.insert(0, record[4])

            date_label = tk.Label(entry_frame, text=" Date", background="#E0F8E0",
                                  fg="dark green", font=("Helvetica", 16, "bold"))
            date_label.place(x=430, y=50)
            self.date_entry = tk.Entry(entry_frame, bg="white", font=("Helvetica", 16, "bold"))
            self.date_entry.place(x=520, y=50)
            self.date_entry.insert(0, record[1])

            # Time entry
            time_label = tk.Label(entry_frame, text="Time", background="#E0F8E0",
                                  fg="dark green", font=("Helvetica", 16, "bold"))
            time_label.place(x=430, y=100)
            self.time_entry = tk.Entry(entry_frame, bg="white", width=5, font=("Helvetica", 16, "bold"))
            self.time_entry.place(x=520, y=100)
            self.time_entry.insert(0, record[2])

            bookingstatus_label = tk.Label(entry_frame, text="Status", background="#E0F8E0",
                                           fg="dark green", font=("Helvetica", 16, "bold"))
            bookingstatus_label.place(x=30, y=150)
            self.bookingstatus_entry = tk.Entry(entry_frame, bg="white", width=15, font=("Helvetica", 16, "bold"))
            self.bookingstatus_entry.place(x=150, y=150)
            self.bookingstatus_entry.insert(0, record[5])
            self.bookingid_entry = tk.Entry(entry_frame, width=1)
            self.bookingid_entry.place(x=790, y=40)
            self.bookingid_entry.insert(0, record[0])

            self.origin_entry.config(state=tk.DISABLED)
            self.destination_entry.config(state=tk.DISABLED)
            self.date_entry.config(state=tk.DISABLED)
            self.time_entry.config(state=tk.DISABLED)
            self.bookingstatus_entry.config(state=tk.DISABLED)

            self.edit_button[indes] = tk.Button(entry_frame, text="Edit", width=10, font=("Helvetica", 14, "bold"),
                                         background="green", foreground="white",command=lambda idx=index: self.edit_booking(idx))
            self.edit_button.place(x=780, y=30)

            self.submit_button[index] = tk.Button(entry_frame, bg="green", fg="white", text="Submit", width=12,
                                           font=("bold", 14),command=lambda idx=index: self.update_booking(idx))

            self.delete_button[index] = tk.Button(entry_frame, text="Delete", width=10, font=("Helvetica", 14, "bold"),
                                           background="red", foreground="white",
                                           command=lambda idx=index: self.delete(idx))
            self.delete_button.place(x=780, y=100)

            entry_frame.pack(pady=10)
            self.entry_frames.append(entry_frame)

        self.check_and_display_label()

    def check_and_display_label(self):
            if not self.data:
                self.label = tk.Label(self.main_frame,text="No Booking right now. Click the make booking button to book your ride",
                                      font=("bold", 18),background="white")
                self.label.place(x=400, y=400)
            elif hasattr(self, 'label'):
                self.label.destroy()
    # Implement other methods as needed (edit_booking, delete_booking)

    def edit_booking(self,index):
        self.origin_entry.config(state=tk.NORMAL)
        self.destination_entry.config(state=tk.NORMAL)
        self.date_entry.config(state=tk.NORMAL)
        self.time_entry.config(state=tk.NORMAL)
        self.submit_button.place(x=780, y=30)


    def update_booking(self,index):
        db = BookingDatabase()
        date = self.date_entry.get()
        time = self.time_entry.get()
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()
        bookingstatus = self.bookingstatus_entry.get()
        booking_id = self.bookingid_entry.get()

        db.update_booking(date, time, origin, destination, bookingstatus, booking_id)
        db.close_connection()
        self.origin_entry.config(state=tk.DISABLED)
        self.destination_entry.config(state=tk.DISABLED)
        self.date_entry.config(state=tk.DISABLED)
        self.time_entry.config(state=tk.DISABLED)
        self.submit_button.place_forget()
        self.edit_button.place(x=780, y=30)

    def delete(self, index):
        db = BookingDatabase()
        date = self.date_entry.get()
        time = self.time_entry.get()
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()
        bookingstatus = "pending"
        booking_id = self.bookingid_entry.get()

        db.delete_booking(booking_id)
        db.close_connection()

        # Destroy the entry frame associated with the rejected booking
        self.destroy_entry_frame(index)

    def destroy_entry_frame(self,record):
        # Destroy the entry frame
        if self.entry_frames:
            entry_frame = self.entry_frames.pop(record)  # Assuming you want to destroy the first entry frame
            entry_frame.destroy()