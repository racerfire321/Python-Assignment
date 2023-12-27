from dbms.connector import Connect
from dbms import Global
class BookingDatabase:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = Connect()

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def insert_booking(self,date,time,origin,destination,bookingstatus,customersid):
        sql = """INSERT INTO bookings (date,time,origin,destination,bookingstatus,customersid)
                 VALUES (%s, %s, %s, %s,%s,%s)"""
        values = (date,time,origin,destination,bookingstatus,customersid)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()

            # Retrieve the last inserted ID
            booking_id = cursor.lastrowid

            return booking_id
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()

    def display_booking(self, cid):
        sql = """SELECT * FROM bookings WHERE `customersid` = %s"""
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

    def display_driverbooking(self, did):
        sql = """SELECT * FROM bookings WHERE `driverid` = %s"""
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

    def display_editbooking(self, cid):
        sql = """SELECT * FROM bookings WHERE `customersid` = %s AND `bookingstatus` = "pending" """
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

    def display_viewbooking(self, did):
        sql = """SELECT * FROM bookings WHERE `driverid` = %s AND `bookingstatus` = "assigned" """
        values = (did,)  # Make sure to use parentheses to create a tuple
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            result = cursor.fetchall()
            self.conn.commit()
            print(result)
            return result

        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()
    def update_booking(self,date,time,origin,destination,bookingstatus,booking_id):
        sql = """UPDATE bookings SET date = %s,time = %s,origin = %s,destination = %s,bookingstatus = %s WHERE booking_id = %s"""
        values = (date,time,origin,destination,bookingstatus,booking_id,)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
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

    def insert_bill(self, ride_fare,bookingid):
        vat = 13
        discount = 0
        ride_fare = float(ride_fare)
        total_amount = ride_fare + (vat / 100 * 13) + discount

        sql = """INSERT INTO bills (ride_fare, vat, discount, total_amount,bookingid)
                 VALUES (%s, %s, %s, %s,%s)"""

        values = (ride_fare, vat, discount, total_amount,bookingid)

        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
            print("Bill inserted successfully!")
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()

    def display_bill(self, bookingid):
        sql = """SELECT * FROM bills WHERE `bookingid` = %s"""
        values = (bookingid,)  # Make sure to use parentheses to create a tuple
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
    def reject_booking(self,bookingstatus, booking_id ):
        sql = """UPDATE bookings SET bookingstatus = %s ,driverid = NULL WHERE booking_id = %s"""
        values = (bookingstatus,booking_id,)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()

    def completed_booking(self, bookingstatus, booking_id):
        sql = """UPDATE bookings SET bookingstatus = %s  WHERE booking_id = %s"""
        values = (bookingstatus, booking_id,)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()