from tkcalendar import DateEntry
import tkinter as tk
from tkinter import Entry, Button, messagebox
from dbms.bookingdb import BookingDatabase
from dbms import Global

class viewBooking:
    def __init__(self, main_frame, data):
        self.main_frame = main_frame
        self.entry_frames = []
        self.read_data(data)


    def read_data(self, data):
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

            # ... (previous code)

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

            self.completed_button = tk.Button(entry_frame, text="Completed", width=10, font=("Helvetica", 14, "bold"),
                                              background="green", foreground="white",
                                              command=lambda idx=index: self.completed_booking(idx))
            self.completed_button.place(x=780, y=30)

            self.reject_button = tk.Button(entry_frame, text="Reject", width=10, font=("Helvetica", 14, "bold"),
                                           background="red", foreground="white",
                                           command=lambda idx=index: self.reject(idx))
            self.reject_button.place(x=780, y=100)

            entry_frame.pack(pady=10)
            self.entry_frames.append(entry_frame)

        self.check_and_display_label()

    def check_and_display_label(self):
        if not self.data:
            self.label = tk.Label(self.main_frame,
                                  text="No trips right now. Have a good day!",
                                  font=("bold", 18), background="white")
            self.label.place(x=400, y=400)
        elif hasattr(self, 'label'):
            self.label.destroy()

    def completed_booking(self, index):
        db = BookingDatabase()
        bookingstatus = "completed"
        booking_id = self.data[index][0]
        db.completed_booking(bookingstatus, booking_id)
        messagebox.showinfo("Ride", "Ride completed Thank you!")
        db.close_connection()



        for frame in self.entry_frames:
            frame.destroy()
        self.entry_frames = []
        did = Global.driverid
        db = BookingDatabase()
        data = db.display_editbooking(did)
        self.read_data(data)

    def reject(self, index):
        db = BookingDatabase()
        bookingstatus = "rejected"
        booking_id = self.data[index][0]
        db.reject_booking(bookingstatus, booking_id)
        messagebox.showinfo("Ride", "Ride rejected Thank you!")
        db.close_connection()

        for frame in self.entry_frames:
            frame.destroy()
        self.entry_frames = []
        did = Global.driverid
        db = BookingDatabase()
        data = db.display_editbooking(did)
        self.read_data(data)

