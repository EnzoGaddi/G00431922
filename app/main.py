from fastapi import Depends, FastAPI

app = FastAPI(title="Example template")

@app.get("/health")
def health():
    return{"status": "ok"}

# response = client.post(
#     "/api/users",
#     json=user_payload(
#         student_id = "1234567"
#     )
# )

# assert response.status_code == 422
