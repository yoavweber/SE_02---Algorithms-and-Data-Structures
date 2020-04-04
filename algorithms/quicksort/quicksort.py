
def swap(arr,pointer_1, pointer_2):
    temp_value = arr[pointer_1]
    arr[pointer_1] = arr[pointer_2]
    arr[pointer_2] = temp_value

def partition(arr,leftPointer,rightPointer):
    pivot = arr[rightPointer]
    pivotPosition = rightPointer
    rightPointer -= 1
  
    while True:
        while arr[leftPointer] < pivot:
            leftPointer +=1

        while arr[rightPointer] > pivot:
            rightPointer -=1    

        if(rightPointer <= leftPointer):
            break
        else:
            swap(arr,leftPointer,rightPointer)

    swap(arr,leftPointer,pivotPosition)
    return leftPointer

def quicksort(arr,leftIndex,rightIndex):
    if(rightIndex - leftIndex <= 0):
        return
    pivot = partition(arr,leftIndex,rightIndex)
    quicksort(arr,leftIndex,pivot-1)
    quicksort(arr,pivot+1,rightIndex)

arr = [3,10,14,1,2,5,9,6,7]
print('before sorting:',arr)

quicksort(arr,0,len(arr) - 1)
print('sorted array:',arr)































# def partition(arr,leftPointer,rightPointer):
#     pivot_position = rightPointer

#     pivot = arr[pivot_position]
#     rightPointer -= 1
#     while True:
#         while arr[leftPointer] < pivot:
#             leftPointer += 1
        
#         while arr[rightPointer] > pivot:
#             rightPointer -= 1
        
#         if leftPointer >= rightPointer:
#             break
#         else:
#             swap(leftPointer, rightPointer)
           
#     swap(leftPointer, pivot_position)
# # We return the leftPointer for the sake of the quicksort method
# # which will appear later in this chapter
#     return leftPointer



# def swap(arr,pointer_1, pointer_2):
#     temp_value = arr[pointer_1]
#     arr[pointer_1] = arr[pointer_2]
#     arr[pointer_2] = temp_value


# arr = [11,2,35,52,3,6,7]

# partition(arr,arr[0],arr[5])

# print(arr)