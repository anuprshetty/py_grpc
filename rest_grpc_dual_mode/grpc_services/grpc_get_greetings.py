from .grpc_utilities.generated import rest_grpc_dual_mode_pb2_grpc as pb2_grpc
from .grpc_utilities.generated import rest_grpc_dual_mode_pb2 as pb2
from business_logics.get_greetings import get_greetings
from google.protobuf import json_format


class GreetingsGeneratorService(pb2_grpc.GreetingsGeneratorServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GRPCGetGreetings(self, request, context):

        # GRPC REQUEST UNPACKING LOGIC
        request_info = json_format.MessageToDict(request)
        # GRPC REQUEST UNPACKING LOGIC

        # BUSINESS LOGIC FUNCTION
        response_info = get_greetings(**request_info)
        # BUSINESS LOGIC FUNCTION

        # GRPC RESPONSE PACKING LOGIC
        response = pb2.ResponseMessage(**response_info)
        # GRPC RESPONSE PACKING LOGIC

        return response
