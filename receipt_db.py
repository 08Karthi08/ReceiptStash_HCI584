import sqlite3
from sqlite3 import Error

class ReceiptDB:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_table(self):
        conn = self.create_connection()
        if conn is not None:
            create_table_sql = """
                CREATE TABLE IF NOT EXISTS receipts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    vendor_name TEXT,
                    date TEXT,
                    total_amount REAL
                );
            """
            self.execute_query(conn, create_table_sql)
        else:
            print("Error: Could not create a database connection.")

    def insert_receipt(self, receipt):
        conn = self.create_connection()
        if conn is not None:
            insert_receipt_sql = """
                INSERT INTO receipts (vendor_name, date, total_amount)
                VALUES (?, ?, ?);
            """
            self.execute_query(conn, insert_receipt_sql, (receipt.vendor_name, receipt.date, receipt.total_amount))
        else:
            print("Error: Could not create a database connection.")

    def get_all_receipts(self):
        conn = self.create_connection()
        if conn is not None:
            select_all_receipts_sql = """
                SELECT id, vendor_name, date, total_amount FROM receipts;
            """
            rows = self.execute_query(conn, select_all_receipts_sql)
            receipts = [Receipt(row) for row in rows]
            return receipts
        else:
            print("Error: Could not create a database connection.")

    def update_receipt(self, receipt_id, vendor_name, date, total_amount):
        conn = self.create_connection()
        if conn is not None:
            update_receipt_sql = """
                UPDATE receipts
                SET vendor_name = ?, date = ?, total_amount = ?
                WHERE id = ?;
            """
            self.execute_query(conn, update_receipt_sql, (vendor_name, date, total_amount, receipt_id))
        else:
            print("Error: Could not create a database connection.")

    def create_connection(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_file)
            return conn
        except Error as e:
            print(e)
        return conn

    def execute_query(self, conn, query, params=None):
        cursor = conn.cursor()
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        conn.commit()
        rows = cursor.fetchall()
        cursor.close()
        return rows
    
    def get_receipt(self, receipt_id):
        conn = self.create_connection()
        if conn is not None:
            select_receipt_sql = """
                SELECT * FROM receipts WHERE id = ?;
            """
            rows = self.execute_query(conn, select_receipt_sql, (receipt_id,))
            if rows:
                return Receipt(rows[0])
            else:
                return None
        else:
            print("Error: Could not create a database connection.")

    def delete_receipt(self, receipt_id):
        conn = self.create_connection()
        if conn is not None:
            delete_receipt_sql = """
                DELETE FROM receipts WHERE id = ?;
            """
            self.execute_query(conn, delete_receipt_sql, (receipt_id,))
        else:
            print("Error: Could not create a database connection.")
           
class Receipt:
    def __init__(self, data):
        self.id = data[0]
        self.vendor_name = data[1]
        self.date = data[2]
        self.total_amount = data[3]