import sys
import twitter
import json
import config


input_path = './data/mytwitter_data/{}'

# # authorization
# CK = config.CONSUMER_KEY
# CS = config.CONSUMER_SECRET
# AT = config.ACCESS_TOKEN
# AS = config.ACCESS_TOKEN_SECRET

# with open(input_path.format('profile.js')) as target:
#     json.load(target)

# open the tweets data
with open(input_path.format('tweet.js')) as target:
    tw_json = target.read()[25:]
    tw_data = json.loads(tw_json)

print(tw_data[0])
print(type(tw_data[0]))
print(type(tw_data[0]['created_at']))

count = 0
for tweet in tw_data:
    # print(tweet['created_at'])
    if tweet['created_at'][-4:] == '2017':
        print(tweet)
        count += 1
    # count += 1
    # if count == 1000:
    #     sys.exit()
print(count)