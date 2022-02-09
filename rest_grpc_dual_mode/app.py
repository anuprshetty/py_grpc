from flask import Flask
from grpc_services.grpc_utilities import grpc_server


app = Flask(__name__)
rest_port = 5000

grpc_server_handler = grpc_server.serve()
# grpc_server_handler.wait_for_termination()

from rest_services import rest_get_greetings

if __name__ == "__main__":
    print(f"REST Server is running at port {rest_port}...")
    app.run(host='0.0.0.0', port=rest_port, debug=True)
