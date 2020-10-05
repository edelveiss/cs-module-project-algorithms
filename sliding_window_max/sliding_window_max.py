'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


# Runtime: O(n) * O(k)
# Space: O(n)
def sliding_window_max(nums, k):
    max_window=[]
    for i in range(len(nums)-k +1):
        max_window.append(max(nums[i:i+k])) # max is O(k)
    return max_window

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
