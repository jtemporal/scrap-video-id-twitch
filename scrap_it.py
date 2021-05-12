import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://www.twitch.tv/jtemporal/videos?filter=archives&sort=time'
  
print('Starting Web Driver')
driver = webdriver.Chrome('./chromedriver')
print('Loading Page')
driver.get(url) 
time.sleep(5)

print('Getting HTML')
html = driver.page_source
driver.close()
  
soup = BeautifulSoup(html, "html.parser")
print('Getting video IDs')
all_a = soup.find_all('a', {"data-a-target": "preview-card-image-link"}, href=True)
video_ids = [video_link.get('href').split('/')[2] for video_link in all_a]
video_ids = [video_id.split('?')[0] for video_id in video_ids]

print('Saving video IDs')
with open('twitch_video_ids.json', 'w') as f:
    f.write(json.dumps({'video_id_list': video_ids}))
print('Saved video IDs')