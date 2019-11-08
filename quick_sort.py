
# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot
def partition_function(array,low,high):

    pivot = array[high] #select pivot as the last element
    i = low-1 # index i not yet pointing to any element in the array
    for j in range(low,high):
        if array[j]<pivot: #execute loop when no reference element at j is less than pivot
            i += 1
            array[j],array[i]=array[i],array[j] #swap eleement at i and j
    array[i+1],array[high]=array[high],array[i+1]
    return i+1

# Function to do Quick sort

def quick_sort(array):
    arr=helper_function(array)
    l = arr[0]
    r = arr[1]
    if l<r:
        index = partition_function(array,l,r)
        quick_sort(array[:index-1])
        quick_sort(array[index+1:])
    return array

def helper_function(array):
    return [0,len(array)-1]


#driver code
print(quick_sort([4,3,9,1,0,2]))
print(quick_sort([0]))
print(quick_sort([]))
print(quick_sort([0,1,1,1,4,2,8,9,1]))