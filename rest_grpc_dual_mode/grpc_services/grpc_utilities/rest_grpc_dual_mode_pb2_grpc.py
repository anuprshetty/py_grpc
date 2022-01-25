# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import rest_grpc_dual_mode_pb2 as rest__grpc__dual__mode__pb2


class GreetingsGeneratorStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GRPCGetGreetings = channel.unary_unary(
                '/rest_grpc_dual_mode.GreetingsGenerator/GRPCGetGreetings',
                request_serializer=rest__grpc__dual__mode__pb2.RequestMessage.SerializeToString,
                response_deserializer=rest__grpc__dual__mode__pb2.ResponseMessage.FromString,
                )


class GreetingsGeneratorServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GRPCGetGreetings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetingsGeneratorServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GRPCGetGreetings': grpc.unary_unary_rpc_method_handler(
                    servicer.GRPCGetGreetings,
                    request_deserializer=rest__grpc__dual__mode__pb2.RequestMessage.FromString,
                    response_serializer=rest__grpc__dual__mode__pb2.ResponseMessage.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'rest_grpc_dual_mode.GreetingsGenerator', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GreetingsGenerator(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GRPCGetGreetings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/rest_grpc_dual_mode.GreetingsGenerator/GRPCGetGreetings',
            rest__grpc__dual__mode__pb2.RequestMessage.SerializeToString,
            rest__grpc__dual__mode__pb2.ResponseMessage.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
