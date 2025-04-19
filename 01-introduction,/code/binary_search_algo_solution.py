def binary_search(sorted_list, target):
    """Binary search with operation count"""
    low = 0
    high = len(sorted_list) - 1
    operations = 0  # Counter for the number of operations
    while low <= high:
        operations += 1  # Increment for each iteration
        mid = (low + high) // 2
        guess = sorted_list[mid]
        print(f"[{mid}]-->", end="")  # Debugging output to show the current mid index and guess
        if guess == target:
            print(f"\nBinary Search Operations: {operations}")
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1

    print(f"\nBinary Search Operations: {operations}")
    return None

def simple_search(nb_list, item):
    """Simple search with operation count"""
    operations = 0  # Counter for the number of operations

    for i in range(len(nb_list)):
        operations += 1  # Increment for each comparison
        if nb_list[i] == item:
            print(f"Simple Search Operations: {operations}")
            return i

    print(f"Simple Search Operations: {operations}")
    return None

# Example usage for the worst case with different list sizes:

# List with 8 items
sorted_list_8 = [1, 2, 3, 4, 5, 6, 7, 8]
target_8 = 9  # Target not in the list (worst case for both searches)

print("List with 8 items:")
print(f"Binary Search: {sorted_list_8}, Target: {target_8}") 
simple_result_8 = simple_search(sorted_list_8, target_8)
print(f"Simple Search Result: {simple_result_8}")  # Output: None
binary_result_8 = binary_search(sorted_list_8, target_8)
print(f"Binary Search Result: {binary_result_8}")  # Output: None

# List with 16 items
sorted_list_16 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
target_16 = 17  # Target not in the list (worst case for both searches)

print("\nList with 16 items:")
print(f"Binary Search: {sorted_list_16}, Target: {target_16}")
simple_result_16 = simple_search(sorted_list_16, target_16)
print(f"Simple Search Result: {simple_result_16}")  # Output: None
binary_result_16 = binary_search(sorted_list_16, target_16)
print(f"Binary Search Result: {binary_result_16}")  # Output: None

# List with 32 items
sorted_list_32 = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32
]
target_32 = 33  # Target not in the list (worst case for both searches)

print("\nList with 32 items:")
print(f"Binary Search: {sorted_list_32}, Target: {target_32}")

simple_result_32 = simple_search(sorted_list_32, target_32)
print(f"Simple Search Result: {simple_result_32}")  # Output: None
binary_result_32 = binary_search(sorted_list_32, target_32)
print(f"Binary Search Result: {binary_result_32}")  # Output: None