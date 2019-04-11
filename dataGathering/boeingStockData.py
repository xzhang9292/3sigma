import http.client
import json
import time
import sys
import collections
from urllib.request import urlopen
import fileinput
import requests
#################################################
# CS6242  - Team Project
# Spring 2019
#################################################

# create array of the companies' ticks
# Boeing,
companies = ['BA']

# get data from API (MSFT, for every 5min)
for i in range(len(companies)):
    symbol = str(companies[i])
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=' + \
        symbol+'&outputsize=compact&apikey=BDBWLB1334VTPKJQ'
    json_obj = urlopen(url)
    data = json.load(json_obj)

    with open(symbol+'adjusted.json', 'a') as outfile:
        json.dump(data, outfile)
        outfile.write('\n')
