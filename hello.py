#!/usr/bin/env python3
"""
Simple Python Program - Greeting and Calculator
A basic program demonstrating Python fundamentals
"""

def greet_user():
    """Function to greet the user and get their name"""
    print("🐍 Welcome to Simple Python Program! 🐍")
    name = input("What's your name? ")
    print(f"Hello, {name}! Nice to meet you!")
    return name

def simple_calculator():
    """Simple calculator function"""
    print("\n🧮 Let's do some math!")
    try:
        num1 = float(input("Enter first number: "))
        operation = input("Choose operation (+, -, *, /): ")
        num2 = float(input("Enter second number: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero!")
                return
        else:
            print("Invalid operation!")
            return
            
        print(f"Result: {num1} {operation} {num2} = {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers!")

def show_fun_facts():
    """Display some fun Python facts"""
    facts = [
        "Python was named after Monty Python's Flying Circus!",
        "Python uses indentation to define code blocks.",
        "Python is great for beginners and professionals alike!",
        "Python's philosophy: 'Simple is better than complex.'"
    ]
    
    print("\n🎉 Fun Python Facts:")
    for i, fact in enumerate(facts, 1):
        print(f"{i}. {fact}")

def main():
    """Main function to run the program"""
    # Greet the user
    user_name = greet_user()
    
    # Show menu
    while True:
        print(f"\n--- What would you like to do, {user_name}? ---")
        print("1. Use calculator")
        print("2. See fun Python facts")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            simple_calculator()
        elif choice == '2':
            show_fun_facts()
        elif choice == '3':
            print(f"Goodbye, {user_name}! Thanks for using the program! 👋")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()