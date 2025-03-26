import mysql.connector as connection


class Database:
    def __init__(self, host="localhost", user="root", password="", database="pricing"):
        try:
            # First creating a database along with establishing connection
            temp_conn = connection.connect(
                host=host,
                user=user,
                password=password
            )
            temp_cursor = temp_conn.cursor()
            temp_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
            temp_conn.close()

            # Now, connect to the database
            self.conn = connection.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.conn.cursor()

            # Create the products table
            self.create_table()

        except connection.Error as err:
            print(f"Error connecting to the database: {err}")
            self.conn = None

    def create_table(self):
        if self.conn is None:
            print("Connection is not established. Cannot create table.")
            return

        query = """
        CREATE TABLE IF NOT EXISTS products (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            base_price FLOAT,
            category VARCHAR(255)
        )
        """
        self.cursor.execute(query)
        self.conn.commit()

    def insert_product(self, name, base_price, category):
        if self.conn is None:
            print("Connection is not established. Cannot insert product.")
            return

        query = "INSERT INTO products (name, base_price, category) VALUES (%s, %s, %s)"
        self.cursor.execute(query, (name, base_price, category))
        self.conn.commit()

    def fetch_products(self):
        if self.conn is None:
            print("Connection is not established. Cannot fetch products.")
            return []

        query = "SELECT * FROM products"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def __del__(self):
        # close the connection
        if hasattr(self, 'conn') and self.conn:   # First it checks if the object (self) has an attribute named conn then closes it.
            self.conn.close()
            print("Database connection closed.")
