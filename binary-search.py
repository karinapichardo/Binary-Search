def binary_search(numbers, element):
    first = 0
    last = len(numbers) - 1

    while first <= last:
        middle = (first + last) // 2
        answer = numbers[middle]
        if answer == element:
            return middle
        if answer > element:
            last = middle - 1
        else:
            first = middle + 1
    return None

my_list = [8, 18, 24, 28, 36]
print (binary_search(my_list, 18)) #testing code, position would be 1
print (binary_search(my_list, -2)) #testing code, element wouldn't be found, invalid


