"""
BMI Calculator

A simple command-line BMI calculator that:
- Accepts weight and height input
- Calculates BMI
- Categorizes BMI
- Handles invalid inputs

Author: Muhammad Mubashar
"""
def calculate_bmi(weight, height):
    """Calculate BMI."""
    return weight / (height ** 2)


def get_bmi_category(bmi):
    """Determine BMI category."""
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    try:
        # Get user input
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (m): "))

        # Validate input
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Get category
        category = get_bmi_category(bmi)

        # Display result
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")


if __name__ == "__main__":
    main()