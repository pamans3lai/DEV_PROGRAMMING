def merge_dicts(d1, d2):
    result = d1.copy()

    for key, value in d2.items():

        result[key] = result.get(key, 0) + value

    return result

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

merged = merge_dicts(dict_a, dict_b)
print(f"Digabugn: {merged}")

