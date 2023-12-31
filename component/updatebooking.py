import tkinter as tk
from tkinter import Entry, Button
from dbms.bookingdb import BookingDatabase
from dbms import Global
from component.billing import Bill
from tkinter import messagebox



class updateBooking:
    def __init__(self, main_frame,data):
        self.main_frame = main_frame
        self.entry_frames = []

        self.readData(data)
        # List for delete buttons
    def readData(self,data):
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
                self.destination_entry.insert( 0,record[4])

                date_label = tk.Label(entry_frame, text=" Date", background="#E0F8E0",
                                      fg="dark green", font=("Helvetica", 16, "bold"))
                date_label.place(x=430, y=50)
                self.date_entry = tk.Entry(entry_frame, bg="white", font=("Helvetica", 16, "bold"))
                self.date_entry.place(x=520, y=50)
                self.date_entry.insert(0,record[1])

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

                self.bookingstatus_entry.insert(0,record[5])
                self.bookingid_entry = tk.Entry(entry_frame, width=1)
                self.bookingid_entry.place(x=790, y=40)
                self.bookingid_entry.insert(0, record[0])

                self.date_entry.config(state="disabled")

                self.time_entry.config(state="disabled")

                self.origin_entry.config(state="disabled")

                self.destination_entry.config(state="disabled")

                self.bookingstatus_entry.config(state="disabled")

                self.bookingid_entry.config(state="disabled")
                self.edit_button = tk.Button(entry_frame, text="Update", width=10, font=("Helvetica", 14, "bold"),
                                        background="green", foreground="white")
                self.edit_button.place(x=780, y=30)
                self.edit_button.bind("<Button-1>", lambda event, idx=index: self.update_booking(event, idx))

                self.delete_button = tk.Button(entry_frame, text="Delete", width=10, font=("Helvetica", 14, "bold"),
                                          background="red", foreground="white")
                self.delete_button.place(x=780, y=100)
                self.delete_button.bind("<Button-1>", lambda event, idx=index: self.delete(event, idx))

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

    def update_booking(self, event, index):
        # Retrieve the data for the selected booking
        selected_data = self.data[index]

        # Create a new window for confirmation
        self.confirmation_window = tk.Toplevel(self.main_frame, background="#c3ecb2", width=100)
        self.confirmation_window.title("Confirmation")

        self.confirmation_window.resizable(False, False)

        # Hide window decorations (minimize, maximize, close buttons)
        self.confirmation_window.overrideredirect(True)

        # Calculate the screen width and height
        screen_width = self.confirmation_window.winfo_screenwidth()
        screen_height = self.confirmation_window.winfo_screenheight()

        # Calculate the x and y coordinates to center the window
        x_coordinate = int((screen_width - 100) / 2)  # Adjust 100 to your window width
        y_coordinate = int((screen_height - 100) / 2)  # Adjust 100 to your window height

        # Set the window position
        self.confirmation_window.geometry(f"+{x_coordinate}+{y_coordinate}")

        tk.Label( self.confirmation_window, text="Pickup:",background="#c3ecb2").grid(row=0, column=0, padx=10, pady=5)
        self.origin = tk.Entry( self.confirmation_window)
        self.origin.insert(0, selected_data[3])
        self.origin.grid(row=0, column=1, padx=10, pady=5)




        tk.Label( self.confirmation_window, text="Destination:",background="#c3ecb2").grid(row=1, column=0, padx=10, pady=5)
        self.destination = tk.Entry( self.confirmation_window)
        self.destination.insert(0, selected_data[4])
        self.destination.grid(row=1, column=1, padx=10, pady=5)

        tk.Label( self.confirmation_window, text="Date:",background="#c3ecb2").grid(row=2, column=0, padx=10, pady=5)
        self.date = tk.Entry( self.confirmation_window)
        self.date.insert(0, selected_data[1])
        self.date.grid(row=2, column=1, padx=10, pady=5)

        tk.Label( self.confirmation_window, text="Time:",background="#c3ecb2").grid(row=3, column=0, padx=10, pady=5)
        self.time = tk.Entry( self.confirmation_window)
        self.time.insert(0, selected_data[2])
        self.time.grid(row=3, column=1, padx=10, pady=5)

        tk.Label( self.confirmation_window, text="Status:",background="#c3ecb2").grid(row=4, column=0, padx=10, pady=5)
        self.status = tk.Entry( self.confirmation_window)
        self.status.insert(0, selected_data[5])
        self.status.config(state=tk.DISABLED)
        self.status.grid(row=4, column=1, padx=10, pady=5)

        # Add a confirmation button
        confirm_button = tk.Button( self.confirmation_window, text="Confirm Update",background="white",foreground="green")
        confirm_button.bind("<Button-1>", lambda event, idx=index: self.confirm_update(event, idx))
        confirm_button.grid(row=5, column=0, columnspan=2, pady=10)

    def confirm_update(self,event, index):
        print(index)
        # This method will be called when the user confirms the update
        origin = self.origin.get()
        destination = self.destination.get()
        date = self.date.get()
        time = self.time.get()
        bookingstatus = self.data[index][5]
        booking_id = self.data[index][0]

        db = BookingDatabase()
        # Update the booking in the database
        db.update_booking(date, time, origin, destination, bookingstatus, booking_id)
        db.close_connection()
        self.update_entry_widgets(index)

        messagebox.showinfo("Success", "Booking updated successfully!")
        self.update_entry_widgets(index)

        # Destroy and re-create entry frames
        for frame in self.entry_frames:
            frame.destroy()
        self.entry_frames = []
        cid = Global.customerid
        db = BookingDatabase()
        data = db.display_editbooking(cid)
        self.readData(data)


        # Close the confirmation window
        self.confirmation_window.destroy()

        # updateBooking(self.main_frame)


    def delete(self, event, index):
        db = BookingDatabase()
        booking_id = self.data[index][0]  # Get the booking_id from the data

        db.delete_booking(booking_id)


        messagebox.showinfo("Success", "Booking deleted successfully!")
        db.close_connection()

        # Destroy and re-create entry frames
        for frame in self.entry_frames:
            frame.destroy()
        self.entry_frames = []
        cid = Global.customerid
        db = BookingDatabase()
        data = db.display_editbooking(cid)
        self.readData(data)


            # Remove the deleted entry from the internal data structure




    def update_entry_widgets(self, index):
        # Update the corresponding Entry widgets with the new data
        date = self.date.get()
        time = self.time.get()
        origin = self.origin.get()
        destination = self.destination.get()
        print(date,time,origin)


        self.origin_entry.delete(index, tk.END)
        self.origin_entry.insert(index, origin)
        self.destination_entry.delete(index, tk.END)
        self.destination_entry.insert(index, destination)
        self.date_entry.delete(index, tk.END)
        self.date_entry.insert(index, date)
        self.time_entry.delete(index, tk.END)
        self.time_entry.insert(index, time)




    #
    # def destroy_entry_frame(self, index):
    #     # Destroy the entry frame at the given index
    #     if 0 <= index < len(self.entry_frames):
    #         entry_frame_to_destroy = self.entry_frames[index]
    #         entry_frame_to_destroy.destroy()
    #
    #         # Remove the destroyed entry frame from the list
    #         self.entry_frames.pop(index)
    #
    #         # Sort the entry frames based on their indices
    #         self.entry_frames.sort(key=lambda frame: int(frame.winfo_name().split("_")[-1]))
    #
    #         # Check and display label after destroying
    #         self.check_and_display_label()