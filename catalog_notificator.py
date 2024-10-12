from bs4 import BeautifulSoup
import telegram_send
import requests
import random
import json
import time

# Constants:

# website = 'https://catalog.roblox.com/v1/search/items/details?Category=3&Subcategory=57&SortType=3' # for test
website = 'https://catalog.roblox.com/v1/search/items/details?Category=11&CreatorName=Roblox&SortType=3' # main link
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')
string_1 = str(soup.prettify())[25:-24:]
string_1 = string_1[string_1.index('['):-1:]
items_data_1 = json.loads(string_1)
newline = '\n'

def startup_message():

	telegram_send.send(messages=[f'❕<code>Catalog Notificator v1.05</code>'], parse_mode='html')

def main():

	global items_data_1

	result_local = requests.get(website)
	content_local = result_local.text
	soup_local = BeautifulSoup(content_local, 'lxml')
	string_2 = str(soup_local.prettify())[25:-24:]
	string_2 = string_2[string_2.index('['):-1:]
	items_data_2 = json.loads(string_2)

	name = items_data_2[0]["name"]
	link = f'https://www.roblox.com/catalog/{items_data_2[0]["id"]}/'
	content_img = requests.get(link).text
	content_img = content_img[content_img.find('https://tr.rbxcdn.com/')::]
	content_img = content_img[:content_img.find('"')]
	image_link = content_img.replace('/110/110/', '/420/420/')
		
	# items_data_1[0]['id'] = 'for test'
		
	if items_data_1[0]['id'] == items_data_2[0]['id']:
		print(items_data_2[0]['id'], 'False')

	else:
		print(items_data_2[0]['id'], 'True')
		if len(items_data_1[0]['itemRestrictions']) != 0:
			telegram_send.send(messages=[f'<a href="{image_link}">❗</a><b>Лимитный предмет в каталоге обновлён</b>❗{newline}{newline}<u>{name}</u>{newline}{newline}{link}'], parse_mode='html')
			items_data_1 = items_data_2
		else:
			for i in range(5):
				telegram_send.send(messages=[f'<a href="{image_link}">❗</a><b>Предмет в каталоге обновлён</b>❗{newline}{newline}<u>{name}</u>{newline}{newline}{link}'], parse_mode='html')
				time.sleep(45)
			items_data_1 = items_data_2

if __name__ == '__main__':
	startup_message()
	while True:
		try:
			main()
			time.sleep(30 + random.randint(0,10))
		except KeyError:
			time.sleep(30)
			main()
	
