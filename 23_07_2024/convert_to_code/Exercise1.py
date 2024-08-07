
import random
random.seed() #Prepare random number generator

n = int(input())
a = [0] *(n)

temp = 0
max_count = 0
for i in range(0, n - 1 + 1, 1):
    a[i] = int(random.ramdom() * 10)
    print (a[i])
for i in range(0, n -1 + 1, 1):
        temp = 0
for j in range(i + 1, n -1 + 1, 1):
    if a[i] == a[j]:
        temp = temp + 1
        if temp >= max:
            max_count = temp
            maxt = a[i]

        print("phần tử lặp lại nhiều nhất trong mảng:" + maxt)