import random

def san_sinh_mang(n):
    """
    Ham san sin mang
    tham so :
        n: so luong phan tu can san sinh
    tra ve: 
        mang chua cac so ngau nhien
    """
    mang = []
    for i in range(n):
        so_ngau_nhien = random.randint(-100, 100)
        mang.append(so_ngau_nhien)
    return mang

def tim_tuyen_tinh(mang, x):
    """
    Ham tim kiem tuyen tinh
    tham so :
        mang: danh sach chua cac gia tri
        x: gia tri can tim
    tra ve: 
        vi tri tim thay trong mang 
        -1 khi khong tim thay
    """
    n = len(mang)
    for i in range(n):
        if mang[i] == x:
            return i
    return -1
def main ():
    """Ham chinh"""
    mang = san_sinh_mang(20)
    print(mang)
    x = int(input("Nhap vao gia tri can tim: "))
    vitri = tim_tuyen_tinh(mang, x)
    if vitri != -1:
        print(f"Gia tri {x} duoc tim thay tai vi tri {vitri}")
    else:
        print(f"Khong tim thay gia {x}")
##Module chinh cua chuong trinh
if __name__ == "__main__":
    main()