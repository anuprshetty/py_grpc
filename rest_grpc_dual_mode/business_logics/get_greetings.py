# BUSINESS LOGIC function
def get_greetings(input_message):

    output_message = f"Here is your greetings --> "

    for key, value in input_message.items():
            output_message += f"({key}, {value})"

    return output_message
# BUSINESS LOGIC function