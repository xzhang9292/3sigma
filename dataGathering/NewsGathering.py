import requests
import json
import datetime

company = "mcdonald's"
fromDate = datetime.datetime.today() - datetime.timedelta(days = 27) # past month (past 27 days)

while fromDate <= datetime.datetime.today():
	page = 1
	maxPage = 9223372036854775807 # temporary max page number
	strFromDate = fromDate.strftime("%Y-%m-%d")

	while page <= maxPage:
		url = ('https://newsapi.org/v2/everything?'
				'q=' + company + '&'
				'from=' + strFromDate + '&to=' + strFromDate + '&language=en&sortBy=popularity&'
				'pageSize=100&page=' + str(page) + '&'
		       	'apiKey=EnterYourAPIKeyHere')

		response = requests.get(url)
		data = response.json()
		# update max page number
		if page == 1:
			data2 = json.dumps(data)
			res = json.loads(data2)
			totalResults = int(res['totalResults'])
			maxPage = totalResults / 100
			if totalResults % 100 != 0:
				maxPage = maxPage + 1
			if maxPage > 10:
				maxPage = 10

		# write to json file
		with open(company + '.json', 'a') as f:
			json.dump(data['articles'], f)
			f.write("\n")

		# go to the next page
		page += 1

	# go to next date
	fromDate = fromDate + datetime.timedelta(days = 1)