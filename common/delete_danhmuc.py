from ketnoidb.ketnoi_mysql import connect_db


def delete_danhmuc(ma_dm):
    conn = connect_db()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        sql = "DELETE FROM danhmuc WHERE MaDM = %s"
        cursor.execute(sql, (ma_dm,))
        conn.commit()

        if cursor.rowcount > 0:
            print(f"✅ Đã xóa danh mục có MaDM = {ma_dm}")
            return True
        else:
            print("⚠️ Không tìm thấy danh mục để xóa.")
            return False

    except Exception as e:
        print("❌ Lỗi khi xóa danh mục:", e)
        return False

    finally:
        cursor.close()
        conn.close()
