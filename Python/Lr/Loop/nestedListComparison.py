# # original list
# school = [["Mary", "Jack", "Tiffany"], 
#           ["Brad", "Claire"],
#           ["Molly", "Andy", "Carla"]]

# # student_list = []
# # for class_group in school:
# #     for student in class_group:
# #         student_list.append(student)

# student_list = [student for class_group in school for student in class_group]

# print(student_list)

# matrix = [[j for j in range(5)] for i in range(2)]

# matrix = [] 
  
# for i in range(2): 
      
#     # create empty row (a sublist inside our list)
#     matrix.append([]) 
      
#     for j in range(5): 
#         matrix[i].append(j) 

# print(matrix)

# n = int(input())

# my_list =  [[1, 2] for _ in range(n)]
# print(my_list)


# for i in range(3):

#     # Append an empty sublist inside the list
#     matrix.append([])

#     for j in range(0, 10, 2):
#         matrix[i].append(j)

string = '0123456789'
# matrix = [[string[i % len(string)] for j in range(10)] for i in range(10)]
matrix = [[string[i] for i in range(len(string))] for j in range(10)]

for row in matrix:

    print(row)