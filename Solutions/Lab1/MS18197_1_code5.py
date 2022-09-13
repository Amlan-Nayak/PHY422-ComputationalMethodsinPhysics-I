def Sort(array):
    for i in range(1, len(array)):
        j = i-1
        nxt_element = array[i]
		
        while (array[j] > nxt_element) and (j >= 0):
            array[j+1] = array[j]
            j=j-1
        array[j+1] = nxt_element
    return array
arr=[2,12,8,9,13,75,84,65,1,0,89,9,8]
array=[2,12,8,9,13,75,84,65,1,0,89,9,8]
print("Array: {}".format(arr))
print("Array: {}".format(Sort(array)))
