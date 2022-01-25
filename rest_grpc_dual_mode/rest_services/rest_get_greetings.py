from __main__ import app
from flask import request
import json
from business_logics.get_greetings import get_greetings


@app.route("/v1/get_greetings", methods=['GET', 'POST'])
def rest_get_greetings():

    # REST REQUEST UNPACKING LOGIC
    greetings_info = {}

    if request.method == 'GET':
        greetings_info = request.args # Query Strings --> ImmutableMultiDict.
    else: # POST method
        greetings_info = json.loads(request.data)

    input_message = greetings_info
    # REST REQUEST UNPACKING LOGIC

    # BUSINESS LOGIC function
    output_message = get_greetings(input_message)
    # BUSINESS LOGIC function

    # REST RESPONSE PACKING LOGIC
    response = output_message
    # REST RESPONSE PACKING LOGIC

    return response
