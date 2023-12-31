
import tkinter as tk

from PIL import Image, ImageTk
from component.bill import DisplayBill
from component.profile import Profile
from component.updatebooking import updateBooking
from component.ridehistory import RideHistory
from dbms.bookingdb import BookingDatabase
from dbms.updateuser import UpdateDatabase
from dbms import Global


class Dashboard:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1400x750+60+20")
        self.root.title("Taxi Booking System")
        root.state("zoomed")
        # Create the main frame
        self.main_frame = tk.Frame(root, bg="white")
        self.main_frame.place(x=301,y=0,width=1300,height=900)

        # Create the right sidebar frame
        self.sidebar_frame = tk.Frame(root, bg="white", width=300)
        self.sidebar_frame.place(x=0, y=0, height=900)

        self.menubar = tk.Frame(self.sidebar_frame, bg="white", width=300)
        self.menubar.place(x=0, y=260,height=900)  # Adjust y-coordinate to place below the user image

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
        #
        self.image_frame = tk.Frame(self.sidebar_frame)
        self.image_frame.place(x=9,y=29)

        # Add an image (replace "path_to_image.png" with the actual path to your image file)
        self.image_path = "../img/userr.png"
        self.img = Image.open(self.image_path)
        self.img = self.img.resize((280, 230))
        self.img = ImageTk.PhotoImage(self.img)
        self.image_label = tk.Label(self.image_frame, image=self.img)
        self.image_label.pack(side=tk.LEFT)

        self.back_button = tk.Button(self.sidebar_frame, text="<Back to Booking", width=15,height=1, font=("Helvetica", 12, "bold"),
                                     bg="black", fg="#c3ecb2", command=self.makeBooking)
        self.back_button.place(x=10,y=20)

        # Sidebar options
        options = ["👨🏻‍💼Profile", "📝Edit Booking",  "💵Billing", "📜Ride History", "🔓SignOut"]
        for option in options:
            option_button = tk.Button(self.menubar, text=option, width=15, font=("Helvetica", 18, "bold"),
                                      bg="#c3ecb2", fg="black", command=lambda o=option: self.display_option(o)
                                    )
            option_button.pack(pady=25, padx=25)  # Adjust y-coordinate to start from 0

        # Initialize a list to store booking instances
        self.bookings = []


    def display_option(self, option):
        # Clear previous content from the main frame
        # Clear previous content from the main frame
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.cid = Global.customerid

        if option == "📝Edit Booking":

            db = BookingDatabase()
            data = db.display_editbooking(self.cid)
            updateBooking(self.main_frame, data)
        elif option == "📜Ride History":
            db = BookingDatabase()
            ride_data = db.display_booking(self.cid)

            RideHistory(self.main_frame, ride_data)

        elif option == "👨🏻‍💼Profile":
            db = UpdateDatabase()
            datas = db.get_customerdetails(self.cid)
            if datas:
                data = list(datas[0])
                Profile(self.main_frame, data)

        elif option == "💵Billing":
            db = BookingDatabase()
            data = db.display_booking(self.cid)

            DisplayBill(self.main_frame, data)


        elif option == "🔓SignOut":
            cid = None
            did = None

            self.root.destroy()

            from customers.home import Login
            login_root = tk.Tk()
            login = Login(login_root)
            login_root.mainloop()
    def makeBooking(self):

        self.root.destroy()
        from booking import bookingDashboard
        booking_window = tk.Tk()
        bookingDashboard(booking_window)
        booking_window.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = Dashboard(root)

    # Run the Tkinter event loop
    root.mainloop()