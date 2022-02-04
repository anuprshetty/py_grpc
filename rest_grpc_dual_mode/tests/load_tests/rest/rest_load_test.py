from locust import HttpUser, task, constant


class RestUser(HttpUser):
	wait_time = constant(0)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.rest_apis = {
			"rest_get_greetings": {
				"url": "/v1/get_greetings",
				"post_data": {
					"dataCommType": "REST",
					"messageType": "Diwali",
					"year": 2023
				}
			}
		}

	def on_start(self):
		""" on_start is called when a Locust start before any task is scheduled """
		pass

	def on_stop(self):
		""" on_stop is called when the TaskSet is stopping """
		pass

	@task
	def rest_get_greetings(self):
		self.client.post(
			url=self.rest_apis["rest_get_greetings"]["url"],
			json=self.rest_apis["rest_get_greetings"]["post_data"]
		)
