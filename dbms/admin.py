from dbms.connector import Connect

class AdminDatabase:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = Connect()

    def close_connection(self):
        if self.conn:
            self.conn.close()



    def bookingTable(self):
        sql = """SELECT * FROM bookings """
        values = ()  # Make sure to use parentheses to create a tuple
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

    def customerTable(self):
        sql = """SELECT * FROM customers """
        values = ()  # Make sure to use parentheses to create a tuple
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
    def driverTable(self):
        sql = """SELECT * FROM driver """
        values = ()  # Make sure to use parentheses to create a tuple
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

    def availableDriver(self):
        sql = """SELECT driver_id FROM driver WHERE driver_id NOT IN ( SELECT driverid FROM bookings WHERE bookingstatus = 'assigned' ) """
        values = ()  # Make sure to use parentheses to create a tuple
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

    # def display_editbooking(self, cid):
    #     sql = """SELECT * FROM bookings WHERE `customersid` = %s AND `bookingstatus` = "pending" """
    #     values = (cid,)  # Make sure to use parentheses to create a tuple
    #     try:
    #         self.connect()
    #         cursor = self.conn.cursor()
    #         cursor.execute(sql, values)
    #         result = cursor.fetchall()
    #         self.conn.commit()
    #         print(result)
    #         return result
    #
    #     except Exception as e:
    #         print("Error:", e)
    #     finally:
    #         self.close_connection()
    #
    # def display_viewbooking(self, did):
    #     sql = """SELECT * FROM bookings WHERE `driverid` = %s AND `bookingstatus` = "assigned" """
    #     values = (did,)  # Make sure to use parentheses to create a tuple
    #     try:
    #         self.connect()
    #         cursor = self.conn.cursor()
    #         cursor.execute(sql, values)
    #         result = cursor.fetchall()
    #         self.conn.commit()
    #         print(result)
    #         return result
    #
    #     except Exception as e:
    #         print("Error:", e)
    #     finally:
    #         self.close_connection()
    def updatebooking(self, booking_id, date, time, origin, destination, bookingstatus, customersid, driverid, adminid):
        print(
            f"Updating booking: {booking_id} - {date}, {time}, {origin}, {destination}, {bookingstatus}, {driverid}, {adminid}")

        sql = """UPDATE bookings SET date = %s, time = %s, origin = %s, destination = %s, bookingstatus = %s, 
                 customersid = %s, driverid = %s, adminid = %s WHERE booking_id = %s"""
        values = (date, time, origin, destination, bookingstatus, customersid, driverid, adminid, booking_id)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()  # Commit the changes to the database
            print("Booking updated successfully.")
            return True

        except Exception as e:
            print("Error during update:", e)
            self.conn.rollback()
            return False

        finally:
            self.close_connection()

    def delete_booking(self, booking_id):
        sql = "DELETE FROM `bookings` WHERE booking_id = %s"
        values = (booking_id,)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()

    def updateCustomer(self, customer_id, full_name, dob, phone_number, gender, email, password):
        sql = """UPDATE customers SET full_name=%s, dob=%s, phone_number=%s, gender=%s, email=%s, password=%s WHERE customer_id=%s"""
        values = (full_name, dob, phone_number, gender, email, password, customer_id)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()  # Commit the changes to the database
            print("Customer updated successfully.")
            return True

        except Exception as e:
            print("Error during update:", e)
            self.conn.rollback()
            return False

        finally:
            self.close_connection()

    def delete_customer(self, customer_id):
        sql = "DELETE FROM `customers` WHERE customer_id = %s"
        values = (customer_id,)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()

    def updateDriver(self, driver_id, full_name, dob, phone_number, gender, email, password):
        sql = """UPDATE driver SET full_name=%s, dob=%s, phone_number=%s, gender=%s, email=%s, password=%s WHERE driver_id=%s"""
        values = (full_name, dob, phone_number, gender, email, password, driver_id)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()  # Commit the changes to the database
            print("Driver updated successfully.")
            return True

        except Exception as e:
            print("Error during update:", e)
            self.conn.rollback()
            return False

        finally:
            self.close_connection()

    def delete_driver(self, driver_id):
        sql = "DELETE FROM `driver` WHERE driver_id = %s"
        values = (driver_id,)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()