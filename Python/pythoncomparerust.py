def print_list(numbers):
   for number in numbers:
       print(str(number) + " ", end="")
   print()
def add_one(numbers):
   numbers.append(1)
def main():
   numbers = [1, 1, 1]
   print_list(numbers)
   add_one(numbers)
   print_list(numbers)
if __name__ == '__main__':
   main()
