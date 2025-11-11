from ketnoidb.ketnoi_mysql import connect_db


def insert_danhmuc(ten_dm, mo_ta, trang_thai=1):
    conn = connect_db()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO danhmuc (TenDM, MoTa, TrangThai)
            VALUES (%s, %s, %s)
        """
        values = (ten_dm, mo_ta, trang_thai)

        cursor.execute(sql, values)
        conn.commit()

        print("✅ Thêm danh mục thành công!")
        return True

    except Exception as e:
        print("❌ Lỗi khi thêm danh mục:", e)
        return False

    finally:
        cursor.close()
        conn.close()
