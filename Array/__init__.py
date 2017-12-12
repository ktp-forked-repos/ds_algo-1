def print_array(arr, start=-1, end=-1):
    """
    :param arr: Source array to be printed.
    :param start: OPTIONAL: start index (inclusive), 0 if not given or if given value is greater than equals to len(arr)
    :param end: OPTIONAL: end index (inclusive), len(arr)-1 if not given or if given value is greater than equals to len(arr)
    """
    alen = len(arr)
    start = 0 if start < 0 or start >= alen else start
    end = alen-1 if end < 0 or end >= alen else end
    for i in xrange(start, end+1):
        print i,
