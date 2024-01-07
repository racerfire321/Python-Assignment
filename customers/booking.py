import re
import tkinter as tk
from tkinter import ttk, simpledialog
from tkinter import messagebox
from tkintermapview import TkinterMapView
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from tkcalendar import DateEntry

from dbms.bookingdb import BookingDatabase
from dbms import Global


class bookingDashboard:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title("Taxi Booking System")

        self.origin_marker_id = None
        self.destination_marker_id = None
        self.path = None

        # root.geometry("1200x900")
        self.map_widget = TkinterMapView(root, width=600, height=400, corner_radius=0)
        self.map_widget.pack(fill="both", expand=True)
        map =self.map_widget.set_tile_server("https://mt0.google.com/vt/lyrs=m&hl=en&x={x}&y={y}&z={z}&s=Ga", max_zoom=22)
        self.map = map
        self.entry_frame = tk.Canvas(root, background="#c3ecb2", width=430, height=280)
        self.entry_frame.place(x=600, y=500)

        # Entry widgets for origin, destination, and time
        self.origin_label = tk.Label(self.entry_frame, text="Pickup", background="#c3ecb2", fg="dark green",
                                     font=("Helvetica", 14, "bold"))
        self.origin_label.place(x=30, y=100)
        self.origin_entry = tk.Entry(self.entry_frame, bg="white",font=("Helvetica", 14, "bold"),highlightcolor="green",highlightthickness=3)  # Set the background color to white
        self.origin_entry.place(x=150, y=100)

        self.destination_label = tk.Label(self.entry_frame, text="Destination", background="#c3ecb2",
                                          fg="dark green", font=("Helvetica", 14, "bold"))
        self.destination_label.place(x=30, y=150)
        self.destination_entry = tk.Entry(self.entry_frame, bg="white",font=("Helvetica", 14, "bold"),highlightcolor="green",highlightthickness=3)  # Set the background color to white
        self.destination_entry.place(x=150, y=150)

        self.date_label = tk.Label(self.entry_frame, text="Pickup Date", background="#c3ecb2",
                                   fg="dark green", font=("Helvetica", 14, "bold"))
        self.date_label.place(x=30, y=40)
        self.date_entry = DateEntry(self.entry_frame, bg="black",font=("Helvetica", 14, "bold"),highlightcolor="green",highlightthickness=3, width=7, height=10)
        self.date_entry.place(x=150, y=40)

        # Time entry
        self.time_label = tk.Label(self.entry_frame, text="Time", background="#c3ecb2",
                                   fg="dark green", font=("Helvetica", 14, "bold"))
        self.time_label.place(x=259, y=40)
        self.time_entry = tk.Entry(self.entry_frame, bg="white", width=2, font=("Helvetica", 14, "bold"),
                                   highlightcolor="green", highlightthickness=3)
        self.time_entry.place(x=309, y=40)
        self.label = tk.Label(self.entry_frame, text=":", background="#c3ecb2",
                                  fg="dark green", font=("Helvetica", 15, "bold"))
        self.label.place(x=333, y=40)
        self.time_entry1 = tk.Entry(self.entry_frame, bg="white", width=2, font=("Helvetica", 14, "bold"),
                                   highlightcolor="green", highlightthickness=3)
        self.time_entry1.place(x=349, y=40)
        self.time_types = ["AM", "PM"]
        self.var_time_type = tk.StringVar()
        self.user_time_combobox = ttk.Combobox(self.entry_frame, textvariable=self.var_time_type, values=self.time_types,width=3)
        self.user_time_combobox.place(x=384, y=47)

        # Button to trigger setting address, time, and calculating distance
        self.book_taxi_button = tk.Button(self.entry_frame, text="Book Taxi", command=self.book_taxi,
                                          bg="green", foreground="white", font=("Helvetica", 14, "bold"))
        self.book_taxi_button.place(x=300, y=230)

        # Button to reset entries
        self.reset_button = tk.Button(self.entry_frame, text="Reset", command=self.reset_entries,
                                      bg="red", foreground="white", font=("Helvetica", 14, "bold"))
        self.reset_button.place(x=50, y=230)

        self.menu = tk.Label(self.map_widget, text="👤☰", bg="green", foreground="white", font=("Helvetica", 30, "bold"))
        self.menu.place(x=self.map_widget.winfo_width() + 1400, y=20)
        self.menu.bind("<Button-1>", lambda event: self.openmenu())
        # Label to display distance
        self.distance_label = tk.Label(self.entry_frame, text="", bg="#c3ecb2")
        self.distance_label.place(x=30, y=200)
        self.amount_label = tk.Label(self.entry_frame, text="", bg="#c3ecb2")
        self.amount_label.place(x=230, y=200)

    # def menuOpen(self):
    #     Dashboard()


    def book_taxi(self):
        # Disable entry fields

        self.origin_entry.config(state=tk.DISABLED)
        self.destination_entry.config(state=tk.DISABLED)
        self.date_entry.config(state=tk.DISABLED)
        self.time_entry.config(state=tk.DISABLED)
        self.time_entry1.config(state=tk.DISABLED)
        # Disable Book Taxi button
        self.book_taxi_button.config(state=tk.DISABLED)

        # Set addresses and markers on the map
        self.origin_marker_id = self.map_widget.set_address(self.origin_entry.get(), marker=True, text="Origin")
        self.destination_marker_id = self.map_widget.set_address(self.destination_entry.get(), marker=True,
                                                                 text="Destination")

        # Add a polyline (line) between origin and destination
        self.add_path_between_points()
        # Calculate and display the distance between origin and destination
        distance = self.calculate_distance(self.origin_entry.get(), self.destination_entry.get())
        self.distance_label.config(text=f"Distance: {distance} km")

        amount = self.calculate_price(self.origin_entry.get(), self.destination_entry.get())
        self.amount_label.config(text=f"TotalPrice: {amount} km")

        # Open confirmation popup
        self.open_confirmation_popup(
            self.origin_entry.get(), self.destination_entry.get(), distance, amount,
            self.date_entry.get(), self.time_entry.get(), self.time_entry1.get(), self.var_time_type.get()
        )

    def reset_entries(self):
        # Enable entry fields
        self.origin_entry.config(state=tk.NORMAL)
        self.destination_entry.config(state=tk.NORMAL)
        self.date_entry.config(state=tk.NORMAL)
        self.time_entry.config(state=tk.NORMAL)
        self.time_entry1.config(state=tk.NORMAL)

        # Clear entry fields
        self.origin_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.time_entry1.delete(0, tk.END)



        # Enable Book Taxi button
        self.book_taxi_button.config(state=tk.NORMAL)


        # Clear distance label
        self.distance_label.config(text="")
        self.amount_label.config(text="")

        # Clear markers on the map
        if self.origin_marker_id:
            self.map_widget.delete(self.origin_marker_id)
            self.origin_marker_id = None

        if self.destination_marker_id:
            self.map_widget.delete(self.destination_marker_id)
            self.destination_marker_id = None
        self.map_widget.delete(self.path)


    def add_path_between_points(self):
        # Get coordinates for origin and destination
        self.origin_coords = self.get_coordinates(self.origin_entry.get())
        self.destination_coords = self.get_coordinates(self.destination_entry.get())

        if self.origin_coords and self.destination_coords:
            # Set path on the map
            path_coordinates = [self.origin_coords, self.destination_coords]
            self.path =self.map_widget.set_path(path_coordinates)

            # Add a polyline (line) between origin and destination
            self.create_path_between_points(self.origin_coords, self.destination_coords)  # Rename the method here
        else:
            print("Error: Unable to create line - invalid coordinates")

    def create_path_between_points(self, origin_coords, destination_coords):
        # Add a polyline (line) between origin and destination
        self.map_widget.canvas.create_line(
            origin_coords[0], origin_coords[1], destination_coords[0], destination_coords[1],
            fill="blue", width=2
        )
        # Force an immediate update of the canvas
        self.map_widget.update()

    def calculate_distance(self, origin, destination):
        origin_coords = self.get_coordinates(origin)
        destination_coords = self.get_coordinates(destination)
        distance = geodesic(origin_coords, destination_coords).kilometers
        return round(distance, 2)

    def calculate_price(self, origin, destination):
        distance = self.calculate_distance(origin, destination)
        ride = 1.25
        amount = round(distance * ride, 2)
        return amount

    def get_coordinates(self, address):
        geolocator = Nominatim(user_agent="your_app_name")  # Replace with your actual app name
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            return None

    def open_confirmation_popup(self, origin, destination, distance, amount, date, time,time2,time3):
        if origin == "":
            messagebox.showwarning("Taxi Booking System", "Please enter origin correctly!")
        elif destination == "":
            messagebox.showwarning("Taxi Booking System", "Please enter destination correctly!")
        elif date == "":
            messagebox.showwarning("Taxi Booking System", "Please enter date correctly!")
        elif time == "":
            messagebox.showwarning("Taxi Booking System", "Please enter time Hour correctly!")
        elif time2 == "":
            messagebox.showwarning("Taxi Booking System", "Please enter Minutes in time correctly!")
        elif time3 == "":
            messagebox.showwarning("Taxi Booking System", "Please select AM/PM in time correctly!")
        else:
            confirmation_window = tk.Toplevel(self.entry_frame.winfo_toplevel(), bg="#c3ecb2")
            confirmation_window.title("Booking Confirmation")
            confirmation_window.resizable(False, False)

            # Hide window decorations (minimize, maximize, close buttons)
            confirmation_window.overrideredirect(True)

            # Set the size and position of the confirmation window
            window_width = self.entry_frame.winfo_reqwidth()
            window_height = self.entry_frame.winfo_reqheight()
            x = self.entry_frame.winfo_x()
            y = self.entry_frame.winfo_y()

            confirmation_window.geometry(f"{window_width}x{window_height}+{x+4}+{y + 19}")


            # Display confirmation details using a table
            columns = ["Attribute", "Values"]
            tree = ttk.Treeview(confirmation_window, columns=columns, show="headings", height=6)

            for col in columns:
                tree.heading(col, text=col)
            tree.pack(pady=20)

            data = [
                ("Origin", origin),
                ("Destination", destination),
                ("Date", date),
                ("Time", time+":"+time2+time3),
                ("Distance (km)", f"{distance:.2f}km"),
                ("Total Price ($)", f"{amount}$"),
            ]

            for row in data:
                tree.insert("", "end", values=row)

            # Button to close the confirmation popup and reset values
            confirm_button = tk.Button(
                confirmation_window,
                text="Confirm Booking",
                command=lambda: self.confirm_booking(confirmation_window),
                bg="green",
                fg="white",
                width=15,
                font=("Helvetica", 12, "bold")
            )
            confirm_button.pack(side="left", pady=5,padx=10)
            cancel_button = tk.Button(
                confirmation_window,
                text="Cancel",
                command=lambda: self.cancel_booking(confirmation_window),
                bg="red",
                fg="white",
                width=10,
                font=("Helvetica", 12, "bold")
            )
            cancel_button.pack(side="right", padx=10)

    def cancel_booking(self, confirmation_window):
        confirmation_window.destroy()

    def openmenu(self):
        self.root.destroy()
        from dashboard import Dashboard

        menu_window = tk.Tk()
        dashboard = Dashboard(menu_window)
        menu_window.mainloop()

    def confirm_booking(self, confirmation_window):
        ride_fare_text = self.amount_label.cget("text")
        numeric_part = re.search(r"\d+\.\d+", ride_fare_text)
        if numeric_part:
            ride_fare = float(numeric_part.group())
        else:
            ride_fare = 0.0
        date = self.date_entry.get_date()
        time = self.time_entry.get() + ":" + self.time_entry1.get() + self.var_time_type.get()
        origin = self.origin_entry.get()
        destination = self.destination_entry.get()
        bookingstatus = "pending"
        customersid = Global.customerid

        db = BookingDatabase()

        bookingid = db.insert_booking(date, time, origin, destination, bookingstatus, customersid)

        print(bookingid)
        db.insert_bill(ride_fare, bookingid)

        self.reset_entries()
        # Close the confirmation window
        confirmation_window.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = bookingDashboard(root)
    root.mainloop()