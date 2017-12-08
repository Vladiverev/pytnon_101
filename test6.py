# Import the base64 encoding library.
import base64
import requests
import json
import argparse
import shutil
import time


# Pass the image data to an encoding function.
def encode_image(image):
    with open(image, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('UTF-8')


def parsed_string(image):
    response = requests.post(
        url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCCFzMrLK-J2YV9_CqtUBrhsanet0pXyzc',
        json={"requests": [{"image": {"content": encode_image(image)},
                            "features": [{"type": "LABEL_DETECTION"}]}]},
        headers={'Content-Type': 'application/json'})
    return json.loads(response.text)


def get_key(image, value):
    i = 0
    key = []
    while i < 5:
        key.append(parsed_string(image)['responses'][0]['labelAnnotations'][i]['description'])
        i += 1
    print(key)
    for item in key:
        if item == value:
            return True


def sort(image):
    contents = open('contents.txt', 'a')
    #image = 't.jpg'
    if get_key(image, 'text') == True:
        shutil.copy2(image, './text/' + time.strftime("%b_%d_%Y_%H_%M_") + image)
        contents.write(time.strftime("%b_%d_%Y_%H_%M_") + image + ' in folder Text\n')
        print('Text')
    elif get_key(image, 'fauna') == True:
        shutil.copy2(image, './fauna/' + time.strftime("%b_%d_%Y_%H_%M_") + image)
        contents.write(time.strftime("%b_%d_%Y_%H_%M_") + image + ' in folder Fauna\n')
        print('Fauna')
    else:
        shutil.copy2(image, './other/' + time.strftime("%b_%d_%Y_%H_%M_") + image)
        contents.write(time.strftime("%b_%d_%Y_%H_%M_") + image + ' in folder Other\n')
        print('Other')
    contents.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Сделать скригщот -s, '
                                                 'Оотсортировать картинку -i name.jpg, '
                                                 'распознать текст -t -name.jpg, ')
    parser.add_argument('-i', '--image', required=True)
    args = parser.parse_args()
    print(args)
    sort(args.image)

