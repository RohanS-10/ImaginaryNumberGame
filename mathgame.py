import random
import cmath

def generate_complex_number():
    # Generates a random complex number with integer real and imaginary parts
    real_part = random.randint(1, 10)
    imag_part = random.randint(1, 10)
    return complex(real_part, imag_part)

def display_question(number):
    # Display the question to the user
    print("Perform the following operation:")
    print(f"({number.real} + {number.imag}j)^2")

def get_user_answer():
    # Get user's answer for the complex number squared
    try:
        real_answer = int(input("Enter the real part of the result: "))
        imag_answer = int(input("Enter the imaginary part of the result: "))
        return complex(real_answer, imag_answer)
    except ValueError:
        print("Invalid input. Please enter integers.")
        return None

def main():
    print("Welcome to the Complex Math Game!")

    score = 0
    num_questions = 5

    for _ in range(num_questions):
        # Generate a random complex number
        complex_number = generate_complex_number()

        # Display the question
        display_question(complex_number)

        # Get user's answer
        user_answer = get_user_answer()

        # Check if the answer is correct
        if user_answer is not None and cmath.isclose((complex_number**2), user_answer):
            print("Correct!\n")
            score += 1
        else:
            print(f"Sorry, the correct answer is ({complex_number.real**2 - complex_number.imag**2} + {2 * complex_number.real * complex_number.imag}j).\n")

    print(f"Game Over! Your score is {score}/{num_questions}.")

if __name__ == "__main__":
    main()
