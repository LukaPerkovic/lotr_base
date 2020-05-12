import scrapy
from bs4 import BeautifulSoup
import requests


source = requests.get('https://lotr.fandom.com/wiki/Category:Characters')
soup = BeautifulSoup(source.content, 'html.parser')


url_list = []


try:
	while True:
		for ul in soup.find_all('ul', class_='category-page__members-for-char'):
			for li in ul.find_all('li'):
				a = li.find('a')
				url_list.append('https://lotr.fandom.com'+a['href'])
		source = requests.get(soup.find("a", {"class": "category-page__pagination-next wds-button wds-is-secondary"})['href'])
		soup = BeautifulSoup(source.content, 'html.parser')
except TypeError:
	print('Not found')


class LotrSpider(scrapy.Spider):
	name = 'lotr'


	def start_requests(self):
		urls = url_list

		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)

	def parse(self, response):
		page = response.url.split("/")[-1]
		filename = f'Character_{page}.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
		self.log(f'Saved file {filename}')


  
