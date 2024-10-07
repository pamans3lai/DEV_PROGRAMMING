# def facebook_likes(names):
#     if len(names) == 0:
#         return "no one likes this"
#     elif len(names) == 1:
#         return (names) + " likes this"
#     # elif len(names) == 2:
#     #     return names[0] + " and " + names[1] + " likes this"
#     elif len(names) == 2: 
#     #    return ", ".join(names[:-1]) + " and " + names[-1] + " likes this"
#         return ', '.join(map(, lst[:-1])) + ' and ' + (lst[-1])
#     else:
#         return  ", ".join(names[:-1]) + " and " + len(names[2:])  + " others likes this"

# names = ["Alex", "Jacob", "Mark", "Max"]

# print(names)

# # def likes(names):
# #     if len(names) == 0:
# #         return 'no one likes this'
# #     elif len(names) == 1:
# #         return (names) + ' likes this'
# #     elif len(names) == 2: 
# #         return (names[0]) + ' and ' + (names[1]) + ' likes this'
# #     elif len(names) == 3: 
# #         return ', '.join(map(, names[:-1])) + ' and ' + (names[-1]) + ' likes this'
# #     elif len(names) > 3:
# #         return ', '.join(map(, names[:-1])) + ' and ' + len(names[+2])  + ' others likes this'    
# #     else: []

names = ['Alex', 'Jacob', 'Mark', 'Max']

# def likes(names):
#     if len(names) == 0:
#         return 'no one likes this'
#     elif len(names) == 1:
#         return (names) + ' likes this'
#     elif len(names) == 2: 
#         return (names[0]) + ' and ' + (names[1]) + ' likes this'
#     elif len(names) == 3: 
#         return (names[0]) + ' and ' + (names[1]) + (names[2]) + ' and ' + (names[-1]) + ' likes this'
#     elif len(names) > 3:
#         return (names[0]) + ' and ' + (names[1]) + ' and ' + len(names[+2])  + ' others likes this'    
#     else: []

def who_likes_this(names: list) -> str:
    who = 'no one'
    number_of_likes = len(names)
    if number_of_likes > 0 and number_of_likes < 3 :
        who = ' and '.join(names)
    elif number_of_likes >= 3:
        who = ', '.join(names[:2])
        who += ' and ' + (names[2] if number_of_likes == 3 else f' and {len(names[2:])} others')
    return f'{who} like{"" if number_of_likes > 1 else "s" } this'


print(who_likes_this)