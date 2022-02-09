import grpc
import os
from concurrent import futures
from .generated import rest_grpc_dual_mode_pb2_grpc as pb2_grpc
from .generated import rest_grpc_dual_mode_pb2 as pb2
from ..grpc_get_greetings import GreetingsGeneratorService


grpc_max_workers = os.getenv("GRPC_MAX_WORKERS")
if not grpc_max_workers:
    grpc_max_workers = 1
grpc_max_workers = int(grpc_max_workers)

grpc_port = os.getenv("GRPC_PORT")
if not grpc_port:
    grpc_port = 50051

print(f"grpc_max_workers: {grpc_max_workers}")
print(f"grpc_port: {grpc_port}")


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=grpc_max_workers))
    pb2_grpc.add_GreetingsGeneratorServicer_to_server(GreetingsGeneratorService(), server)
    server.add_insecure_port(f'[::]:{grpc_port}')
    server.start()
    print(f"gRPC Server is running at port {grpc_port}...")
    return server