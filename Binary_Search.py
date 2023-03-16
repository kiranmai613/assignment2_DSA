def binary_search(arr, x):
    """
    Search for the element x in the sorted array arr using binary search.

    Returns the index of x in arr if it is present, else returns -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [2, 4, 6, 8, 10, 12, 14]
x = 10

index = binary_search(arr, x)

if index == -1:
    print(f"{x} is not present in the array.")
else:
    print(f"{x} is present at index {index} in the array.")
