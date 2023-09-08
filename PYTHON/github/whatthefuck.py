def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        # Check if the target is equal to the middle element
        if arr[mid] == target:
            return mid

        # If the target is less than the middle element, search the left half
        elif arr[mid] > target:
            right = mid - 1

        # If the target is greater than the middle element, search the right half
        else:
            left = mid + 1

    # Target not found in the array
    return -1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10

result = binary_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the array")
