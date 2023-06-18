import sqlite3

class Receipt:
    def __init__(self, receipt):
        self.receipt = receipt

class ReceiptDB:
    def __init__(self, db_path):
        self.db_path = db_path

    def create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS receipts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    image_path TEXT NOT NULL,
                    vendor_name TEXT,
                    date TEXT,
                    total_amount REAL
                )
            ''')
            conn.commit()

    def insert_receipt(self, receipt):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO receipts (image_path, vendor_name, date, total_amount) VALUES (?, ?, ?, ?)", 
                           (receipt.receipt['image_path'], receipt.receipt['vendor_name'], 
                            receipt.receipt['date'], receipt.receipt['total_amount']))
            conn.commit()

    def get_all_receipts(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM receipts")
            return cursor.fetchall()