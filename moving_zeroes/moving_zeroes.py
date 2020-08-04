'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    first_zero_index = -1
    second_zero_index = -1
    i = 0
    while i < len(arr):
        if arr[i] == 0 and second_zero_index == -1 and first_zero_index != -1:
            second_zero_index = i
            i += 1
        # if a zero is found, record zero index
        elif arr[i] == 0 and first_zero_index == -1:
            first_zero_index = i
            i += 1
        # if nonzero found, swap with zero index if exists
        elif arr[i] != 0 and first_zero_index != -1:
            arr[first_zero_index], arr[i] = arr[i], arr[first_zero_index]
            # check for second index. If second index exists, send pointer back to index,
            # set first index to second index and clear second index
            if second_zero_index != -1:
                first_zero_index = second_zero_index
                second_zero_index = -1
                i = first_zero_index
            # # if second index does not exist, increment pointer and update first zero index
            else:
                first_zero_index = i
                i += 1
        else:
            i += 1
        

    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")