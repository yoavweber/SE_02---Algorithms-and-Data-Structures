import math

array = [1,3,5,7,9,11,13]
array.sort()


def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array) - 1
    count = 0
    while lower_bound <= upper_bound:
        midpoint = (upper_bound + lower_bound) // 2
        value_at_midpoint = array[midpoint]
        
        if value < value_at_midpoint:
            count += 1
            upper_bound = midpoint - 1
        elif value > value_at_midpoint:
            count += 1
            lower_bound = midpoint + 1
        elif value == value_at_midpoint:
            count += 1
            print(count)
            break
    print('element is not in the array')

        
    
array = [1,3,5,7,9,11,1]
binary_search(array, 20)



        
