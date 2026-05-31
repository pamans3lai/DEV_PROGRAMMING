def merge_and_group(dict1, dict2):
    combined  = {}

    all_keys = set(dict1.keys()) | set(dict2.keys())

    for key in all_keys:
        values = []
        if key in dict1:
            values.append(dict1[key])
        if key in dict2:
            values.append(dict2[key])
        combined[key] = values

    return combined

d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "d": 4}
print(f"Grouped Merge: {merge_and_group(d1, d2)}")