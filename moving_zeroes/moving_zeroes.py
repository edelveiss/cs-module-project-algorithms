'''
Input: a List of integers
Returns: a List of integers
'''
#-------------improved solution--------------
# Runtime: O(n)
# Space: O(1)
def moving_zeroes(arr):
    zero_counter = 0
    for i in range(len(arr)):
        if arr[i]  != 0:
            arr[zero_counter], arr[i] = arr[i], arr[zero_counter]
            zero_counter +=1  
    return arr

#-------------first pass solution-------------
# Runtime: O(n^2)
# Space: O(1)
def moving_zeroes_first_pass(arr):
    swap = 1
    while swap > 0:
        swap = 0
        for i in range(len(arr)-1):
            if arr[i] == 0 and arr[i+1] != 0:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swap +=1  
    return arr

 

if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [4, 3, 1, 0, -2]
    
    print("-------------improved solution---------------")
    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")
    print("-------------first pass solution-------------")
    print(f"The resulting of moving_zeroes is: {moving_zeroes_first_pass(arr)}")