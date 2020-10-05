'''
Input: an integer
Returns: an integer
'''
import time
#------------improved solution with tabulation------------------
# O(n) - runtime complexity
# O(n) - space complexity
start_time = time.time()
def tab_eating_cookies(n):
    # n validation 
    if n < 0:
        return 0
    if not isinstance(n, int):
        print("n must be an integer")
        return 

    solution_table = [0 for _ in range(0,n + 1)]
    solution_table[0] = 1
    solution_table[1] = 1
    solution_table[2] = 2

    for i in range(3, n+1):
        solution_table[i] = solution_table[i-3] + solution_table[i-2] +  solution_table[i-1]
    return solution_table[n]
    
if __name__ == "__main__":
    tab_num_cookies = 50
  
    print("------------------tab_eating_cookies-------------------------")
    print(f"There are {tab_eating_cookies(tab_num_cookies)} ways for Cookie Monster to each {tab_num_cookies} cookies")
    print (f"tab_eating_cookies runtime: {time.time() - start_time:.5f} seconds")

#------------improved solution with memoization------------------
# O(n) - runtime complexity
# O(n) - space complexity
start_time = time.time()
def mem_eating_cookies(n, cache = []):
    if n < 0:
        return 0
    if not isinstance(n, int):
        print("n must be an integer")
        return 
    if n == 0:
        cache[0] = 1
        return 1
    if n < 3:
        cache[n] = n
        return n
    if cache[n] == 0:
        cache[n] = mem_eating_cookies(n-3,cache) + mem_eating_cookies(n-2,cache) + mem_eating_cookies(n-1,cache)
    return cache[n]
    
if __name__ == "__main__":
    mem_num_cookies = 50
    cache = [0 for i in range(mem_num_cookies + 1)]
    print("------------------mem_eating_cookies-------------------------")
    print(f"There are {mem_eating_cookies(mem_num_cookies,cache)} ways for Cookie Monster to each {mem_num_cookies} cookies")
    
    print (f"mem_eating_cookies runtime: {time.time() - start_time:.5f} seconds")


#-------------first pass solutin------------------
start_time1 = time.time()
# O(3^n) - runtime complexity
def eating_cookies(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n < 3:
        return n
    return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)


if __name__ == "__main__":
    num_cookies = 10
    print("------------------eating_cookies-------------------------")
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    print (f"eating_cookies runtime: {time.time() - start_time1:.5f} seconds")
