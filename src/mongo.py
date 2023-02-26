from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()
URL = os.getenv('MongoDB_HOST')

def holodive(account):
  try:
    client = MongoClient(host=URL)
    db = client['TGDY']
    col = db['user']
    char_dict = {}
    profile = []
    for i in col.find():
      if account == i['Account']:
        profile.append(i['Name'])
        profile.append(i['Photo'])
        profile.append(i['Coin'])
        profile.append(i['Diamond'])
        for j in i['HoloDive_Character']:
          char_dict[j] = i['HoloDive_Character'][j][0]
        profile.append(char_dict)
    return profile
  except:
    return []