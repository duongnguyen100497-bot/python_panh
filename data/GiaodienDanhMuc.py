import tkinter as tk
from tkinter import ttk, messagebox

# Gọi các hàm xử lý ĐÃ CÓ SẴN
from common.get_danhmuc import get_all_danhmuc
from common.update_danhmuc import update_danhmuc
from common.delete_danhmuc import delete_danhmuc
from common.insertdanhmuc import insert_danhmuc   # <== Đúng tên hàm

# ========= FUNCTION ========= #

def load_data():
    """Hiển thị danh sách lên bảng"""
    for row in tree.get_children():
        tree.delete(row)

    data = get_all_danhmuc()
    if data:
        for dm in data:
            tree.insert("", tk.END, values=(dm[0], dm[1], dm[2], dm[3]))


def add_danhmuc():
    ten = entry_ten.get()
    mota = entry_mota.get()
    trangthai = entry_trangthai.get()

    if ten.strip() == "":
        messagebox.showwarning("Cảnh báo", "Tên danh mục không được bỏ trống!")
        return

    insert_danhmuc(ten, mota, trangthai)
    load_data()
    clear_input()
    messagebox.showinfo("Thành công", "Đã thêm danh mục!")


def delete_danhmuc_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chọn dữ liệu", "Hãy chọn danh mục để xóa!")
        return

    maDM = tree.item(selected[0])["values"][0]

    delete_danhmuc(maDM)
    load_data()
    clear_input()
    messagebox.showinfo("Đã xóa", "Danh mục đã được xóa!")


def update_danhmuc_selected():
    selected = tree.selection()
    if not selected:
        messagebox.showwarning("Chọn dữ liệu", "Hãy chọn danh mục để sửa!")
        return

    maDM = entry_ma.get()
    ten = entry_ten.get()
    mota = entry_mota.get()
    trangthai = entry_trangthai.get()

    update_danhmuc(maDM, ten, mota, trangthai)
    load_data()
    clear_input()
    messagebox.showinfo("Đã sửa", "Cập nhật danh mục thành công!")


def on_select(event):
    """Khi click chọn dòng trong bảng → load lên form"""
    selected = tree.selection()
    if not selected:
        return

    values = tree.item(selected[0])["values"]

    entry_ma.config(state=tk.NORMAL)
    entry_ma.delete(0, tk.END)
    entry_ma.insert(0, values[0])
    entry_ma.config(state=tk.DISABLED)

    entry_ten.delete(0, tk.END)
    entry_ten.insert(0, values[1])

    entry_mota.delete(0, tk.END)
    entry_mota.insert(0, values[2])

    entry_trangthai.delete(0, tk.END)
    entry_trangthai.insert(0, values[3])


def clear_input():
    entry_ma.config(state=tk.NORMAL)
    entry_ma.delete(0, tk.END)
    entry_ma.config(state=tk.DISABLED)

    entry_ten.delete(0, tk.END)
    entry_mota.delete(0, tk.END)
    entry_trangthai.delete(0, tk.END)


# ========= UI ========= #

root = tk.Tk()
root.title("Quản lý Danh Mục")
root.geometry("750x480")

frame_input = tk.LabelFrame(root, text="Thông tin danh mục", padx=10, pady=10)
frame_input.pack(fill="x", padx=10, pady=5)

tk.Label(frame_input, text="Mã DM:").grid(row=0, column=0)
entry_ma = tk.Entry(frame_input, state=tk.DISABLED)   # KHÓA TỰ ĐỘNG
entry_ma.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Tên DM:").grid(row=1, column=0)
entry_ten = tk.Entry(frame_input)
entry_ten.grid(row=1, column=1, padx=5)

tk.Label(frame_input, text="Mô tả:").grid(row=2, column=0)
entry_mota = tk.Entry(frame_input)
entry_mota.grid(row=2, column=1, padx=5)

tk.Label(frame_input, text="Trạng thái (1/0):").grid(row=3, column=0)
entry_trangthai = tk.Entry(frame_input)
entry_trangthai.grid(row=3, column=1, padx=5)

frame_btn = tk.Frame(root)
frame_btn.pack(pady=5)

tk.Button(frame_btn, text="Thêm", width=12, command=add_danhmuc).pack(side="left", padx=5)
tk.Button(frame_btn, text="Sửa", width=12, command=update_danhmuc_selected).pack(side="left", padx=5)
tk.Button(frame_btn, text="Xóa", width=12, command=delete_danhmuc_selected).pack(side="left", padx=5)
tk.Button(frame_btn, text="Làm mới", width=12, command=clear_input).pack(side="left", padx=5)

columns = ("madm", "tendm", "mota", "trangthai")
tree = ttk.Treeview(root, columns=columns, show="headings", height=12)

tree.heading("madm", text="Mã DM")
tree.heading("tendm", text="Tên Danh Mục")
tree.heading("mota", text="Mô tả")
tree.heading("trangthai", text="Trạng thái")

tree.pack(fill="both", expand=True, padx=10, pady=10)
tree.bind("<<TreeviewSelect>>", on_select)

load_data()
root.mainloop()


