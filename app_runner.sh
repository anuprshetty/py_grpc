#!/bin/bash

# Execute this script with following commands.
# Commands:
# [ONE_TIME] chmod 777 path/to/app_runner.sh
# [EVERY_TIME] source path/to/app_runner.sh path/to/app_runner.sh

script_path="$PWD/$1" &&
    script_dir="$(dirname "$script_path")" &&
    cd "$script_dir" &&
    source venv/bin/activate &&
    # pip install -r requirements.txt &&
    # python -m grpc_tools.protoc --proto_path=./protobufs ./protobufs/rest_grpc_dual_mode.proto --python_out=./rest_grpc_dual_mode/grpc_services/grpc_utilities/generated --grpc_python_out=./rest_grpc_dual_mode/grpc_services/grpc_utilities/generated &&
    # python -m grpc_tools.protoc --proto_path=./protobufs ./protobufs/rest_grpc_dual_mode.proto --python_out=./rest_grpc_dual_mode/tests/load_tests/grpc/generated --grpc_python_out=./rest_grpc_dual_mode/tests/load_tests/grpc/generated # &&
    python ./rest_grpc_dual_mode/app.py
