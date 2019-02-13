data = [2, 99, 7, 4, 6, 8, 33, 55, 88, 22, 11]
print(data)
sorted_data = sorted(data, key=int)
print(sorted_data)

high = len(sorted_data)
print("max of data", high)
low = 0
print("Minimum of data", low)


def binary_search(data, target, low, high):

    if low > high:
        return False
    else:
        mid = (low + high) // 2
        print("mid is", mid)
        if target == data[mid]:
            return True, mid
        elif target < data[mid]:
            return binary_search(data, target, low, mid - 1)
        else:
            return binary_search(data, target, mid + 1, high)


result, position = binary_search(sorted_data, 88, low, high)
print(result, "at position", position)
