from common.update_danhmuc import update_danhmuc

while True:
    ma_dm = input("Mã danh mục")
    ten_dm=input("Nhập vào tên danh mục")
    mo_ta=input("Nhập vào mô tả")
    update_danhmuc(ma_dm, ten_dm,mo_ta)
    con=input("tiếp tục y, Thoát nhấn ký tự bất kỳ")
    if con!="y":
        break