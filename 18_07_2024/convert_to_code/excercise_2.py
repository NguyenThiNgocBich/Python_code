import random
random.seed() #Prepare random number generator

n = int(input("Enter the size of the array: "))
a = [0] * (n)
sum = 0

for i in range(n):
    a[i] = int(random.random() * 9)
    print(a[i])
    if a[i] % 2 != 0:
        sum += a[i]
print("sum in: ", sum)
