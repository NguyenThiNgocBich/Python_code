import random
from collections import Counter

# Khởi tạo random seed
random.seed()

# Nhập số phần tử của mảng
n = int(input("Nhập số phần tử của mảng: "))

# Tạo mảng ngẫu nhiên
a = [random.randint(0, 9) for _ in range(n)]
print("Mảng ngẫu nhiên:", a)

# Đếm số lần xuất hiện của từng phần tử
count = Counter(a)

# Tìm phần tử lặp lại nhiều nhất
maxt = max(count, key=count.get)

print("Phần tử lặp lại nhiều nhất trong mảng:", maxt)
print("Số lần xuất hiện của phần tử này:", count[maxt])
