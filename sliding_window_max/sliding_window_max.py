'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''

from binary_search_tree import BSTNode
from collections import deque


def sliding_window_max(nums, k):
    # Your code here
    de = deque()
    max_list = []

    for i in range(k):
        while de and nums[i] >= nums[de[-1]]:
            de.pop()
        de.append(i)

    for i in range(k, len(nums)):
        max_list.append(nums[de[0]])
          
        # Remove the elements which are  
        # out of this window 
        while de and de[0] <= i-k: 
              
            # remove from front of de 
            de.popleft()  
          
        # Remove all elements smaller than 
        # the currently being added element  
        # (Remove useless elements) 
        while de and nums[i] >= nums[de[-1]] : 
            de.pop() 
          
        # Add current element at the rear of de 
        de.append(i) 
      
    # Print the maximum element of last window 
    max_list.append(nums[de[0]])
    return max_list



if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
