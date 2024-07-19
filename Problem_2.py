def decimal_to_binary(n):
    if n == 0:
        return "0"
    
    binary_digits = []
    
    while n > 0:
        remainder = n % 2
        binary_digits.append(str(remainder))
        n = n // 2
    
    # The binary number is the sequence of remainders read from bottom to top
    binary_digits.reverse()
    return ''.join(binary_digits)

def main():
    number = int(input("Enter a positive decimal number: "))
    
    if number < 0:
        print("Please enter a positive number.")
        return
    
    binary_equivalent = decimal_to_binary(number)
    print(f"The binary equivalent of {number} is {binary_equivalent}")

if __name__ == "__main__":
    main()
