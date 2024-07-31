# Read the three numbers from input
a = int(input())
b = int(input())
c = int(input())

# Initialize the maximum number with the first number
largest = a

# Compare with the second number
if b > largest:
    largest = b

# Compare with the third number
if c > largest:
    largest = c

# Print the largest number
print(largest)
