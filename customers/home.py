import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from dbms.userdb import UserDatabase
from  dbms import  Global



class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Taxi Booking System")
        # self.root.config(background="white", width=1200, height=900)
        # self.root.resizable(height=1300, width=1000)
        root.state("zoomed")
        # Create a frame for the image
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(side=tk.LEFT, pady=0)

        # Add an image (replace "path_to_image.png" with the actual path to your image file)
        self.image_path = "../img/car1.jpg"
        self.img = Image.open(self.image_path)
        self.img = ImageTk.PhotoImage(self.img)
        self.image_label = tk.Label(self.image_frame, image=self.img)
        self.image_label.pack(side=tk.LEFT)

        # Create a frame for the login form
        self.form_frame = tk.Frame(self.root, background="#c3ecb2", width=340, height=760)
        self.form_frame.pack(side=tk.RIGHT, pady=10, fill=tk.BOTH, expand=True)

        # Create and place widgets on the form frame
        self.header_label = tk.Label(self.form_frame, text="Welcome To Taxi Service", background="#c3ecb2",
                                     foreground="red", font=("Caveat", 23, "bold"))
        self.header_label.place(x=90, y=130)

        self.username_label = tk.Label(self.form_frame, text="Username:", background="#c3ecb2", fg="red",
                                       font=("Helvetica", 16, "bold"))
        self.username_label.place(x=120, y=260)

        self.email_entry = tk.Entry(self.form_frame, width=25,
                                    font=("Helvetica", 16, "bold"))  # Set the width of the entry
        self.email_entry.place(x=120, y=300)

        self.password_label = tk.Label(self.form_frame, text="Password:", background="#c3ecb2", fg="red",
                                       font=("Helvetica", 16, "bold"))
        self.password_label.place(x=120, y=350)

        self.password_entry = tk.Entry(self.form_frame, show="*", width=25,
                                       font=("Helvetica", 16, "bold"))  # Set the width of the entry
        self.password_entry.place(x=120, y=400)

        self.toggle_button = tk.Checkbutton(self.form_frame, text="Show Password",
                                            command=self.toggle_password_visibility, background="#c3ecb2")
        self.toggle_button.place(x=320, y=360)

        self.login_button = tk.Button(self.form_frame, text="Login", command=self.validate_login, width=20, bg="red",
                                      fg="white", font=("Helvetica", 14, "bold"))
        self.login_button.place(x=150, y=470)

        self.register_label = tk.Label(self.form_frame, text="No Account? No Worries! Register for Instant Access.",
                                       background="#c3ecb2", foreground="black", font=("Helvetica", 13))
        self.register_label.place(x=80, y=660)

        self.register_button = tk.Button(self.form_frame, text="Register", width=20, bg="green", fg="white",
                                         font=("Helvetica", 14, "bold") ,command=self.register)
        self.register_button.place(x=150, y=690)

    def toggle_password_visibility(self):
        current_state = self.password_entry.cget("show")
        if current_state == "*":
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def register(self):

        self.root.destroy()

        from register import RegistrationForm

        registers = RegistrationForm(root)
        registers.mainloop()
    def validate_login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()
        db = UserDatabase()

        if email == '' or password == '':
            messagebox.showwarning("Taxi Booking System", "Please enter all the fields")
        else:
            # Call login_user on the instance
            if db.login_customer(email, password):
                customers_id = db.login_customer(email, password)
                Global.customerid = customers_id

                self.root.destroy()
                from booking import bookingDashboard
                booking = bookingDashboard(self.root)
                booking.mainloop()
            elif db.login_driver(email, password) :
                driver_id = db.login_driver(email, password)
                Global.driverid = driver_id
                self.root.destroy()
                from driver.dashboard import driverDashboard
                driver_dashboard = tk.Tk()
                driver = driverDashboard(driver_dashboard)
                driver_dashboard.mainloop()
            elif db.login_admin(email, password):
                admin_id = db.login_admin(email, password)
                Global.adminid = admin_id
                self.root.destroy()
                from admin.dashboard import adminDashboard
                admin_dashboard = tk.Tk()
                driver = adminDashboard(admin_dashboard)
                admin_dashboard.mainloop()

            else:
                messagebox.showwarning("Taxi Booking System", "Invalid email or password")

        db.close_connection()


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)

    # Run the Tkinter event loop
    root.mainloop()