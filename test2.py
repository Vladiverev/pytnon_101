# Import the base64 encoding library.
import base64
import requests


# Pass the image data to an encoding function.
def encode_image(image):
    with open(image, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('UTF-8')



response = requests.post(
    url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCCFzMrLK-J2YV9_CqtUBrhsanet0pXyzc',
    json={"requests": [{"image": {"content": encode_image('d.jpg')},
                        "features": [{"type": "LABEL_DETECTION"}]}]},
    headers={'Content-Type': 'application/json'})

print(response.text)
