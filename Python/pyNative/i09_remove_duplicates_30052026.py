def remove_duplicates(items):
    seen = set()
    result = []

    for x in items:
        if x not in seen:
            result.append(x)
            seen.add(x)

    return result

nums = [1, 2, 2, 3, 1, 4, 2]
print(f"Cleaned list: {remove_duplicates(nums)}")
print(seen)