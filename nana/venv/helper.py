def day_to_units(num_of_days, conversion_unit):
        if conversion_unit == "hours":
            return f"{num_of_days} days are {num_of_days * 24} {conversion_unit}"
        elif conversion_unit == "minutes":
            return f"{num_of_days} days are {num_of_days * 24 * 60} {conversion_unit}"
        else:
            return "unsupported unit"

def validate_and_execute(days_and_units_dictionary):
    try:
        user_input_number = int(days_and_units_dictionary["days"])
        # we want to do conversion only for positive intergers
        if user_input_number > 0:
            calculated_value = day_to_units(user_input_number, days_and_units_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print ("you enter a 0, please enter a valid number") 
        else:
            print ("your entered a negative value, so no conversion for you!")
    except ValueError:
        print("your input is not a valid number, dont ruin ruin my program")

user_input_message = "Hey User, enter number of days and conversion unit!\n"