import requests
from dotenv import load_dotenv
import os

# Загружаем переменные из .env файла
load_dotenv()


class ProjectsAPI:

    def __init__(self):
        # Получаем BASE_URL и API_TOKEN из переменных окружения
        self.BASE_URL = os.getenv("BASE_URL")
        self.API_TOKEN = os.getenv("API_TOKEN")

        # Устанавливаем заголовки с авторизацией
        self.headers = {
            "Authorization": f"Bearer {self.API_TOKEN}",
            "Content-Type": "application/json"
        }

    def create_project(self, payload):
        """Создать проект."""
        url = f"{self.BASE_URL}/projects"
        return requests.post(url, json=payload, headers=self.headers)

    def get_all_projects(self):
        """Получить все проекты."""
        url = f"{self.BASE_URL}/projects"
        return requests.get(url, headers=self.headers)

    def get_project_by_id(self, project_id):
        """Получить проект по ID."""
        url = f"{self.BASE_URL}/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(self, project_id, payload):
        """Обновить проект по ID."""
        url = f"{self.BASE_URL}/projects/{project_id}"
        return requests.put(url, json=payload, headers=self.headers)