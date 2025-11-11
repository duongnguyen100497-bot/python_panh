from ketnoidb.ketnoi_mysql import connect_db


def update_danhmuc(ma_dm, ten_dm, mo_ta, trang_thai=None):
    conn = connect_db()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Tạo câu UPDATE động theo tham số truyền vào
        fields = []
        values = []

        if ten_dm is not None:
            fields.append("TenDM = %s")
            values.append(ten_dm)

        if mo_ta is not None:
            fields.append("MoTa = %s")
            values.append(mo_ta)

        if trang_thai is not None:
            fields.append("TrangThai = %s")
            values.append(trang_thai)

        # Nếu không có gì để cập nhật
        if not fields:
            print("⚠️ Không có dữ liệu cần cập nhật.")
            return False

        values.append(ma_dm)

        sql = f"UPDATE danhmuc SET {', '.join(fields)} WHERE MaDM = %s"

        cursor.execute(sql, tuple(values))
        conn.commit()

        if cursor.rowcount > 0:
            print("✅ Cập nhật thành công!")
            return True
        else:
            print("⚠️ Không tìm thấy danh mục để cập nhật.")
            return False

    except Exception as e:
        print("❌ Lỗi khi cập nhật danh mục:", e)
        return False

    finally:
        cursor.close()
        conn.close()
