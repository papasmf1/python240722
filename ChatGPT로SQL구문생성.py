import sqlite3
import random
import string

class ProductDatabase:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL
        )
        ''')
        self.conn.commit()

    def insert_product(self, name, price):
        self.cursor.execute('''
        INSERT INTO products (name, price) VALUES (?, ?)
        ''', (name, price))
        self.conn.commit()

    def update_product(self, product_id, name=None, price=None):
        if name:
            self.cursor.execute('''
            UPDATE products SET name = ? WHERE id = ?
            ''', (name, product_id))
        if price is not None:
            self.cursor.execute('''
            UPDATE products SET price = ? WHERE id = ?
            ''', (price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
        DELETE FROM products WHERE id = ?
        ''', (product_id,))
        self.conn.commit()

    def select_product(self, product_id):
        self.cursor.execute('''
        SELECT * FROM products WHERE id = ?
        ''', (product_id,))
        return self.cursor.fetchone()

    def select_all_products(self):
        self.cursor.execute('''
        SELECT * FROM products
        ''')
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

    def generate_sample_data(self, num_samples=100):
        for _ in range(num_samples):
            name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
            price = round(random.uniform(10, 1000), 2)
            self.insert_product(name, price)

# 사용 예시
if __name__ == "__main__":
    db = ProductDatabase()
    db.generate_sample_data()

    # 데이터 확인
    all_products = db.select_all_products()
    print(f"총 {len(all_products)}개의 제품이 데이터베이스에 저장되었습니다.")

    # 특정 제품 업데이트 및 확인
    if all_products:
        first_product_id = all_products[0][0]
        db.update_product(first_product_id, price=199.99)
        print("업데이트된 제품 정보:", db.select_product(first_product_id))

    # 특정 제품 삭제
    if all_products:
        last_product_id = all_products[-1][0]
        db.delete_product(last_product_id)
        print("삭제된 제품 정보:", db.select_product(last_product_id))

    db.close()
