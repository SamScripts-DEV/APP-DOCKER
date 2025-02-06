from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    # Tiempo de espera entre tareas (en segundos)
    wait_time = between(1, 3)

    @task
    def submit_form(self):
        # Simular el envío del formulario con datos de prueba
        self.client.post("/", {
            "first_name": "Locust",
            "last_name": "User",
            "phone": "1234567890",
            "email": "locust@example.com",
            "project_idea": "This is a test message from Locust."
        })

    @task(3)  # Esta tarea se ejecutará 3 veces más que la anterior
    def view_responses(self):
        # Simular la visualización de respuestas
        self.client.get("/")

    @task(2)
    def view_page(self):
        # Simular la visualización de la página de inicio
        self.client.get("/")

