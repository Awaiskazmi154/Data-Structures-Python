

array = [2, 4, 6, 7, 88, 3, 2, 4, 7, 34, 67, 88]
print(array)

def remove_repeated_from_array(array):

    # bubble sort algorithm
    for index in range(len(array)):
        for counter in range(len(array) - 1):
            if array[counter] > array[counter + 1]:
                temp = array[counter]
                array[counter] = array[counter + 1]
                array[counter + 1] = temp

    # remove repeated => sorted array
    counter = 0
    for index in range(len(array)-1):
        if ( array[index] != array[index+1] ):
            array[counter] = array[index]
            counter += 1

    array[counter] = array[index]
    return array[0:counter+1]


array = remove_repeated_from_array(array)
print(array)