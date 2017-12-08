import base64
import requests
import json
import argparse
import shutil
from PIL import ImageGrab
import time


# Pass the image data to an encoding function.
def encode_image(image):
    with open(image, 'rb') as image_file:
        return base64.b64encode(image_file.read()).decode('UTF-8')


# image
def parsed_str(image):
    response = requests.post(
        url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCCFzMrLK-J2YV9_CqtUBrhsanet0pXyzc',
        json={"requests": [{"image": {"content": encode_image(image)},
                            "features": [{"type": "LABEL_DETECTION"}]}]},
        headers={'Content-Type': 'application/json'})
    return json.loads(response.text)


def get_key(ki, value):
    i = 0
    key = []
    while i < 5:
        key.append(parsed_str(ki)['responses'][0]['labelAnnotations'][i]['description'])
        i += 1
    print(key)
    for item in key:
        if item == value:
            return True


def sort(image):
    if get_key(image, 'text') == True:
        text_save(image)
        print('Text')
    elif get_key(image, 'fauna') == True:
        shutil.copy2(image, './fauna/' + time.strftime("%b_%d_%Y_%H_%M_") + image)
        contents(image, 'fauna')
        print('Fauna')
    else:
        shutil.copy2(image, './other/' + time.strftime("%b_%d_%Y_%H_%M_") + image)
        contents(image, 'other')
        print('Other')


# text
def parsed_string(imt):
    response = requests.post(
        url='https://vision.googleapis.com/v1/images:annotate?key=AIzaSyCCFzMrLK-J2YV9_CqtUBrhsanet0pXyzc',
        json={"requests": [{"image": {"content": encode_image(imt)},
                            "features": [{"type": "TEXT_DETECTION"}]}]},
        headers={'Content-Type': 'application/json'})
    return json.loads(response.text)


def text_save(imt):
    shutil.copy2(imt, './text/' + time.strftime("%b_%d_%Y_%H_%M_") + imt)
    contents(imt, 'text')
    text = open('text.txt', 'a')
    text.write(time.strftime("%b_%d_%Y_%H_%M_") + imt + '\n' +
               parsed_string(imt)['responses'][0]['textAnnotations'][0]['description'])
    text.close()



# screenshot
def screen(name):
    time.sleep(5)
    ImageGrab.grab().save('./screenshot/' + time.strftime("%b_%d_%Y_%H_%M_") + name + '.jpg', "JPEG")
    contents(name, 'screenshot')


def contents(im, value):
    cont = open('contents.txt', 'a')
    cont.write(time.strftime("%b_%d_%Y_%H_%M_") + im + ' in folder ' + value + '\n')
    cont.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Сделать скригщот -s, '
                                                 'Оотсортировать картинку -i '
                                                 'распознать текст -t')
    parser.add_argument('-i', '--image', help='name of the opening picture for label detection')
    parser.add_argument('-t', '--text', help='name of the opening picture for text detection')
    parser.add_argument('-s', '--screen', help='name of the saving picture after 5 sec.')
    args = parser.parse_args()
    if args.image:
        sort(args.image)
    elif args.text:
        text_save(args.text)
    elif args.screen:
        screen(args.screen)
