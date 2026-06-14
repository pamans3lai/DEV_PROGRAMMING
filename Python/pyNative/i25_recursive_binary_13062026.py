def binary_search_recursive(arr, low, high, x):
    if high < low:
        return -1

    mid = (low + high) // 2

    if arr[mid] == x:
        return mid

    elif arr[mid] > x:
        return binary_search_recursive(arr, low, mid -1, x)

    else:
        return binary_search_recursive(arr, mid +1, high, x)

data = [10, 20, 30, 40, 50, 60]
target = 50
result = binary_search_recursive(data, 0, len(data) -1, target)

print(f"Target found at index: {result}")

