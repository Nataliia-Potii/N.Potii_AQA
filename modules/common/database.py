import sqlite3


class Database():
    """
    The class Database was created to interact with the database.
    """

    def __init__(self):
        """
        The class constructor where two attributes are initialized.
        The connection allows to interract with the db.
        The cursor is an entity that can execute commands in the db.
        """
        self.connection = sqlite3.connect(
            r'C:\Users\lorel\N.Potii_AQA' + r'\become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        """
        The method executes the SQL query SELECT sqlite_version().
        After that the version of the db is shown in the terminal.
        """
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

    def get_all_users(self):
        """
        The method returns the fields values: name, address, city for all users from customers.
        """
        query = "SELECT name, address, city From customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        """
        The method has one required parameter - name.
        It returns the values of this fields from table for the user with the specific name.
        """
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        """
        The method has two mandatory parameters - product_id, qnt.
        It changes the product quantity according to the value specified in the qnt 
        for the product with specific product_id.
        """
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        """
        The method has a required parameter - product_id.
        It return the product qnt according to value in the product_id from the products table.
        """
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def insert_product(self, product_id, name, description, qnt):
        """
        The method has four mandatory parameters - product_id, name, description, qnt.
        It inserts/replace data in the table for the columns: id, name, description, quantity.
        """
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        """
        The method has one required parameter - product_id"
        It removes the product from the products table.
        """
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        """
        The method allows to collect the info about an order
        using the JOIN command and the orders, customers, products tables.
        """
        query = "SELECT orders.id, customers.name, products.name, \
                products.description \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
