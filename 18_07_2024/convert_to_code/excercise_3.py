import  random
random.seed() #Prepare random number generator
# Input the size of the array
n = int(input("Enter the size of the array: "))
# Initialize the array with zeros
a = [0] * n
# Initialize the sum variable
sum = 0
for i in range(0, n - 1 + 1, 1):
    a[i] = int(random.random() * 9)
    print("a[" + i + "]:" + a[i])
    for i in range(0, n - 1 + 1, 1):
        if a[i] > 1:
            m = a[i]
            b = [0] * (m)

    for j in range(2, m - 1 + 1, 1):
        b[j] = j
        if a[i] % b[j] == 0:
            a[i] = 0
       sum = sum + a[i]
    print("Sum is" + sum)