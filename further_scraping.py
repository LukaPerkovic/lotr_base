from bs4 import BeautifulSoup
from collections import defaultdict
import os
import pprint
import json


link_dict = defaultdict(list)


culture_list = {}
divisions_list = {}
titles_list = {}
divisions_list = {}
dominions_list = {}
realms_list = {}
race_list = {}
weapons_list = {}



for file in os.listdir('.'):
	if file.startswith('Culture'):


		soup = BeautifulSoup(open(os.path.abspath(file),encoding='utf-8'),'html.parser')

		kb_dict = {}

		try:
			kb_dict['Name'] = soup.find('h2', class_='pi-item pi-item-spacing pi-title').text
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])

					except TypeError:
						pass
					except KeyError:
						pass
		except AttributeError:
			kb_dict['Name'] = 'Missing!'
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])

					except TypeError:
						pass
					except AttributeError:
						pass
		culture_list[file.split('.')[0]] = kb_dict


	elif file.startswith('Culture'):


		soup = BeautifulSoup(open(os.path.abspath(file),encoding='utf-8'),'html.parser')

		kb_dict = {}

		try:
			kb_dict['Name'] = soup.find('h2', class_='pi-item pi-item-spacing pi-title').text
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except KeyError:
						pass
		except AttributeError:
			kb_dict['Name'] = 'Missing!'
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except AttributeError:
						pass
		culture_list[file.split('.')[0]] = kb_dict

	elif file.startswith('Divisions'):


		soup = BeautifulSoup(open(os.path.abspath(file),encoding='utf-8'),'html.parser')

		kb_dict = {}

		try:
			kb_dict['Name'] = soup.find('h2', class_='pi-item pi-item-spacing pi-title').text
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except KeyError:
						pass
		except AttributeError:
			kb_dict['Name'] = 'Missing!'
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except AttributeError:
						pass
		divisions_list[file.split('.')[0]] = kb_dict


	elif file.startswith('Titles'):


		soup = BeautifulSoup(open(os.path.abspath(file),encoding='utf-8'),'html.parser')

		kb_dict = {}

		try:
			kb_dict['Name'] = soup.find('h2', class_='pi-item pi-item-spacing pi-title').text
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except KeyError:
						pass
		except AttributeError:
			kb_dict['Name'] = 'Missing!'
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except AttributeError:
						pass
		titles_list[file.split('.')[0]] = kb_dict


	elif file.startswith('Dominions'):


		soup = BeautifulSoup(open(os.path.abspath(file),encoding='utf-8'),'html.parser')

		kb_dict = {}

		try:
			kb_dict['Name'] = soup.find('h2', class_='pi-item pi-item-spacing pi-title').text
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])

						pass
					except KeyError:
						pass
		except AttributeError:
			kb_dict['Name'] = 'Missing!'
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])

						pass
					except AttributeError:
						pass
		dominions_list[file.split('.')[0]] = kb_dict


	elif file.startswith('Realms'):


		soup = BeautifulSoup(open(os.path.abspath(file),encoding='utf-8'),'html.parser')

		kb_dict = {}

		try:
			kb_dict['Name'] = soup.find('h2', class_='pi-item pi-item-spacing pi-title').text
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except KeyError:
						pass
		except AttributeError:
			kb_dict['Name'] = 'Missing!'
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except AttributeError:
						pass
		realms_list[file.split('.')[0]] = kb_dict



	elif file.startswith('Race'):


		soup = BeautifulSoup(open(os.path.abspath(file),encoding='utf-8'),'html.parser')

		kb_dict = {}

		try:
			kb_dict['Name'] = soup.find('h2', class_='pi-item pi-item-spacing pi-title').text
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except KeyError:
						pass
		except AttributeError:
			kb_dict['Name'] = 'Missing!'
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except AttributeError:
						pass
		race_list[file.split('.')[0]] = kb_dict



	elif file.startswith('Weapons'):


		soup = BeautifulSoup(open(os.path.abspath(file),encoding='utf-8'),'html.parser')

		kb_dict = {}

		try:
			kb_dict['Name'] = soup.find('h2', class_='pi-item pi-item-spacing pi-title').text
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])
						# print(h3.text,':',small_div.text,'--',small_div.a['href'])

					# 	print(small_div.a['href'])
					except TypeError:
						pass
					except KeyError:
						pass
		except AttributeError:
			kb_dict['Name'] = 'Missing!'
			for big_div in soup.find_all('div', class_='pi-item pi-data pi-item-spacing pi-border-color'):
				h3 = big_div.find('h3')
				for small_div in big_div.find_all('div', class_='pi-data-value pi-font'):
					try:
						kb_dict[h3.text] = small_div.text
						link_dict[h3.text].append('https://lotr.fandom.com'+small_div.a['href'])

					except TypeError:
						pass
					except AttributeError:
						pass
		weapons_list[file.split('.')[0]] = kb_dict



with open('culture_list.json','w', encoding='utf8') as c_list:
	json.dump(culture_list,c_list, indent=4, sort_keys=True, ensure_ascii=False)
with open('divisions_list.json','w', encoding='utf8') as c_list:
	json.dump(divisions_list,c_list, indent=4, sort_keys=True, ensure_ascii=False)
with open('titles_list.json','w', encoding='utf8') as c_list:
	json.dump(titles_list,c_list, indent=4, sort_keys=True, ensure_ascii=False)
with open('divisions_list.json','w', encoding='utf8') as c_list:
	json.dump(divisions_list,c_list, indent=4, sort_keys=True, ensure_ascii=False)
with open('dominions_list.json','w', encoding='utf8') as c_list:
	json.dump(dominions_list,c_list, indent=4, sort_keys=True, ensure_ascii=False)
with open('realms_list.json','w', encoding='utf8') as c_list:
	json.dump(realms_list,c_list, indent=4, sort_keys=True, ensure_ascii=False)
with open('race_list.json','w', encoding='utf8') as c_list:
	json.dump(race_list,c_list, indent=4, sort_keys=True, ensure_ascii=False)
with open('weapons_list.json','w', encoding='utf8') as l_dict:
	json.dump(weapons_list,l_dict, indent=4, sort_keys=True, ensure_ascii=False)






