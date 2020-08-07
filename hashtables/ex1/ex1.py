# cache to store values that match
cache = {}

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # while loop to allow me to loop through elements
    # i'll have two pointers 
    if length == 1:
        return None
    first_pointer = 0
    second_pointer = 1

    while first_pointer != length - 1:
        # print(second_pointer,'second index after each itteration')

        if second_pointer == length:
            first_pointer += 1
            second_pointer = first_pointer + 1

        elif weights[first_pointer] + weights[second_pointer] == limit: # what returns my tuple and passes test
            cache[weights[first_pointer]] = (second_pointer, first_pointer)
            pair = cache[weights[first_pointer]]

        second_pointer += 1

    if pair:
        return pair
    else:
        return None



weights_3 = [4, 6, 10, 15, 16]
# arr = [4,4]
# print(get_indices_of_item_weights(arr, 2, 8))
print(get_indices_of_item_weights(weights_3, 5, 21))
