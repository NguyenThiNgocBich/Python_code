
import random
random.seed()

# Nhập số phần tử của mảng
n = int(input("Nhập số phần tử của mảng: "))

# Tạo mảng ngẫu nhiên
a = [int(random.random() * 9) for _ in range(n)]
print("Mảng ngẫu nhiên:", a)

# Nhập vị trí cần thêm và số cần thêm
add_point = int(input("Nhập vị trí cần thêm (0-based index): "))
add_number = int(input("Nhập số cần thêm: "))

# Tạo mảng mới có kích thước lớn hơn 1 phần tử
m = n + 1
e = [0] * m

# Chèn số mới vào vị trí mong muốn
for i in range(m):
    if i < add_point:
        e[i] = a[i]
    elif i == add_point:
        e[i] = add_number
    else:
        e[i] = a[i - 1]

# In mảng mới sau khi thêm
print("Mảng sau khi thêm phần tử:", e)






