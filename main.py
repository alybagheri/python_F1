from helper import validate_and_execution, user_input_message

user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_units = user_input.split(":")
    print(days_and_units)
    days_and_units_dictionary = {"days": days_and_units[0], "unit": days_and_units[1]}
    print(days_and_units_dictionary)
    print(type(days_and_units_dictionary))
    validate_and_execution(days_and_units_dictionary)


