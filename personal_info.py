def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age <= 0:
                print("Age must be greater than 0.")
            else:
                return age
        except ValueError:
            print("Please enter a valid number for age.")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value == "":
            print("This field cannot be empty. Please enter a value.")
        else:
            return value


def display_information(name, age, city, hobby, favorite_food, favorite_color):
    age_in_months = age * 12

    print("\n===================================")
    print("        PERSONAL INFORMATION       ")
    print("===================================")
    print(f"Name: {name}")
    print(f"Age: {age} ({age_in_months} months old)")
    print(f"City: {city}")
    print(f"Hobby: {hobby}")
    print("\nFavorite Food:", favorite_food)
    print("Favorite Color:", favorite_color)
    print("===================================")
    print("Thank you for using the program!")


def main():
    print("Welcome to Personal Information Manager!\n")

    name = get_non_empty_input("Enter your name: ")
    age = get_valid_age()
    city = get_non_empty_input("Enter your city: ")
    hobby = get_non_empty_input("Enter your hobby: ")
    favorite_food = get_non_empty_input("Enter your favorite food: ")
    favorite_color = get_non_empty_input("Enter your favorite color: ")

    display_information(name, age, city, hobby, favorite_food, favorite_color)


if __name__ == "__main__":
    main()
