# tweets_cleaner
ツイート削除API

## How to use
API認証のために`./scripts`にconfig.pyを置く

```python:config.py
CONSUMER_KEY = "hogehoge"
CONSUMER_SECRET = "hogehoge"
ACCESS_TOKEN = "hogehoge"
ACCESS_TOKEN_SECRET = "hogehoge"
```
あとは実行するのみ

### hit_api_sample
Twitter apiを叩く挙動のサンプルスクリプト。タイムライン閲覧とツイート送信の2機能

- タイムライン閲覧: 最新20ツイートを表示
- ツイート送信: コンソール上に入力したツイートを送信

### delete_tweet
`data/mytwitter_data/tweet.js`に保存されたツイートIDを取得し日付指定したツイートを削除する.

