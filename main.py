from selenium import webdriver
from bs4 import BeautifulSoup
import os
import definition
import time


class Ycrawler:
    driver = None

    def __init__(self):
        self.init_engine()

    def print_hi(name):
        print(f'Hi, {name}')

    def init_engine(self):
        # os.path.abspath()
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--lang=ko')

        self.driver = webdriver.Chrome(definition.ROOT_DIR+'/config/chromedriver', options=options)


    def scrolling(self, scroll_count = 10):
        idx = 1
        while True:
            print("scrolling the contents...")
            self.driver.execute_script("window.scrollTo(0, window.scrollY + 3000);")
            time.sleep(0.5)

            idx += 1
            if idx == scroll_count:
                break;


if __name__ == '__main__':
    #web driver 객체 생성(selenium base)
    crawler = Ycrawler()

    print("please enter the youtube channel url \n")
    urls = input()
    if urls[:5] != 'https':
        urls = 'https://www.youtube.com/channel/UC12YJZLancDKojjbRunyhZA/videos'
    else:
        urls += '/videos'
    #site 호출
    crawler.driver.get(urls)
    crawler.scrolling()
    post_title = list()
    post_uploader = list()
    post_views = list()


    soup = BeautifulSoup(crawler.driver.page_source, "lxml")

    posts = soup.find_all('a',attrs={'class': "yt-simple-endpoint style-scope ytd-grid-video-renderer"})

    print("총 영상"+str(len(posts)))

    for post in posts:
        # print(post.attrs['title'])
        arrs = post.attrs['aria-label']

        # arrs = arrs.split('by ')
        arrs = arrs.split('게시자: ')

        # title append
        post_title.append(arrs[0])
        print(arrs[0])

        # channel uploader name append
        post_uploader.append(arrs[1].split(' ')[0])
        print(arrs[1].split(' ')[0])

        # video views append
        arrs = arrs[1].split(' ')
        print(arrs[len(arrs)-1])
        post_views.append(arrs[len(arrs)-1])
        print('')




