'''
Input: a List of integers
Returns: a List of integers
'''
#-------------improved solution--------------
# Runtime: O(n)
# Space: O(n)
def product_of_all_other_numbers(arr):  
    n = len(arr)
    # Base case 
    if(n == 1): 
        print(0) 
        return
          
    # temporary arrays 
    left = [1]*n  
    right = [1]*n  
  
    # Allocate memory for the product array  
    prod = [0]*n  
  
  
    # Construct the left array  
    for i in range(1, n):  
        left[i] = arr[i - 1] * left[i - 1]  
  
    # Construct the right array  
    for j in range(n-2, -1, -1):  
        right[j] = arr[j + 1] * right[j + 1]  
  
    # Construct the product array using  
    for i in range(n):  
        prod[i] = left[i] * right[i]  
    
    return prod

#-------------first pass solution-------------
# Runtime: O(n^2)
# Space: O(n)
def product_of_all_other_numbers1(arr):
    product_arr = []
    if len(arr) != 0:
        product = 1
    else:
        return product_arr
   
    for i in range(len(arr)):
        for index, num in enumerate(arr):
            if i != index:
                product *=num
            index +=1

        product_arr.append(product)
        product = 1
    return product_arr
        
arr1 = [1, 7, 3, 4]
print(product_of_all_other_numbers(arr1))

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
    
