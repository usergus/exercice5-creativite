import pytest
from average import calculate_average

def test_calculate_average():
    result = calculate_average([1, 2, 3, 4, 5])
    print(f"Average of [1, 2, 3, 4, 5]: {result}")
    assert result == 3
    
    result = calculate_average([10, 20, 30])
    print(f"Average of [10, 20, 30]: {result}")
    assert result == 20
    
    result = calculate_average([-1, 0, 1])
    print(f"Average of [-1, 0, 1]: {result}")
    assert result == 0
    
    result = calculate_average([1])
    print(f"Average of [1]: {result}")
    assert result == 1
    
    result = calculate_average([])
    print(f"Average of []: {result}")
    assert result == 0
