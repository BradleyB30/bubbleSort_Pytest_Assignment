"""
pytest test cases for the bubble_sort function.

Run with coverage:
    pytest --cov=bubble_sort --cov-report=term-missing test_bubble_sort.py -v
"""

import pytest
from bubble_sort import bubble_sort

@pytest.mark.parametrize("input_list, expected_output", [
    #w3resource example list
    ([14, 46, 43, 27, 57, 41, 45, 21, 70], [14, 21, 27, 41, 43, 45, 46, 57, 70]),
    #Already sorted list
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    #Reverse sorted list, worst case for bubble sort
    ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
])

def test_bubble_sort(input_list, expected_output):
    bubble_sort(input_list)
    assert input_list == expected_output

# test case 2 Exception handling (uses pytest.raises)
def test_bubble_sort_non_comparable():
    mixed_list = [1, "two", 3]
    with pytest.raises(TypeError):
        bubble_sort(mixed_list)
