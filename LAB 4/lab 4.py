import sqlite3

def create_db_and_table():
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS product (
        Id INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Price REAL NOT NULL,
        Amount INTEGER NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

def show_products():
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute('SELECT * FROM product')
    products = c.fetchall()
    for product in products:
        print(product)
    conn.close()

def add_product(name, price, amount):
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute('INSERT INTO product (Name, Price, Amount) VALUES (?, ?, ?)', (name, price, amount))
    conn.commit()
    conn.close()

def search_product(name):
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute('SELECT * FROM product WHERE Name LIKE ?', ('%' + name + '%',))
    products = c.fetchall()
    for product in products:
        print(product)
    conn.close()

def update_product(id, price, amount):
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute('UPDATE product SET Price = ?, Amount = ? WHERE Id = ?', (price, amount, id))
    conn.commit()
    conn.close()

def delete_product(id):
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute('DELETE FROM product WHERE Id = ?', (id,))
    conn.commit()
    conn.close()

def main_menu():
    create_db_and_table()
    while True:
        print("\n--- Menu Quản Lý Sản Phẩm ---")
        print("1. Hiển Thị Danh Sách Sản Phẩm")
        print("2. Thêm Sản Phẩm Mới")
        print("3. Tìm Kiếm Sản Phẩm Theo Tên")
        print("4. Cập Nhật Thông Tin Sản Phẩm")
        print("5. Xóa Sản Phẩm")
        print("6. Thoát")
        choice = input("Chọn chức năng: ")

        if choice == '1':
            show_products()
        elif choice == '2':
            name = input("Tên sản phẩm: ")
            price = float(input("Giá sản phẩm: "))
            amount = int(input("Số lượng: "))
            add_product(name, price, amount)
        elif choice == '3':
            name = input("Nhập tên sản phẩm cần tìm: ")
            search_product(name)
        elif choice == '4':
            id = int(input("ID sản phẩm: "))
            price = float(input("Giá mới: "))
            amount = int(input("Số lượng mới: "))
            update_product(id, price, amount)
        elif choice == '5':
            id = int(input("ID sản phẩm: "))
            delete_product(id)
        elif choice == '6':
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    main_menu()
