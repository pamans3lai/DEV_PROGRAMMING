print("Welcome to the tip calculator!")
bill = []
bill = float(input("What was the total bill? $"))
tip = []
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = []

people = int(input("How many people to split the bill? "))

pay = round(((bill+tip)/people), 2)

print(pay)
print(f'everyone should pay ${pay}')