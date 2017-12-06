import requests

response = requests.post(
    url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCCFzMrLK-J2YV9_CqtUBrhsanet0pXyzc',
    json={"requests": [{"image": {"source": {"imageUri": "https://storage.googleapis.com/1234v/captcha2.jpg"}},
                        "features": [{"type": "TEXT_DETECTION"}]}]},
    headers={'Content-Type': 'application/json'})

print(response.text)