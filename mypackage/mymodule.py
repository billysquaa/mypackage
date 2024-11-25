def top_n(items, n):
    """Return the top n items in an array, in descending order.

    Args:
        items(array): list or array-like object
        n(int): number of items to return

    Return:
        Array: top n items, in descending order

    Egs:
        >>>top_n([1,2,3,4,5,6,7,8], 3)
        [8,7,6]
    """

      # We add the body of the function just below the docstring:

    for i in range(n):  # Keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:  # If this item is bigger than next the item..
                items[j], items[j+1] = items[j+1], items[j]  # swap the two!

    # Get last two items
    top_n = items[-n:]

    # Return in descending order
    return top_n[::-1]
