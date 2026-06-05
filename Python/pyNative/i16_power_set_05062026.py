from itertools import combinations

def get_power_set(s):
    elements = list(s)
    power_set = []

    for r in range(len(elements) + 1):
        for combo in combinations(elements, r):
            power_set.append(combo)
    return power_set

my_set = {1, 2, 3}

print(f"power_set: {get_power_set(my_set)}")
