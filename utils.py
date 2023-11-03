class Request:
    def __init__(self, id: int, role: str):
        self.id = id
        self.role = role

    def __str__(self):
        return f"Request ID: {self.id}, Role: {self.role}"