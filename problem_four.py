a_list = input("Enter a list of numbers separated by space: ").split()
a_list1 = input("Enter a list of numbers separated by space: ").split()



intersect = list(filter(lambda x: x in a_list, a_list1))
print("The lists intersects at:", intersect)
