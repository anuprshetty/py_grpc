import time
import grpc


class LocustGRPCWrapper:
	def __init__(self, environment, stub):
		self.environment = environment
		self._stub_class = stub.__class__
		self._stub = stub

	def __getattr__(self, name):
		func = self._stub_class.__getattribute__(self._stub, name)

		def wrapper(*args, **kwargs):

			request_meta = {
				"request_type": "gRPC",
				"name": name,
				"start_time": time.time(),
				"response_length": 0,
				"exception": None,
				"context": None,
				"response": None,
			}
			start_perf_counter = time.perf_counter()
			try:
				request_meta["response"] = func(*args, **kwargs)
			except grpc.RpcError as e:
				request_meta["exception"] = e
			# response_time in ms (milli seconds)
			request_meta["response_time"] = (time.perf_counter() - start_perf_counter) * 1000
			self.environment.events.request.fire(**request_meta)
			return request_meta["response"]

		return wrapper
