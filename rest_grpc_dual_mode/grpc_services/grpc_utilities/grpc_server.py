import grpc
from concurrent import futures
from . import rest_grpc_dual_mode_pb2_grpc as pb2_grpc
from . import rest_grpc_dual_mode_pb2 as pb2
from ..grpc_get_greetings import GreetingsGeneratorService


def serve():
    grpc_port = 50051
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_GreetingsGeneratorServicer_to_server(GreetingsGeneratorService(), server)
    server.add_insecure_port(f'[::]:{grpc_port}')
    server.start()
    print(f"gRPC Server is running at port {grpc_port}...")
    return server