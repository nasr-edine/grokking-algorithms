def simple_search(nb_list, item):
    """"simple_search"""
    operations = 0  # Counter for the number of operations

    print("simple search algorithm")
    for i in range(len(nb_list)):
        operations += 1
        print(f"[{nb_list[i]}]-->", end="")  # Debugging output to show the current index
        if nb_list[i] == item:
            print(f"\nSimple Search Operations: {operations}")
            return i
    print(f"\nSimple Search Operations: {operations}")
    return None

def binary_search(nb_list, item):
    """"binary_search"""
    print("binary search algorithm")
    low = 0
    high = len(nb_list) - 1
    operations = 0  # Counter for the number of operations
    print(f"nb_list: {nb_list}, item: {item}")
    print(f"low: {low}, high: {high}")
    
    print("Middle value:")

    while low <= high:
        operations += 1
        mid = (low + high) // 2
        print(f"[{nb_list[mid]}]-->", end="")  # Debugging output to show the current mid index and guess
        if nb_list[mid] == item:
            print(f"\nBinary Search Operations: {operations}")
            return mid
        elif nb_list[mid] > item:
            high = mid - 1
        else:
            low = mid + 1
    print(f"\nBinary Search Operations: {operations}")
    return None

target = 8
for i in range(3):
    nb_list = list(range(1, target + 1))
    # print(f"nb_list: {nb_list}")


    print("")
    pos = simple_search(nb_list, target)
    print(f"nb: {nb_list[pos]}") 

    print("")
    pos = binary_search(nb_list, target)
    print(f"\nnb: {nb_list[pos]}")  
    target *= 2