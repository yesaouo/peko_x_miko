import requests
from bs4 import BeautifulSoup

def type(name):
  try:
    url = f'https://wiki.52poke.com/wiki/{name}'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    pm_type = soup.find_all('span', class_='type-box-9-text')
    type_list = []
    for i in pm_type:
      if i.get_text() not in type_list:
        type_list.append(i.get_text())
    return type_list
  except: return []

def stat(name):
  try:
    url = f'https://wiki.52poke.com/wiki/{name}'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    pm_stat = soup.find_all('table', class_='roundy')
    stat_list = []
    for i in pm_stat:
      all_div = i.find_all('div')
      if len(all_div) != 0:
        for j in all_div:
          if j.get_text().isdigit():
            stat_list.append(j.get_text())
    return stat_list  
  except: return []

def skill(name):
  try:
    url = f'https://wiki.52poke.com/wiki/{name}'
    web = requests.get(url)
    soup = BeautifulSoup(web.text, "html.parser")
    pm_skill = soup.find_all('tr', class_='at-c bgwhite')
    skill_list = []
    for i in pm_skill:
      all_td = i.find_all('td')
      skill = []
      for j in all_td:
        if j.get_text() != '\n':
          skill.append(j.get_text().replace('\n','').replace('[详]',''))
          if len(skill) == 7:
            skill_list.append(skill)
            skill = []
    return skill_list      
  except: return []