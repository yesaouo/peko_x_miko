import random, datetime, requests
from bs4 import BeautifulSoup

def main(mode = 'monthly', rank = 1, date = ''):
  try:
    if mode.lower() in 'daily': mode = 'daily'
    elif mode.lower() in 'weekly': mode = 'weekly'
    else: mode = 'monthly'

    if date == '':
      month = str(random.randint(1,12))
      if len(month) == 1: month = '0' + month
      day = str(random.randint(1,28))
      if len(day) == 1: day = '0' + day
      date = str(datetime.datetime.now().year-random.randint(1,5)) + month + day

    url = f'https://www.pixiv.net/ranking.php?mode={mode}&content=illust&date={date}'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    imgs = soup.find_all('a', class_='work')
    return f'https://www.pixiv.net{imgs[rank-1]["href"]}'
  except: return 'error'