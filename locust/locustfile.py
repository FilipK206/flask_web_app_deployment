from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def temperature_conversion(self):
        self.client.get("/convert/50")
