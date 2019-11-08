'''Always important to know merge sort'''

def merge_sort(array):

    if len(array)<2:
        return array

#calculate the mid of array
    mid = len(array)//2

    left_array = array[:mid]
    right_array = array[mid:]
#recursion for every element unless it comes down to one element in each array
    L=merge_sort(left_array)
    R=merge_sort(right_array)
#call for helper function to sort two arrays
    return merge_helper(L,R)

def merge_helper(left,right):

    result = []
    i = j = 0

# only when the element is small, append to result
# increment indexes respectively
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
# append all the rest of the values to result
    result += left[i:]
    result += right[j:]
    return result

# driver code for some test cases
print(merge_sort([4,3,9,1,0,2]))
print(merge_sort([0]))
print(merge_sort([]))
print(merge_sort([0,1,1,1,4,2,8,9,1]))



