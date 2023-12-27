import sqlite3
import tkinter as tk

from PIL import Image, ImageTk

from component.bill import DisplayBill
from component.profile import Profile
from component.viewbooking import viewBooking
from component.ridehistory import RideHistory
from dbms.bookingdb import BookingDatabase
from dbms.updateuser import UpdateDatabase
from dbms import Global


class driverDashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x750+60+20")
        self.root.title("Taxi Booking System")
        root.state("zoomed")
        # Create the main frame
        self.main_frame = tk.Frame(root, bg="white")
        self.main_frame.place(x=301, y=0, width=1300, height=900)

        # Create the right sidebar frame
        self.sidebar_frame = tk.Frame(root, bg="white", width=300)
        self.sidebar_frame.place(x=0, y=0, height=900)

        self.menubar = tk.Frame(self.sidebar_frame, bg="white", width=300)
        self.menubar.place(x=0, y=260, height=900)  # Adjust y-coordinate to place below the user image

        self.image_frame1 = tk.Frame(self.main_frame)
        self.image_frame1.place(x=50, y=40)

        # Add an image (replace "path_to_image.png" with the actual path to your image file)
        self.image_path = "../img/taxi.jpg"
        self.img1 = Image.open(self.image_path)
        self.img1 = self.img1.resize((1100, 750))
        self.img1 = ImageTk.PhotoImage(self.img1)
        self.image_label1 = tk.Label(self.image_frame1, image=self.img1)
        self.image_label1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.label = tk.Label(
            self.main_frame,
            text=("Welcome to our Taxi Reservation Service"
                  ",where comfort meets personalized navigation! "
                  "Embark on a stress-free travel with our"
                  "user-friendly software, which includes"
                  " integrated maps.fun and stress-free."
                  " Welcome to our service, where your "
                  "comfort and convenience come first!"),
            font=("Helvetica", 16, "bold"),
            justify=tk.LEFT,
            wraplength=460,
            pady=10,
            padx=10,
            background="white",
            highlightthickness=0,
            bd=5

        )
        self.label.place(x=50, y=530)

        self.image_frame = tk.Frame(self.sidebar_frame)
        self.image_frame.place(x=0,y=0)

        # Add an image (replace "path_to_image.png" with the actual path to your image file)
        self.image_path = "../img/driver.jpg"
        self.img = Image.open(self.image_path)
        self.img = self.img.resize((320, 230))
        self.img = ImageTk.PhotoImage(self.img)
        self.image_label = tk.Label(self.image_frame, image=self.img)
        self.image_label.pack(side=tk.LEFT)

        # Sidebar options
        options = ["👨🏻‍💼Profile", "📝View Booking",  "💵Billing", "📜Ride History", "🔓SignOut"]
        for option in options:
            option_button = tk.Button(self.menubar, text=option, width=15, font=("Helvetica", 18, "bold"),
                                      bg="#c3ecb2", fg="black", command=lambda o=option: self.display_option(o))
            option_button.pack(pady=25, padx=25)  # Adjust y-coordinate to start from 0

        # Initialize a list to store booking instances
        self.bookings = []

    def display_option(self, option):
        # Clear previous content from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()

        if option == "📝View Booking":
            did = Global.driverid
            db = BookingDatabase()
            data = db.display_viewbooking(did)
            viewBooking(self.main_frame,data)


        elif option == "📜Ride History":
            did = Global.driverid
            db = BookingDatabase()
            ridehistory_data = db.display_driverbooking(did)

            RideHistory(self.main_frame, ridehistory_data)
        elif option == "👨🏻‍💼Profile":
            did = Global.driverid
            db = UpdateDatabase()
            datas = db.get_driverdetails(did)
            if datas:
                data = list(datas[0])
                print(data)
                Profile(self.main_frame, data)
            else:
                print("No data found for the driver ID:", did)

            Profile(self.main_frame, data)

        elif option == "💵Billing":
            did = Global.driverid
            db = BookingDatabase()
            data = db.display_driverbooking(did)


            DisplayBill(self.main_frame, data)
        elif option == "🔓SignOut":

            Global.driverid = None

            self.root.destroy()

            from customers.home import Login
            login_root = tk.Tk()
            login = Login(login_root)
            login_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = driverDashboard(root)

    # Run the Tkinter event loop
    root.mainloop()