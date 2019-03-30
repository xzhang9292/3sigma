import json

json_data = json.load(open("verizon.json"))

new_data = []

i = 0
for j in json_data:
	j['sentiment'] = "undefined"
	if i < 100:
		new_data.append({"title": j['title'], "description": j['description'], "sentiment": j['sentiment']})
	i += 1

with open("../100Samples/verizon100.json", "w") as outfile:
    json.dump(new_data, outfile)