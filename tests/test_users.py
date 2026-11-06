import pytest

def user_payload(
    equipment_id = "999",
    student_id = "ST-AB1234",
    description = "student equipment maintenance",
    priority = "2"
):
    return {
        "equipment_id": equipment_id,
        "student_id": student_id,
        "description": description,
        "priority": priority,
    }

def test_create_user_returns_201(client):
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()

    assert data["equipment_id"] == "999"
    assert data["description"] == "student equipment maintenance"
    assert data["priority"] == "2"

def test_get_user_returns_422(client):
    response = client.post(
        "/api/users",
        json=user_payload(
            student_id = "1234567"
        )
    )

    assert response.status_code == 422

def test_get_users(client):
    client.post("/api/users", json=user_payload())
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 200

    assert len(
        response.json()
        ) == 1
    
    assert response.json()[0]["student_id"] == "ST-AB1234"

def test_get_priority_users(client):
    client.post("/api/users", json=user_payload())
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 200

    assert len(
        response.json()
        ) == 1

    assert response.json()[0]["priority"] == "1" 

def test_get_priority_user_returns_422(client):
    response = client.post(
        "/api/users",
        json=user_payload(
            priority = "5"
        )
    )

    assert response.status_code == 422  

@pytest.mark.parametrize(
    "bad_sid",
    [
        "dwopd093"
        "dw90003"
        "dwo"
        "dwopd093"
    ],
)

def test_invalid_student_id_returns_422(client, bad_sid):
    response = client.post(
        "/api/users", 
        json = user_payload(
            student_id = bad_sid),
        )
    assert response.status_code == 422








    

