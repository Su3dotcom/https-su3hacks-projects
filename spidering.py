#!/usr/bin/python3
import scrapy
import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
import datetime

DELAY = 1
TIMEOUT = 60.0
MAX_CONNECTION = 5
logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class HttpSpider(GridLayout):
    def __init__(self, **kwargs):
        super(HttpSpider, self).__init__(**kwargs)
        name = 'cockroch'
        url = ''
        self.visited_urls = []
        self.urls_to_visit = urls

    def update_settings(cls, settings):
        settings.set("ROBOTSTXT_OBEY", "True", priority="spider")
        settings.set("AUTOTHROTTLE_ENABLED", "True", priority="spider")
        settings.set("HTTPCACHE_ENABLED", "True", priority="spider")
        settings.set("DOWNLOAD_DELAY", "2.5", priority="spider")
        settings.set("DNS_TIMEOUT", "60", priority="spider")
        settings.set("DOWNLOADER_CLIENT_TLS", "TLSv1.1",priority="spider")
        settings.set("DOWNLOAD_TIMEOUT","180", priority="spider")
        settings.set("DOWNLOAD_MAXSIZE", "1073741824",priority="spider")
        return settings

    def download_url(self, url):
        return requests.get(url).text

    def show_linked_url(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a'):
            path = link.get('href')
            if path and path.startwith('/'):
                path = urljoin(url, path)
                yield path

    def add_url_to_visit(self, url):
        if url not in visited_urls and url not in self.url_to_visit:
            self.urls_to_visit.append(url)

    def crawl_url(self, url):
        html = self.download_url(url)
        for url in self.get_linked_urls(url, html):
            self.add_urls_to_visit(url)

    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit.pop(0)
            logging.inf(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
        
class CatFeetApp(App):
    def build(self):
        return HttpSpider()

if __name__ == '__main__':
    CatFeetApp('neverssl.com')().run()
