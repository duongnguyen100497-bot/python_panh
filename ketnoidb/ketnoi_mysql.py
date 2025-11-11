import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3307,              # cổng MySQL của bạn
            user="root",            # tên đăng nhập MySQL
            password="",            # mật khẩu (nếu có thì điền vào)
            database="db_panh"      # tên database
        )

        if connection.is_connected():
            print("✅ Kết nối MySQL thành công!")
            return connection

    except Error as e:
        print("❌ Lỗi kết nối MySQL:", e)
        return None
