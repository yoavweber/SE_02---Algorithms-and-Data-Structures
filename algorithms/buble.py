array = [1,3,6,2,5,8,4]

def sort(array):
    for s in range(len(array)-1):
        for i in range(len(array)-1):
            if array[i] > array[i+1]:
                while array[i] > array[i+1]:
                    array[i], array[i+1] = array[i+1], array[i]
                    print(array)

sort(array)
print('sorted array:',array)
