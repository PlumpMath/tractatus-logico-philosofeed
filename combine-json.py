import os
import json

data = []

for filename in os.listdir('./data/split'):
    if filename.endswith(".json"): 
        with open('./data/split/' + filename) as data_file:
            data += json.load(data_file)
            
with open('./data/buzzfeed.json','w') as outfile:
    json.dump(data, outfile)

titles = []

for item in data:
    titles.append(item['title'])
    
# remove duplicates
titles = list(set(titles))

with open('./data/buzzfeed.txt', 'w') as outfile:
    for title in titles:
        outfile.write("%s\n" % title)
