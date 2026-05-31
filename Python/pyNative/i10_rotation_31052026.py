def rotate_list(lst, n, direction='right'):
    if not lst:
        return  lst

    n = n % len(lst)

    if direction == 'right':
        return lst[-n:] + lst[:-n]

    else:
        return  lst[n:]  + lst[:n]

data =  [1, 2, 3, 4, 5]

print(f"Right Shift 2: {rotate_list(data, 2, 'right')}")
print(f"Left Shift 1: {rotate_list(data, 1, 'left')}")