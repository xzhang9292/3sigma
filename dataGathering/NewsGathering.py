import requests
import json
import datetime

company = "microsoft"
fromDate = datetime.datetime.today() - datetime.timedelta(days = 27)

while fromDate <= datetime.datetime.today():
	page = 1
	maxPage = 9223372036854775807
	strFromDate = fromDate.strftime("%Y-%m-%d")

	while page <= maxPage:
		url = ('https://newsapi.org/v2/everything?'
				'q=' + company + '&'
				'from=' + strFromDate + '&to=' + strFromDate + '&language=en&sortBy=popularity&'
				'pageSize=100&page=' + str(page) + '&'
		       	'apiKey=EnterYourAPIKeyHere')

		response = requests.get(url)
		data = response.json()
		if page == 1:
			data2 = json.dumps(data)
			res = json.loads(data2)
			totalResults = int(res['totalResults'])
			maxPage = totalResults / 100
			if totalResults % 100 != 0:
				maxPage = maxPage + 1
			if maxPage > 10:
				maxPage = 10

		with open(company + '.json', 'a') as f:
			json.dump(data, f)
			f.write("\n")

		page += 1

	fromDate = fromDate + datetime.timedelta(days = 1)