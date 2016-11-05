# Author(s): Isaiah Mann
# Description: Exports Twitter JSON with just the keys and the text

import json
textKey = "text"
userKey = "user"
nameKey = "name"
twitterKey = "Twitter"
with open('twitterfeed.json') as data_file:
    data = json.load(data_file)[twitterKey]
tweets = {}
for i in range(0, len(data)):
    tweets[data[i][userKey][nameKey]] = data[i][textKey]
with open('twitterfeedexport.json', 'w') as fp:
    json.dump(tweets, fp, indent=2)
