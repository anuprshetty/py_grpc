from __main__ import app
from flask import request
import json
from business_logics.get_greetings import get_greetings


@app.route("/v1/get_greetings", methods=['GET', 'POST'])
def rest_get_greetings():

    # REST REQUEST UNPACKING LOGIC
    request_info = {}

    if request.method == 'GET':
        request_info = request.args # Query Strings --> ImmutableMultiDict.
    else: # POST method
        request_info = json.loads(request.data)
    # REST REQUEST UNPACKING LOGIC

    # BUSINESS LOGIC FUNCTION
    response_info = get_greetings(**request_info)
    # BUSINESS LOGIC FUNCTION

    # REST RESPONSE PACKING LOGIC
    response = json.dumps(response_info)
    # REST RESPONSE PACKING LOGIC

    return response
