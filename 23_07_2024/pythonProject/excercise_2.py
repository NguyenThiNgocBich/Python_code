import random

random.seed()

# Nhập số phần tử của mảng
n = int(input("Nhập số phần tử của mảng: "))

# Tạo mảng ngẫu nhiên
a = [random.randint(0, 9) for _ in range(n)]
print("Mảng ngẫu nhiên:", a)

# Nhập vị trí cần xóa
delete_point = int(input("Nhập vị trí cần xóa (0-based index): "))

# Kiểm tra vị trí hợp lệ
if 0 <= delete_point < n:
    # Xóa phần tử tại vị trí delete_point
    for i in range(delete_point, n - 1):
        a[i] = a[i + 1]
    # Giảm kích thước mảng
    n -= 1
    # Cắt mảng để loại bỏ phần tử cuối cùng (đã được dịch lên)
    a = a[:n]

    # In mảng sau khi xóa
    print("Mảng sau khi xóa phần tử tại vị trí", delete_point, "là:", a)
else:
    print("Vị trí xóa không hợp lệ")
