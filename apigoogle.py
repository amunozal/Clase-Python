#import os

#os.system('sudo pip install requests')
#os.system('sudo pip install json')

import requests
import json
 

#pip install requests
#pip install json

token = "Bearer <TOKEN>"
headers = {"Authorization": token}
r = requests.get('https://google.com/', headers = headers)
r.status_code
print(r.status_code)