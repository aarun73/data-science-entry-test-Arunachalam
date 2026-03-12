def swap_if_numeric(x, y):
    """
    Swaps the values of x and y using only x and y as variables, 
    if both are numeric (int or float).
    
    :param x: The first value.
    :param y: The second value.
    :return: -1 if either x or y is not numeric, otherwise None.
    """
    # Check if both x and y are numeric (int or float)
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        # Use arithmetic operations to swap without a temporary variable
        # This approach works for numbers in Python because they have arbitrary precision
        x = x + y
        y = x - y
        x = x - y
        
        # Print the swapped values as required
        print(f"Swapped values: x = {x}, y = {y}")
    else:
        # Return "-1" if either is not numeric
        return "-1"




# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17
