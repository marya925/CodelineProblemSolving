def display_menu():
    print("Menu:")
    print("1. Display a right-angle triangle of ones")
    print("2. Display a Palindromic Triangle")
    print("3. Help")
    print("4. Exit")

def right_angle_triangle_of_ones(n):
    for i in range(1, n + 1):
        print('1' * i)

def palindromic_triangle(n):
    for i in range(1, n + 1):
        num = ''.join(str(x) for x in range(1, i + 1))
        print(num + num[-2::-1])

def help_info():
    print("This program displays different types of triangles based on the user's choice:")
    print("1. Right-angle triangle of ones: Displays a triangle of ones with the specified height.")
    print("2. Palindromic Triangle: Displays a palindromic triangle with the specified height.")
    print("3. Help: Displays this help information.")
    print("4. Exit: Exits the program.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            n = int(input("Enter the height of the triangle: "))
            right_angle_triangle_of_ones(n)
        elif choice == '2':
            n = int(input("Enter the height of the palindromic triangle: "))
            palindromic_triangle(n)
        elif choice == '3':
            help_info()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
