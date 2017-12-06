import requests

data = open('1.json', 'rb')
response = requests.post(url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCCFzMrLK-J2YV9_CqtUBrhsanet0pXyzc',
    data=data,
    headers={'Content-Type': 'application/json'})
print(response.text)
