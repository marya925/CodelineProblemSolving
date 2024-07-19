def list_of_squares_of_even_numbers(numbers):
    return [x ** 2 for x in numbers if x % 2 == 0]

def slice_list(numbers, start_index, end_index):
    return numbers[start_index:end_index]

def main():
    # Take input list from user
    numbers = input("Enter the list of integers (e.g., [1, 2, 3, 4]): ")
    # Convert input string to list of integers
    numbers = list(map(int, numbers.strip('[]').split(',')))
    
    # Create a new list of squares of even numbers
    even_squares = list_of_squares_of_even_numbers(numbers)
    print("List of squares of even numbers:", even_squares)
    
    # Take start and end indices for slicing the list
    start_index = int(input("Enter the start index for slicing the list: "))
    end_index = int(input("Enter the end index for slicing the list: "))
    
    # Slice the list
    sliced_list = slice_list(numbers, start_index, end_index)
    print("Sliced list:", sliced_list)

if __name__ == "__main__":
    main()
