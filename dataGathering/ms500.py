import json

json_data = json.load(open("microsoft.json"))

new_data = []

i = 0
k = 1
for j in json_data:
	j['sentiment'] = "undefined"
	if i < 500:
		new_data.append({"title": j['title'], "description": j['description'], "sentiment": j['sentiment'], 'publishedAt': j['publishedAt']})
	elif i == 500:
		with open("../microsoft/data" + str(k) + ".json", "w") as outfile:
			json.dump(new_data, outfile)

		new_data = []
		i = 0
		k += 1
		if k > 6:
			break

		new_data.append({"title": j['title'], "description": j['description'], "sentiment": j['sentiment'], 'publishedAt': j['publishedAt']})

	i += 1