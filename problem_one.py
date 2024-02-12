sum_of_nums = lambda n: sum(int(digit) for digit in str(n) if digit.isdigit())

num = int(input("Enter a number: "))
print("Sum:", sum_of_nums(num))

