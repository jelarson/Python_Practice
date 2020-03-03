# link1 = 'http://www.dailysmarty.com/posts/installing-anaconda-python-data-science-platform'
# link2 = 'http://www.dailysmarty.com/posts/python-libraries-to-import-for-data-science-programs'


# def title1(link1):
#   link2 = link1[33:]
#   link3 = link2.split("-")
#   link4 = " ".join(link3)

#   return link4.title()

# print(title1(link1))
# print(title1(link2))

import requests
from bs4 import BeautifulSoup
from inflection import titleize


def titles_generator(links):
  titles = []

  def post_formatter(url):
    if 'posts' in url:
      url = url.split('/')[-1]
      url = url.replace('-', ' ')
      url = titleize(url)
      titles.append(url)

  for link in links:
    if link.get('href') == None:
      continue
    else:  
      post_formatter(link.get('href'))

  return titles

page = requests.get("http://www.dailysmarty.com/topics/python")

soup = BeautifulSoup(page.text, 'html.parser')

links = soup.find_all('a')
 
titles = titles_generator(links)

for title in titles:
  print (title)