import json

json_data = json.load(open("microsoft_sources.json"))

new_data = []

i = 0
k = 1
for j in json_data:
	j['sentiment'] = "undefined"
	if (i < 478 and k == 1) or (i < 595 and k > 1):
		new_data.append({"title": j['title'], "description": j['description'], "sentiment": j['sentiment'], 'publishedAt': j['publishedAt']})
	elif (i == 478 and k == 1) or (i == 595 and k > 1):
		with open("../newsSources/microsoft" + str(k) + ".json", "w") as outfile:
			json.dump(new_data, outfile)

		new_data = []
		i = 0
		k += 1

		new_data.append({"title": j['title'], "description": j['description'], "sentiment": j['sentiment'], 'publishedAt': j['publishedAt']})

	i += 1

with open("../newsSources/microsoft" + str(k) + ".json", "w") as outfile:
	json.dump(new_data, outfile)