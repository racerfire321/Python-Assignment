from dbms.connector import Connect
from dbms import Global

class UpdateDatabase:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = Connect()

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def update_customer(self, full_name, dob, phone_number, gender, email, password, customer_id):
        sql = """UPDATE customers SET full_name=%s, dob=%s, phone_number=%s, gender=%s, email=%s, password=%s WHERE customer_id=%s"""
        values = (full_name, dob, phone_number, gender, email, password, customer_id)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            # Commit the changes to the database
            self.conn.commit()
            return True
        except Exception as e:
            print("Error:", e)
            return False
        finally:
            self.close_connection()

    def get_customerdetails(self, cid):
        sql = """SELECT * FROM customers WHERE `customer_id` = %s"""
        values = (cid,)  # Make sure to use parentheses to create a tuple
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            result = cursor.fetchall()
            self.conn.commit()
            return result

        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()

    def update_driver(self, full_name, dob, phone_number, gender, email, password, driver_id):
        sql = """UPDATE driver SET full_name=%s, dob=%s, phone_number=%s, gender=%s, email=%s,password=%s WHERE driver_id=%s"""
        values = (full_name, dob, phone_number, gender, email, password, driver_id)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            result = cursor.fetchone()
            return result is not None
        except Exception as e:
            print("Error:", e)
            return False
        finally:
            self.close_connection()

    def get_driverdetails(self, did):
        sql = """SELECT * FROM driver WHERE `driver_id` = %s"""
        values = (did,)  # Make sure to use parentheses to create a tuple
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            result = cursor.fetchall()
            self.conn.commit()
            return result

        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()
 #
 # def update_profile(self):
 #    # Disable Entry widgets and Update Profile button
 #    for entry_widget in self.entries:
 #        entry_widget.set("")
 #        entry_widget.widget.config(state=tk.DISABLED)
 #
 #    # Disable Update Profile button
 #    self.root.nametowidget(self.root.winfo_parent()).nametowidget(".").children["!frame"].children["!button"].config(
 #        state=tk.DISABLED)
 #
 #    try:
 #        update_query = f"UPDATE {self.user_type}s SET full_name=?, dob=?, phone_number=?, gender=?, email=?"
 #        if self.user_type == "driver":
 #            update_query += ", license_number=?, vehicle_number=?"
 #
 #        update_query += " WHERE id = ?"
 #
 #        self.cursor.execute(update_query, tuple([entry.get() for entry in self.entries] + [self.user_id]))
 #        self.conn.commit()
 #        messagebox.showinfo("Update Profile", "Profile updated successfully!")
 #    except Exception as e:
 #        messagebox.showerror("Error", f"Error updating profile: {str(e)}")
