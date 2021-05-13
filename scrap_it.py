import argparse
import json
import sys
import time

from bs4 import BeautifulSoup
from selenium import webdriver


argparser = argparse.ArgumentParser(add_help=False)
argparser.add_argument('user', type=str,
                       help=('User handle on twitch e.g.: jtemporal.'))


def main(argv):
    url = f'https://www.twitch.tv/{argv[1]}/videos?filter=archives&sort=time'

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
    print('All done')


if __name__ == '__main__':
    main(sys.argv)