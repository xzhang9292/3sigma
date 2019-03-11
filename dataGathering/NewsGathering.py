import requests
import json

company = "microsoft"
page = 1

while page <= 169:
	url = ('https://newsapi.org/v2/everything?'
			'q=' + company + '&'
			'from=2019-02-10&to=2019-03-10&language=en&sortBy=popularity&'
			'pageSize=100&page=' + str(page) + '&'
	       	'apiKey=EnterYourAPIKeyHere')

	response = requests.get(url)
	data = response.json()

	with open(company + '.json', 'a') as f:
		json.dump(data, f)
		f.write("\n")

	page += 1