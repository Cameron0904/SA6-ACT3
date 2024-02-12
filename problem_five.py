numbers = input("Enter a list of numbers separated by space: ").split()

n = 3
result = list(map(lambda x: int(x) ** n, numbers))
print("Original list of numbers:", numbers)
print("After raising each number to the power of", n, ":", result)
