from flask import Flask
from grpc_services.grpc_utilities import grpc_server


app = Flask(__name__)
rest_port = 5000

from rest_services import rest_get_greetings

if __name__ == "__main__":
    grpc_server = grpc_server.serve()
    # server.wait_for_termination()
    print(f"REST Server is running at port {rest_port}...")
    app.run(host='0.0.0.0', port=rest_port, debug=True)
