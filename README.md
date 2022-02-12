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

## REST and gRPC Dual Mode

This POC shows working simultaneously with both REST and gRPC services listening at different ports in the same application.

### Advantages of REST and gRPC Dual Mode POC

- Decouples core business logic and data communication logic (SOAP, REST, gRPC, etc.).
- Application can be extended to any type of data communication format with minimal changes without affecting business logic.
- Generalizing application structure (standardization) which brings many possibilities and helps in many scenarios like...
  - Supporting many data communication formats at a time.
  - Migrating from one data communication format to another with minimal effort, taking one chunk at a time. No need to convert all services to another format in one go. Which helps in backward compatibility for older data communication format without affecting the application functionalities.

## Load Testing using Locust Tool

Locust tool is used to perform load testing on the application via both REST and gRPC communication.  
**Based on the Locust performance reports, I found that performance of gRPC communication is much better than the performance of REST communication.**  

**Reports Path:** *rest_grpc_dual_mode/tests/load_tests/reports/*

### Locust Commands

- [OPTIONAL] python -m grpc_tools.protoc --proto_path=./protobufs ./protobufs/rest_grpc_dual_mode.proto --python_out=./rest_grpc_dual_mode/tests/load_tests/grpc/generated --grpc_python_out=./rest_grpc_dual_mode/tests/load_tests/grpc/generated
- [For REST] locust -f rest_grpc_dual_mode/tests/load_tests/rest/rest_load_test.py --host http://localhost:5000 --users <MAX_USERS> --spawn-rate <NO_OF_USERS_TO_ADD_PER_SEC>
- [For gRPC] locust -f rest_grpc_dual_mode/tests/load_tests/grpc/grpc_load_test.py --host http://localhost:50051 --users <MAX_USERS> --spawn-rate <NO_OF_USERS_TO_ADD_PER_SEC>

## References

- [Implementing gRPC In Python](https://www.velotio.com/engineering-blog/grpc-implementation-using-python)
- [gRPC documentation](https://grpc.io/docs/what-is-grpc/)
- [Python gRPC documentation](https://grpc.io/docs/languages/python/)
- [Python gRPC API reference](https://grpc.github.io/grpc/python/)
- [Protocol Buffers](https://developers.google.com/protocol-buffers)
- [gRPC Motivation and Design Principles](https://www.grpc.io/blog/principles/)
- [BloomRPC tool - GUI Client for GRPC Services](https://appimage.github.io/BloomRPC/)
- [Werkzeug - Werkzeug is a comprehensive WSGI web application library](https://werkzeug.palletsprojects.com/en/2.0.x/)
- [Locust Tool](https://locust.io/)
- [Locust Documentation](http://docs.locust.io/en/stable/#)
- [Locust - Testing non-HTTP systems (gRPC)](https://docs.locust.io/en/latest/testing-other-systems.html#)
- [gRPC benchmarking and load testing tool](https://ghz.sh/)
