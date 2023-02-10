import random, requests
from bs4 import BeautifulSoup

def getPage():
  web = requests.get('https://www.ptt.cc/bbs/Beauty/index.html', cookies={'over18':'1'})
  soup = BeautifulSoup(web.text, "html.parser")
  btn_wide = soup.find_all('a', class_='btn wide')
  for i in btn_wide:
    if i.get_text() == '‹ 上頁':
      newPage = int(i['href'].replace('/bbs/Beauty/index','').replace('.html','')) + 1
      return newPage

def main():
  try:
    newPage = getPage()
    page = random.randint(newPage - 1000, newPage)
    ban = ['[公告]','[帥哥]','大尺碼']
    web = requests.get(f'https://www.ptt.cc/bbs/Beauty/index{page}.html', cookies={'over18':'1'})
    soup = BeautifulSoup(web.text, "html.parser")
    all_titles = soup.find_all('div', class_='title')
    titles = []
    for i in all_titles:
      find_a = i.find('a')
      if find_a:
        text_a = find_a.get_text()
        if find_a != None and not any([e in text_a for e in ban]):
          titles.append(f'https://www.ptt.cc/{find_a["href"]}')
    url = titles[random.randint(0, len(titles) - 1)]
    web = requests.get(url, cookies={'over18':'1'})
    soup = BeautifulSoup(web.text, "html.parser")
    imgs = soup.find_all('img')
    imgList = []
    for i in imgs:
      imgList.append(i['src'].replace('cache.ptt.cc/c/https/',''))
    return imgList[random.randint(0, len(imgList) - 1)]
    
  except: return 'error'