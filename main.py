# main.py

from first_function import add_numbers

def main():
    num1 = 10
    num2 = 25
    
    sum_result = add_numbers(num1, num2)
    
    print(f"The sum of {num1} and {num2} is: {sum_result}")

if __name__ == "__main__":
    main()
