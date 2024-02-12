strings = input("Enter strings separated by space: ").split()

s_strings = sorted(strings, key=lambda x: (len(x), x))

print("Sorted strings:", s_strings)
