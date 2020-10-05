'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
#-------------improved solution--------------
# Runtime: O(n)
# Space: O(1)
#a bitwise exclusive-OR operator ^, XOR will not return any duplicates found in the list
def single_number(arr):
    single_n = arr[0]
    for i in range(1, len(arr)):
        single_n = single_n ^ arr[i] # O(1) "bitwise xor" is binary addition without carry
    return single_n
    


#-------------improved solution--------------
# Runtime: O(nlogn)
# Space: O(1)
def single_number1(arr):
    arr.sort() # O(nlogn) Tim sort
    # Edge cases
    if arr[0] != arr[1]:
        return arr[0]
    if arr[len(arr) -1] != arr[len(arr) -2]:
        return arr[len(arr) -1]
    # General case
    for i in range(1,len(arr)-1):
        if arr[i] != arr[i-1] and arr[i] != arr[i+1]:
            return arr[i]

#-------------first pass solution-------------
# Runtime: O(n^2)
# Space: O(1)
def single_number_first_pas(arr):
    for num in arr: #O(n)
        if arr.count(num) == 1: #O(n)
            return num
        

    
if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    
    print("-------------improved solution---------------")
    print(f"The odd-number-out is {single_number(arr)}")
    print("-------------first pass solution-------------")
    print(f"The odd-number-out is {single_number_first_pas(arr)}")