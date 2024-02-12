nums = input("Enter a list of numbers separated by space: ").split()

Max = list(filter(lambda x: all(x >= num for num in nums), nums))
print("Maximum number:", Max)
