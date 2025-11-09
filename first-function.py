# first-function.py

def add_numbers(a, b):
    """
    A simple function that returns the sum of two numbers.
    """
    result = a + b
    return result

if __name__ == "__main__":
    test_result = add_numbers(5, 3)
    print(f"Test in first-function.py: {test_result}") 
