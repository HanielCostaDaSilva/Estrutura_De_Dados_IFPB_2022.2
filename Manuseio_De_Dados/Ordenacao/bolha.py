array=[32,28,49,7,52,1,99]

def bubbleSort(array):
    for i in range(len(array)-1, 0 ,-1):
        alterou=False
        
        for j in range( 0, i):
            
            if array[j] >= array[j+1]:
                array[j], array[j+1]= array[j+1], array[j]
                alterou=True
        
        if alterou==False:
            break
        
    #return array

        

bubbleSort(array)
print(array)