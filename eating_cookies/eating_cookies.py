'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    print(n)
    # Your code here
    if n == 0:
        # getting to 0 means we found a way to eat our cookies
        return 1
    if n < 0:
        # getting to a negative number means we didn't find one of the ways
        return 0

    # check if the cache exists
    if cache is None:
        cache = {}
    # if cache is None (no cache yet)
    if n in cache:
        return cache[n]
        # create the cache
    cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
