from locust import HttpUser, task, between, tag

# Defining a custom Locust user class
class WebsiteUser(HttpUser):
    # Setting the wait time between requests
    wait_time = between(1, 3)

    @tag('flask')
    @task
    def temperature_conversion(self):
        self.client.get("/convert/50")

    @tag('tf')
    @task
    def temperature_prediction(self):
        # Sending a POST request to the model's prediction endpoint
        self.client.post("/v1/models/saved_model:predict", json={"instances": [100, 50, 10 ]})
        