import random

random.seed()  # Prepare random number generator

# Input the size of the array
n = int(input("Enter the size of the array: "))

# Initialize the array with zeros
a = [0] * n

# Initialize the sum variable
sum = 0

# Populate the array with random integers and calculate the sum
for i in range(n):
    a[i] = int(random.random() * 9)  # Generate a random integer between 0 and 8
    sum += a[i]  # Add the current element to the sum
    print(a[i])  # Print the current element

# Print the total sum
print("Sum is:", sum)
