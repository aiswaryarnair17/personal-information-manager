Personal Information Manager
Project Overview and Objectives
Overview

The Personal Information Manager is a console-based Python application developed to collect, validate, process, and display user personal information in a structured format.

The application demonstrates fundamental programming concepts including modular design, input validation, exception handling, and formatted output.

This project serves as an introductory-level implementation of structured Python programming.

Objectives

The main objectives of this project were:

To understand and implement variables for different data types

To handle user input dynamically

To implement validation to prevent incorrect or empty data

To use exception handling (try-except) for robust execution

To organize code using functions (modular programming)

To apply arithmetic logic (age to months conversion)

To display formatted output using f-strings

Setup and Installation Instructions
Requirements

Python 3.x

Git (for version control)

VS Code (recommended IDE)

Installation Steps

Clone the repository:

git clone https://github.com/yourusername/personal-information-manager.git


Navigate to project folder:

cd personal-information-manager


Run the application:

python personal_info.py


OR

python3 personal_info.py

Code Structure Explanation
Project Structure
personal-information-manager/
│
├── personal_info.py
└── README.md

Program Architecture

The program is structured using modular functions:

## 1. get_valid_age()

Accepts age input

Uses try-except to handle invalid numeric entries

Prevents negative or zero values

Ensures valid integer return

## 2. get_non_empty_input(prompt)

Prevents empty input

Uses a loop until valid input is entered

Trims whitespace using .strip()

## 3. display_information(...)

Calculates age in months

Formats output using f-strings

Displays clean structured layout

## 4. main()

Controls overall program flow

Calls input and display functions

Maintains separation of logic

## 5. Execution Control
if __name__ == "__main__":
    main()


Ensures script runs only when executed directly.

Screenshots of Working Application
Screenshot 1 – Input Stage

The program prompts the user for personal details including name, age, city, hobby, favorite food, and favorite color.

Example:

Welcome to Personal Information Manager!

Enter your name: Aiswarya R Nair

Enter your age: 22

Enter your city: jaipur

Enter your hobby: singing

Enter your favorite food: biriyani

## Sample output

===================================
        PERSONAL INFORMATION
===================================
Name: Aiswarya R Nair

Age: 22 (264 months old)

City: jaipur

Hobby: singing

Favorite Food: biriyani

Favorite Color: yellow

===================================
Thank you for using the program!  

## Explanation of Technical Requirements Fulfillment
1. Variables

Used variables to store:

Name (string)

Age (integer)

City (string)

Hobby (string)

Favorite food (string)

Favorite color (string)

2. Input / Output

Used input() to collect user data.

Used print() to display formatted results.

3. String Formatting

Used f-strings for dynamic output formatting:

print(f"Age: {age} ({age * 12} months old)")


This improves readability and structure.

4. Error Handling

Implemented try-except block:

except ValueError:
    print("Please enter a valid number for age.")


Prevents program crash due to invalid input.

5. Input Validation

Prevents empty input

Ensures valid numeric age

Re-prompts user until valid data is entered

6. Calculation Logic

Age conversion:

age_in_months = age * 12


Demonstrates basic arithmetic operation implementation.

## Conclusion

The Personal Information Manager successfully demonstrates structured programming principles, user interaction handling, error management, and modular code organization.

This project builds a strong foundation for advanced Python applications such as:

File handling systems

Database-based applications

GUI applications

Menu-driven programs

## Technologies Used
- Python 3

## How to Run
1. Clone the repository
2. Navigate to project folder
3. Run:
   python personal_info.py

## Author
Aiswarya R Nair
