from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
URL = os.getenv('MongoDB_HOST')

def holodive(account):
  try:
    client = MongoClient(host=URL)
    db = client['holodive']
    col = db['login']
    char_dict = {}
    profile = []
    for i in col.find():
      if account == i['Account']:
        profile.append(i['Name'])
        profile.append([i['Item'][0],i['Item'][1]])
        for j in i['Character']:
          char_dict[j] = i['Character'][j][0]
        profile.append(char_dict)
    return profile
  except:
    return []