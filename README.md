# Py_gRPC

Implementation of gRPC in Python.

## System Requirements

- Ubuntu 20.04 LTS
- Python 3.6.15
- python3-virtualenv

## Project Setup and Execution

- clone py_grpc project
- cd py_grpc
- virtualenv -p /usr/bin/python3.6 venv
- source venv/bin/activate
- pip install -r requirements.txt

### Unary gRPC

This is a simple gRPC which works like a normal function call. It sends a single request declared in the .proto file to the server and gets back a single response from the server.

### Unary gRPC Setup and Execution

- [OPTIONAL] python -m grpc_tools.protoc --proto_path=./protobufs ./protobufs/unary.proto --python_out=./unary_grpc --grpc_python_out=./unary_grpc
- In one terminal --> python ./unary_grpc/unary_server.py
- In another terminal --> python ./unary_grpc/unary_client.py

### Bidirectional gRPC

Both gRPC client and the gRPC server use a read-write stream to send a message sequence. Both operate independently, so gRPC clients and gRPC servers can write and read in any order they like, i.e. the server can read a message then write a message alternatively, wait to receive all messages then write its responses, or perform reads and writes in any other combination.

NOTE: gRPC guarantees the ordering of messages within an individual RPC call. In the case of Bidirectional streaming, the order of messages is preserved in each stream.

### Bidirectional gRPC Setup and Execution

- [OPTIONAL] python -m grpc_tools.protoc --proto_path=./protobufs ./protobufs/bidirectional.proto --python_out=./bidirectional_grpc --grpc_python_out=./bidirectional_grpc
- In one terminal --> python ./bidirectional_grpc/bidirectional_server.py
- In another terminal --> python ./bidirectional_grpc/bidirectional_client.py

## References

- [Implementing gRPC In Python](https://www.velotio.com/engineering-blog/grpc-implementation-using-python)
