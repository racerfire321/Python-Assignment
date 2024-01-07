import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from dbms.userdb import UserDatabase
from dbms import Global

class Login:
    def __init__(self, root):
        # Initialize the login window
        self.root = root
        self.root.title("Taxi Booking System")
        root.state("zoomed")

        # Create a frame for the image
        self.image_frame = tk.Frame(self.root)
        self.image_frame.pack(side=tk.LEFT, pady=0)

        # Add an image
        # Replace "path_to_image.png" with the actual path to your image file
        self.image_path = "../img/car1.jpg"
        self.img = Image.open(self.image_path)
        self.img = ImageTk.PhotoImage(self.img)
        self.image_label = tk.Label(self.image_frame, image=self.img)
        self.image_label.pack(side=tk.LEFT)

        # Web label
        self.web_label = tk.Label(self.image_frame, text="www.Cabity.com", background="white",
                                     foreground="black", font=("Helvetica", 24, "bold", "underline"))
        self.web_label.place(x=300, y=660)

        # Create a frame for the login form
        self.form_frame = tk.Frame(self.root, background="#c3ecb2", width=340, height=760)
        self.form_frame.pack(side=tk.RIGHT, pady=10, fill=tk.BOTH, expand=True)

        # Create and place widgets on the form frame
        self.header_label = tk.Label(self.form_frame, text="Welcome to", background="#c3ecb2",
                                     foreground="red", font=("Times New Roman", 28, "bold"))
        self.header_label.place(x=70, y=100)

        # Additional label for the app name
        self.app_name_label = tk.Label(self.form_frame, text="🚗Cabity", background="#E0F8E0",
                                       foreground="green", font=("Times New Roman", 32, "bold"))
        self.app_name_label.place(x=270, y=97)

        # Slogan label
        self.slogan_label = tk.Label(self.form_frame, text="Your Portal to Smooth Travels!", background="#c3ecb2",
                                     foreground="black", font=("Helvetica", 14, "bold"))
        self.slogan_label.place(x=120, y=160)

        # Username and email entry
        self.username_label = tk.Label(self.form_frame, text="Email:", background="#c3ecb2", fg="red",
                                       font=("Helvetica", 18, "bold"))
        self.username_label.place(x=100, y=260)
        self.email_entry = tk.Entry(self.form_frame, width=25,
                                    font=("Helvetica", 18, "bold"), highlightcolor="green", highlightthickness=3)
        self.email_entry.place(x=100, y=310)

        # Password entry
        self.password_label = tk.Label(self.form_frame, text="Password:", background="#c3ecb2", fg="red",
                                       font=("Helvetica", 18, "bold"))
        self.password_label.place(x=100, y=360)
        self.password_entry = tk.Entry(self.form_frame, show="*", width=25,
                                       font=("Helvetica", 18, "bold"), highlightcolor="green", highlightthickness=3)
        self.password_entry.place(x=100, y=410)

        # Toggle button for showing/hiding password
        self.toggle_button = tk.Checkbutton(self.form_frame, text="Show Password",
                                            command=self.toggle_password_visibility, background="#c3ecb2")
        self.toggle_button.place(x=320, y=370)

        # Forget password label
        self.forget_button = tk.Label(self.form_frame, text="Forget Password?", background="#c3ecb2")
        self.forget_button.place(x=320, y=460)
        self.forget_button.config(font=("Arial", 12, "underline"), cursor="hand2")

        # Login button
        self.login_button = tk.Button(self.form_frame, text="Login", command=self.validate_login, width=17, bg="red",
                                      fg="white", font=("Helvetica", 16, "bold"))
        self.login_button.place(x=150, y=500)

        # Registration section
        self.register_label = tk.Label(self.form_frame, text="No Account? No Worries! Register for Instant Access.",
                                       background="#c3ecb2", foreground="black", font=("Helvetica", 13))
        self.register_label.place(x=80, y=660)
        self.register_button = tk.Button(self.form_frame, text="Register", width=17, bg="green", fg="white",
                                         font=("Helvetica", 16, "bold"), command=self.register)
        self.register_button.place(x=150, y=690)

    def toggle_password_visibility(self):
        # Toggle the visibility of the password
        current_state = self.password_entry.cget("show")
        if current_state == "*":
            self.password_entry.configure(show="")
        else:
            self.password_entry.configure(show="*")

    def register(self):
        # Destroy current window and open the registration window
        self.root.destroy()
        from register import RegistrationForm
        register_window = tk.Tk()
        RegistrationForm(register_window)
        register_window.mainloop()

    def validate_login(self):
        # Validate user login
        email = self.email_entry.get()
        password = self.password_entry.get()
        db = UserDatabase()

        if email == '' or password == '':
            messagebox.showwarning("Taxi Booking System", "Please enter all the fields")
        else:
            # Attempt to login based on user type (customer, driver, admin)
            if db.login_customer(email, password):
                messagebox.showinfo("Taxi Booking System", "Welcome to the taxi booking system")
                customers_id = db.login_customer(email, password)
                Global.customerid = customers_id
                self.root.destroy()
                from booking import bookingDashboard
                booking_window = tk.Tk()
                bookingDashboard(booking_window)
                booking_window.mainloop()

            elif db.login_driver(email, password):
                driver_id = db.login_driver(email, password)
                Global.driverid = driver_id
                self.root.destroy()
                from driver.dashboard import driverDashboard
                driver_dashboard = tk.Tk()
                driver = driverDashboard(driver_dashboard)
                messagebox.showinfo("Taxi Booking System", "Welcome to the taxi booking system")
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

# Main program execution
if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
