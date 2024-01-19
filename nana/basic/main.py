calculation_to_units = 24
name_of_unit = "hours"


def day_to_units(num_of_days):
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    elif num_of_days == 0:
        return "you enter a 0, please enter a valid number"
    else:
        return "your entered a negative value, so no conversion for you!"

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        calculated_value = day_to_units(user_input_number)
        print(calculated_value)
    else:
        print("your input is not a valid number, dont ruin ruin my program")

# my_var = day_to_units(20)
# print(my_var)
user_input = input("Hey user, enter a number of days and i will convert it to hours!\n")
validate_and_execute()


