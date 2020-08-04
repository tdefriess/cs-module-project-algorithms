'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    arr.sort()
    #check first element:
    if arr[0] != arr[1]:
        return arr[0]
    # check final element:
    if arr[len(arr)-1] != arr[len(arr)-2]:
        return arr[len(arr)-1]
    for i in range(1, len(arr)-2):
        if arr[i-1] < arr[i] and arr[i+1] > arr[i]:
            return arr[i]

    pass


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")