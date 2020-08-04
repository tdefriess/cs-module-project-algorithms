'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    max_arr = []
    # initialize window at first position
    window = nums[:k]
    # initialize running max with first maximum and append to output array
    running_max = max(window)
    max_arr.append(running_max)    
    for i in range(1, len(nums) - k + 1):
        # capture values leaving and entering window
        old = window.pop(0)
        new = nums[i + k - 1]
        # update window
        window.append(new)
        # Check old and new window values to see if running_max needs to be recalculated
        if old != running_max and running_max >= new:
            max_arr.append(running_max)
        else:
            running_max = max(window)
            max_arr.append(running_max)
        
    return max_arr
    pass


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
