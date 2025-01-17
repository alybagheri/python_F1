def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} hours"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} minutes"
    elif conversion_unit == "secound":
        return f"{number_of_days} days are {number_of_days * 24 * 60 * 60} secound"
    else:
        return "unsupported unit"
def validate_and_execution(days_and_units_dictionary):
    try:

        user_input_number = int(days_and_units_dictionary["days"])
        if user_input_number > 0:
                calculated_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
                print(calculated_value)
        elif user_input_number == 0:
                calculated_value = days_to_units(user_input_number, days_and_units_dictionary["unit"])
                print(calculated_value)
        else:
            print("You entered a negative number, please give me positive numb")
    except ValueError:
        print("your input is not a number. Do not ruin my app please")




user_input_message = "hey user, enter a random number and a valid unit!\n"