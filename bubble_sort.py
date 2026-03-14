def bubble_sort(nlist):
    """Sorts a list in ascending order using the bubble sort algorithm.
    Source: https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php
    Args:
        nlist: The list of comparable elements to sort (sorted in place).
    Returns:
        None: The list is sorted in place.
    """
    for passnum in range(len(nlist)-1, 0,-1):
        for i in range(passnum):
            if nlist[i] > nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    
if __name__ == "__main__":
    nlist = [14, 46, 43, 27, 57, 41, 45, 21, 70]
    bubble_sort(nlist)
    print(nlist)