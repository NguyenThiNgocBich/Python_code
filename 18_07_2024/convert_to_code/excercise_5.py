import random
random.seed() #Prepare random number generator

n = int(input())
a = [0] * (n)

i = 0
j = 0
b = 0
m = 0
for i in range(0, n - 1 + 1, 1):
    a[i] = int(random.redom() * 9)
    print(a[i])
for j in range(0, n - 1 + 1, 1):
for b in range(j + 1, n - 1 + 1, 1):
    if a[j] > a[b]
       a[b] = a[j]
       a[j] = m
print("")
for i in range(0, n - 1 + 1, 1):
     print(a[i])


