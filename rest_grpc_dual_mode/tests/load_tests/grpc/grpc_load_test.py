from locust import User, task, constant
import grpc
import time
from generated import rest_grpc_dual_mode_pb2_grpc as pb2_grpc
from generated import rest_grpc_dual_mode_pb2 as pb2
from grpc_utilities.locust_grpc_wrapper import LocustGRPCWrapper

# patch grpc so that it uses gevent instead of asyncio
import grpc.experimental.gevent as grpc_gevent
grpc_gevent.init_gevent()


class GRPCUser(User):
	wait_time = constant(0)

	def __init__(self, environment):
		super().__init__(environment)
		self.environment = environment
		self.locust_grpc_wrapper = None
		self._channel = None
		self._channel_closed = True

		self.grpc_rpcs = {
			"GRPCGetGreetings": {
				"request_info": {
					"dataCommType": "gRPC",
					"messageType": "Diwali",
					"year": 2023
				}
			}
		}

	def on_start(self):
		""" on_start is called when a Locust start before any task is scheduled """

		# GRPC COMMUNICATION SETUP
		self._channel = grpc.insecure_channel('localhost:50051')
		self._channel_closed = False
		stub = pb2_grpc.GreetingsGeneratorStub(self._channel)
		self.locust_grpc_wrapper = LocustGRPCWrapper(self.environment, stub)
		# GRPC COMMUNICATION SETUP

	def on_stop(self):
		""" on_stop is called when the TaskSet is stopping """
		self._channel_closed = True
		time.sleep(1)
		self._channel.close()
		super().stop(force=True)

	@task
	def grpc_get_greetings(self):
		if not self._channel_closed:
			request = pb2.RequestMessage(**self.grpc_rpcs["GRPCGetGreetings"]["request_info"])
			self.locust_grpc_wrapper.GRPCGetGreetings(request)
