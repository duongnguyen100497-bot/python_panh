from ketnoidb.ketnoi_mysql import connect_db

def get_all_danhmuc():
    conn = connect_db()
    if conn is None:
        print("❌ Không thể kết nối database.")
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT MaDM, TenDM, MoTa, TrangThai FROM danhmuc ORDER BY MaDM ASC")
        rows = cursor.fetchall()   # ✅ Lấy danh sách

        return rows  # ✅ Trả về danh sách để GUI hiển thị

    except Exception as e:
        print("❌ Lỗi khi lấy danh mục:", e)
        return []   # ✅ Tránh lỗi GUI

    finally:
        cursor.close()
        conn.close()
