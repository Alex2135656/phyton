def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = sorted_list[mid]
        
        if mid_value == target:
            return mid  
        elif mid_value < target:
            left = mid + 1 
        else:
            right = mid - 1  

    return -1  

if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
    target_number = 7
    result = binary_search(numbers, target_number)
    if result != -1:
        print(f"Element {target_number} znaleziony na indeksie {result}.")
    else:
        print(f"Element {target_number} nie został znaleziony w liście.")