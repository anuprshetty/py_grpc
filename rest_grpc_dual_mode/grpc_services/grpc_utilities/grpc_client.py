import grpc
from generated import rest_grpc_dual_mode_pb2_grpc as pb2_grpc
from generated import rest_grpc_dual_mode_pb2 as pb2
from google.protobuf import json_format


if __name__ == '__main__':

    # GRPC COMMUNICATION SETUP
    print('gRPC client started...')
    channel = grpc.insecure_channel('localhost:50051')
    stub = pb2_grpc.GreetingsGeneratorStub(channel)
    # GRPC COMMUNICATION SETUP

    # GRPC PRE-PROCESSING
    request_info = {
        "dataCommType": "gRPC",
        "messageType": "Holi",
        "year": 2021
    }
    print(f'request_info:\n {request_info}')
    request = pb2.RequestMessage(**request_info)
    # GRPC PRE-PROCESSING

    # GRPC SERVICE
    response = stub.GRPCGetGreetings(request)
    # GRPC SERVICE

    # GRPC POST-PROCESSING
    response_json_string = json_format.MessageToJson(response)
    print(f'response_json_string:\n {response_json_string}')
    response_info = json_format.MessageToDict(response)
    print(f'response_info:\n {response_info}')
    # GRPC POST-PROCESSING
