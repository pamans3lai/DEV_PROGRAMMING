def flatten(lst):
    flat_list = []

    for item in lst:
        if isinstance(item, list):
            # Recursion: jika itu adalah list, flatten dan extend
            flat_list.extend(flatten(item))
        else:
            # base case: nilai single, tambahkan saja
            flat_list.append(item)

    return flat_list

nested_data = [1, [2, 3], [4, [5, 6]], 7]
result = flatten(nested_data)

print(f"Original: {nested_data}")
print(f"Flattened: {result}")
