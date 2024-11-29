# Позитивные тесты

def test_create_project(api):
    valid_project_payload = {'title': 'Test Project'}
    response = api.create_project(valid_project_payload)
    assert response.status_code == 201, f"Expected 201, got {response.status_code}"


def test_get_all_projects(api):
    response = api.get_all_projects()
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert len(response.json()) > 0, "No projects found"


def test_get_project_by_id(api):
    valid_project_payload = {'title': 'Test Project'}
    create_response = api.create_project(valid_project_payload)
    project_id = create_response.json().get('id')
    response = api.get_project_by_id(project_id)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_update_project(api):
    valid_project_payload = {'title': 'Updated Project'}
    create_response = api.create_project(valid_project_payload)
    project_id = create_response.json().get('id')
    updated_payload = {'title': 'Updated Project Name'}
    response = api.update_project(project_id, updated_payload)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


# Негативные тесты

def test_create_project_missing_title(api):
    invalid_payload = {}
    response = api.create_project(invalid_payload)
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"


def test_get_project_by_invalid_id(api):
    response = api.get_project_by_id('invalid-id')
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"


def test_update_project_with_invalid_id(api):
    invalid_project_id = 'nonexistent-id'
    updated_payload = {'title': 'Updated Title'}
    response = api.update_project(invalid_project_id, updated_payload)
    assert response.status_code == 404, f"Expected 404, got {response.status_code}"


def test_create_project_invalid_title(api):
    invalid_payload = {'title': 12345}
    response = api.create_project(invalid_payload)
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"