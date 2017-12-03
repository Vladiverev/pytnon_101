import shutil
import time
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient


image = 'p.jpg'
#    {'keywords': [{'keyword': 'Women', 'score': 0.685829222202301}, {'keyword': 'People', 'score': 0.6810674071311951}, {'keyword': 'Outdoors', 'score': 0.5401944518089294}, {'keyword': 'Cultures', 'score': 0.3085557222366333}, {'keyword': 'Adult', 'score': 0.2786104083061218}, {'keyword': 'Females', 'score': 0.2597598433494568}, {'keyword': 'Summer', 'score': 0.21838253736495972}, {'keyword': 'Dress', 'score': 0.21028336882591248}], 'status': 'ok'}
#    {'keywords': [{'keyword': 'Panda - Animal', 'score': 0.9958991408348083}, {'keyword': 'Bear', 'score': 0.9896968603134155}, {'keyword': 'Animal', 'score': 0.9547567367553711}, {'keyword': 'Wildlife', 'score': 0.9156829118728638}, {'keyword': 'Mammal', 'score': 0.8703738451004028}, {'keyword': 'Nature', 'score': 0.8522777557373047}, {'keyword': 'Endangered Species', 'score': 0.8331900835037231}, {'keyword': 'Giant Panda', 'score': 0.8262365460395813}, {'keyword': 'Asia', 'score': 0.6280353665351868}, {'keyword': 'Cute', 'score': 0.5546023845672607}, {'keyword': 'Black Color', 'score': 0.5511609315872192}, {'keyword': 'Animals In The Wild', 'score': 0.5385469794273376}, {'keyword': 'Forest', 'score': 0.5103386640548706}, {'keyword': 'Wildlife Reserve', 'score': 0.4646719694137573}, {'keyword': 'China - East Asia', 'score': 0.45713457465171814}, {'keyword': 'Zoo', 'score': 0.42306017875671387}, {'keyword': 'Chengdu', 'score': 0.39728304743766785}, {'keyword': 'Fur', 'score': 0.38207927346229553}, {'keyword': 'Sichuan Province', 'score': 0.32027432322502136}, {'keyword': 'Outdoors', 'score': 0.31819653511047363}, {'keyword': 'Large', 'score': 0.2999182939529419}, {'keyword': 'Close-up', 'score': 0.2883228659629822}, {'keyword': 'Bamboo - Plant', 'score': 0.28627195954322815}, {'keyword': 'White', 'score': 0.27913421392440796}, {'keyword': 'One Animal', 'score': 0.2583237588405609}, {'keyword': 'No People', 'score': 0.24541325867176056}, {'keyword': 'Wilderness Area', 'score': 0.23896482586860657}, {'keyword': 'Carnivore', 'score': 0.22171810269355774}], 'status': 'ok'}

client_id = 'Ba4KbJbr1aECLFxZKGrjzFwaUB2nqe1iyV3KYEbT'
client_secret = 'Ras3R23sfsYC1xVZK4RzxrrX2lJrzKWNAwssz2aDYoFuewsEL9'

oauth = OAuth2Session(client=BackendApplicationClient(client_id))
token = oauth.fetch_token(token_url='https://api.everypixel.com/oauth/token', auth=(client_id, client_secret))

api = OAuth2Session(client_id, token=token)

data = {'data': open(image, 'rb')}
result = api.post('https://api.everypixel.com/v1/keywords', files=data).json()

print(result)


def get_key(result, value):
    for item in result['keywords']:
        if item.get('keyword') == value:
            return True


contents = open('contents.txt', 'a')

if get_key(result, 'Text') == True:
    shutil.copy2(image, './text/' + time.strftime("%b_%d_%Y_%H_%M_") + image)
    contents.write(time.strftime("%b_%d_%Y_%H_%M_") + 'image' + ' in folder Text\n')
    print('Text')
elif get_key(result, 'People') == True:
    shutil.copy2(image, './People/' + time.strftime("%b_%d_%Y_%H_%M_") + image)
    contents.write(time.strftime("%b_%d_%Y_%H_%M_") + 'image' + ' in folder People\n')
    print('People')
else:
    shutil.copy2(image, './other/' + time.strftime("%b_%d_%Y_%H_%M_") + image)
    contents.write(time.strftime("%b_%d_%Y_%H_%M_") + 'image' + ' in folder Other\n')
    print('Other')
contents.close()