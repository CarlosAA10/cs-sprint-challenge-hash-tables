def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    cache = {}

    result = [] 
    for num in a: # correctly creates negative and positive value in cache for each number 

        if num not in cache and num > 0:
            cache[num] = "positive"

        if num not in cache and num < 0:

            cache[num] = "negative"

    for num in a:

        if num < 0:

            if num in cache and abs(num) in cache:

                result.append(abs(num)) # adds our negative number turned positive to results

    



    return result
    # return cache


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
