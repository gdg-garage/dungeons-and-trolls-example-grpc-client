import logging
import sys

import grpc

import dungeonsandtrolls_pb2
import dungeonsandtrolls_pb2_grpc

SERVER_ADDRESS = "localhost:8081"


def game():
    with grpc.insecure_channel(SERVER_ADDRESS) as channel:
        stub = dungeonsandtrolls_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(dungeonsandtrolls_pb2.HelloRequest(name='name'))
        logging.info("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    game()
