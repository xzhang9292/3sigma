import json

json_data = json.load(open("BAadjusted.json"))

new_data = []

i = 0
for day in json_data["Time Series (Daily)"]:
	new_data.append({day: json_data["Time Series (Daily)"][str(day)]["5. adjusted close"]})
	
with open("boeingAdjustedOnly.json", "w") as outfile:
    json.dump(new_data, outfile)