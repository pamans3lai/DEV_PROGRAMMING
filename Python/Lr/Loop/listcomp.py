# my_list = []
# for i in range(5):
#     my_list.append(i)

# print(my_list)

# my_list = [i for i in range(5)]
# print(my_list)

starting_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_inefficient_list = []

for i in starting_numbers:
    my_inefficient_list.append(i + 10)

print(my_inefficient_list)


my_efficient_list = [i + 10 for i in my_inefficient_list]
print(my_efficient_list)
