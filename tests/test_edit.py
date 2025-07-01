import pytest
from unittest.mock import patch, MagicMock
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["PROPAGATE_EXCEPTIONS"] = True
    with app.test_client() as client:
        yield client

@patch("services.functions.conection_userprofile")
@patch("main.jwt.decode")
def test_update_profile_success(mock_jwt_decode, mock_con_userprofile, client):
    # Simulted JWT decode
    mock_jwt_decode.return_value = {"user_id": 123}

    # Simulate database session and user profile
    mock_session = MagicMock()
    mock_con_userprofile.return_value = mock_session

    fake_profile = MagicMock()
    mock_session.query().filter_by().first.return_value = fake_profile

    # Data for the request
    data = {
        "Description": "Test perdonal description",
        "Id_preferences": 2,
        "Id_type": 3
    }

    response = client.patch(
        "/update-profile",
        headers={"Authorization": "Bearer fake.jwt.token"},
        json=data
    )

    assert response.status_code == 200
    assert response.get_json()["message"] == "Profile updated successfully"
