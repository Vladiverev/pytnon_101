import time
image = {'keywords': [{'keyword': 'Women', 'score': 0.685829222202301}, {'keyword': 'People', 'score': 0.6810674071311951}, {'keyword': 'Outdoors', 'score': 0.5401944518089294}, {'keyword': 'Cultures', 'score': 0.3085557222366333}, {'keyword': 'Adult', 'score': 0.2786104083061218}, {'keyword': 'Females', 'score': 0.2597598433494568}, {'keyword': 'Summer', 'score': 0.21838253736495972}, {'keyword': 'Dress', 'score': 0.21028336882591248}], 'status': 'ok'}

print(image['keywords'])


def get_key(keywords, value):
    for item in keywords['keywords']:
        if item.get('keyword') == value:
            return True


contents = open('contents.txt', 'a')
if get_key(image, 'Text') == True:
    contents.write(time.strftime("%b_%d_%Y_%H_%M_")  + ' in folder Text\n')
    print('Text')
elif get_key(image, 'People') == True:
    contents.write(time.strftime("%b_%d_%Y_%H_%M_") + ' in folder People\n')
    print('People')
else:
    contents.write(time.strftime("%b_%d_%Y_%H_%M_") + ' in folder Other\n')
    print('Other')