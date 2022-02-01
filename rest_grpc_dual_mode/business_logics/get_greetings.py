# BUSINESS LOGIC function
def get_greetings(dataCommType, messageType, year):

    greetings = f"Here is your greetings --> Today is a special day! ({messageType}, {year})"
    print(f"{dataCommType}: {greetings}")

    response_info = {"greetings": greetings, "messageReceived": True}

    return response_info
# BUSINESS LOGIC function