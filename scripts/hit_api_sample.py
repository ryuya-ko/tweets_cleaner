import twitter
import config
import sys
import json

# authorization
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
AS = config.ACCESS_TOKEN_SECRET

api = twitter.Api(consumer_key=CK, consumer_secret=CS, access_token_key=AT, access_token_secret=AS)

# api.GetUser()
# api.DestroyStatus()
# api.GetStatuses()
# api.GetUserTimeline(user_id=1412344992, count=20)

def main():
    flag = input(r'Do you want to tweet? y/n:')
    convert = lambda flag: True if flag == 'y' else False
    if flag != 'y' and flag != 'n':
        print('Invalid input')
    else:
        flag = convert(flag)
    if flag is True:
        postTweet()
    else:
        getTimeline()

def getTimeline():
    res = api.GetHomeTimeline()
    print(type(res))
    for tw in res:
        print('==========')
        print(tw.user.screen_name)
        print(tw.created_at)
        print(tw.text)
        print()

def postTweet():
    message = input(">>")
    api.PostUpdates(status=message, continuation='cont')


if __name__ == "__main__":
    main()