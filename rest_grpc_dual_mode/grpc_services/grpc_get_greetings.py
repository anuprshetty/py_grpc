from .grpc_utilities import rest_grpc_dual_mode_pb2_grpc as pb2_grpc
from .grpc_utilities import rest_grpc_dual_mode_pb2 as pb2
from business_logics.get_greetings import get_greetings


class GreetingsGeneratorService(pb2_grpc.GreetingsGeneratorServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GRPCGetGreetings(self, request, context):

        # GRPC REQUEST UNPACKING LOGIC
        request_message = request
        input_message = {"type": request_message.type, "year": request_message.year}
        # GRPC REQUEST UNPACKING LOGIC

        # BUSINESS LOGIC function
        output_message = get_greetings(input_message)
        # BUSINESS LOGIC function

        # GRPC RESPONSE PACKING LOGIC
        response_message = output_message
        # GRPC RESPONSE PACKING LOGIC

        return pb2.ResponseMessage(message=response_message)
