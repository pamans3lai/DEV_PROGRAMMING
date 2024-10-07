# string_ = 'abcde'  # a string iterable
# tuple_ = ('aa', 'bb', 'cc')  # a tuple iterable
# list_ = ['Python', 'programming language']  # a list iterable

# print(' + '.join(string_))  # join with the ' + ' separator
# print(' = '.join(tuple_))  # join with the ' = ' separator

# sep = ' is a '
# print(sep.join(list_))  # join with the ' is a ' separator

fruits = ['apples', 'bananas', 'peaches', 'grapes']
separator = ' and I like '
joined = (separator.join(fruits))
print('I like', joined)
