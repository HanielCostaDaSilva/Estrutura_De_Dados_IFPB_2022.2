
def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if(array[j] < array[min]):
                min = j

        array[min], array[i] = array[i], array[min]
# troca

# main
array=[32,28,49,7,52,1,99]
print(array)
selectionSort( array )
print(array)