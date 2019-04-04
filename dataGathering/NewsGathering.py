import requests
import json
import datetime
#300 44 664 1072 498 55 252 148 229 2492
#5754
company = "boeing"
fromDate = datetime.datetime.today() - datetime.timedelta(days = 31) # past month (past 31 days)

while fromDate <= datetime.datetime.today():
	page = 1
	maxPage = 9223372036854775807 # temporary max page number
	strFromDate = fromDate.strftime("%Y-%m-%d")

	while page <= maxPage:
		url = ('https://newsapi.org/v2/everything?'
				'q=' + company + 
				'&sources=abc-news,associated-press,bbc-news,bleacher-report,bloomberg,business-insider,cbs-news,cnbc,cnn,daily-mail,espn,financial-times,fortune,four-four-two,fox-news,fox-sports,google-news,hacker-news,msnbc,nbc-news,reuters,techcrunch,techradar,the-economist,the-huffington-post,the-new-york-times,the-telegraph,the-wall-street-journal,the-washington-post,time,usa-today&'
				'domains=seekingalpha.com&'
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
		with open(company + '_sources.json', 'a') as f:
			if 'articles' in data: # might have changed the max number of pages we can get for free
				json.dump(data['articles'], f)
				f.write("\n")

		# go to the next page
		page += 1

	# go to next date
	fromDate = fromDate + datetime.timedelta(days = 1)