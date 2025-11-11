from common.insertdanhmuc import insert_danhmuc
while True:
    ten_dm=input("Nhập vào tên danh mục")
    mo_ta=input("Nhập vào mô tả")
    insert_danhmuc(ten_dm,mo_ta)
    con=input("tiếp tục y, Thoát nhấn ký tự bất kỳ")
    if con!="y":
        break
