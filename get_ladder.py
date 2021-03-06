import configparser
import requests
import time

config = configparser.ConfigParser()
config.read('config.ini')

regions = config.get('adjustable', 'regions').split(',')
leagues = config.get('adjustable', 'leagues').split(',')

for region in regions:
	file = open(config.get('setup', 'ladder_dir') + '/ladder-{}.txt'.format(region), "w", encoding="utf-8")
	for league in leagues:
		url = config.get('default', 'ladder_url').format(region, league, config.get('setup', 'api_key'))
		try:
			response = requests.get(url)
			if(response.status_code == 200):
				entries = response.json()['entries']
				players = [file.write(entry['summonerName'] + '\n') for entry in entries]
		except:
			print("something failed")
		time.sleep(1)
