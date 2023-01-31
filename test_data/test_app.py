import io
import pytest

def test_infer_image(client):
    image_path = "test_data/NORMAL-10188061.jpg"
    with open(image_path, "rb") as f:
        data = f.read()
    response = client.post("/predict", data={"file": (io.BytesIO(data), "test.jpg")})
    assert response.status_code == 200
    assert b"NORMAL" in response.data.lower()
