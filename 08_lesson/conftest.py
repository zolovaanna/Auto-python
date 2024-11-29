import pytest
from api import ProjectsAPI


@pytest.fixture(scope="session")
def api():
    """Инициализация API клиента с токеном из переменных окружения."""
    return ProjectsAPI()


@pytest.fixture
def valid_project_payload():
    """Корректные данные для создания проекта."""
    return {"name": "Test Project", "description": "This is a test project"}


@pytest.fixture
def invalid_project_payload():
    """Некорректные данные (отсутствие обязательных полей)."""
    return {"description": "Missing required fields"}