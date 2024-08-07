import random
random.seed()
n = int(input())
max = 0
min = 100
a = [0] * (n)

for i in range(0, n - 1 + 1,  1):
    a[i] = int(random.random() * 9)
    print(a[i])
for i in range(0, n - 1 + 1,  1):
    if max < a[i]
        max = a[i]
for i in range(0, n - 1 + 1, 1):
    if min > a[i]
        min = a[i]
        print("Max:" + max + "Min: " + min)
