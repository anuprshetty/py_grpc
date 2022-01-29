# BUSINESS LOGIC function
def get_greetings(data_comm_type, input_message):

    output_message = f"Here is your greetings --> "

    for key, value in input_message.items():
            output_message += f"({key}, {value})"

    print(f"{data_comm_type}: {output_message}")
    return output_message
# BUSINESS LOGIC function