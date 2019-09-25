import twitter
import json
import config
import time

# authorization
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_TOKEN_SECRET

api = twitter.Api(consumer_key=CK, consumer_secret=CS, access_token_key=AT, access_token_secret=AS)

# load tweet
input_path = './data/mytwitter_data/{}'
with open(input_path.format('tweet.js')) as target:
    tw_data = json.loads(target.read()[25:])

for tweet in tw_data:
    year_tw = int(tweet['created_at'][-4:])
    if year_tw <= 2017:
        target_id = int(tweet['id'])
        try:
            api.DestroyStatus(status_id=target_id)
            time.sleep(1)
        except twitter.error.TwitterError:
            pass
        

