def unique(lst1):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(["b","a","a","b","b","b","a","a"])
    ["b","a"]
    >>> unique([])
    []
    >>> unique([2,2,2,3,3,2,3,3])
    [2, 3]
    """
    lst2 = []
    if not(isinstance(lst1, list)):
        raise ValueError
    for i in lst1:
        if i not in lst2:
            lst2.append(i)
    return lst2

if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)


