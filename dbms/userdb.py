from dbms.connector import Connect

class UserDatabase:
    def __init__(self):
        self.conn = None

    def connect(self):
        self.conn = Connect()

    def close_connection(self):
        if self.conn:
            self.conn.close()

    def insert_customers(self, full_name, dob, phone_number, gender, user_type, email, password,payment_method,creditcard_No):
        sql = """INSERT INTO customers (full_name, dob, phone_number, gender, user_type, email, password,payment_method,creditcard_No)
                 VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s 
                 )"""
        values = (full_name, dob, phone_number, gender, user_type, email, password,payment_method,creditcard_No)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()
    def update_customers(self, full_name, dob, phone_number, gender, user_type, email, password,payment_method,creditcard_No):
        sql = """UPDATE INTO customers (full_name, dob, phone_number, gender, user_type, email, password,payment_method,creditcard_No)
                 VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s)"""
        values = (full_name, dob, phone_number, gender, user_type, email, password,payment_method,creditcard_No)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()

    def insert_drivers(self, full_name, dob, phone_number, gender, user_type, email, license_number, vehicle_number, password):
        sql = """INSERT INTO driver (full_name, dob, phone_number, gender, user_type, email, license_number, vehicle_number, password)
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (full_name, dob, phone_number, gender, user_type, email, license_number, vehicle_number, password)
        try:
            self.connect()
            cursor = self.conn.cursor()
            cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print("Error:", e)
        finally:
            self.close_connection()
        

    def search_user(self, email,password ):
        sql = "SELECT * FROM customers WHERE password = %s OR email = %s  OR EXISTS (SELECT * FROM driver WHERE password = %s OR email = %s )"
        values = ( email,password, email,password)
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
    def login_customer(self, email, password):
     sql = " SELECT customer_id FROM customers WHERE password = %s AND email = %s"
     values = (password,email)
     try:
         self.connect()
         cursor = self.conn.cursor()
         cursor.execute(sql, values)
         result = cursor.fetchone()
         self.conn.commit()
         if result:
             customer_id = result[0]
             return customer_id
         else:
             print("No matching customer found.")
             return None
     except Exception as e:
        print("Error:", e)
        return False
     finally:
        self.close_connection()

    def login_driver(self, email, password):
     sql = "SELECT driver_id FROM driver WHERE password = %s AND email = %s"
     values = ( password,email)
     try:
         self.connect()
         cursor = self.conn.cursor()
         cursor.execute(sql, values)
         result = cursor.fetchone()
         self.conn.commit()
         if result:
             driver_id = result[0]
             return driver_id
         else:
             print("No matching customer found.")
             return None
     except Exception as e:
        print("Error:", e)
        return False
     finally:
        self.close_connection()


    def login_admin(self, email, password):
     sql = "SELECT admin_id FROM admin WHERE password = %s AND email = %s"
     values = ( password,email)
     try:
         self.connect()
         cursor = self.conn.cursor()
         cursor.execute(sql, values)
         result = cursor.fetchone()
         self.conn.commit()
         if result:
             admin_id = result[0]
             return admin_id
         else:
             print("No matching customer found.")
             return None
     except Exception as e:
        print("Error:", e)
        return False
     finally:
        self.close_connection()
