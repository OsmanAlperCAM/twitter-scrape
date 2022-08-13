from flask import *
import json
import time
from datetime import datetime
import snscrape.modules.twitter as twitterScraper


app = Flask(__name__)

scraper = twitterScraper.TwitterUserScraper("haskologlu")

tweets = []

nowYear = str(datetime.now().year)
nowMonth = str(datetime.now().month)
nowDay = str(datetime.now().day)

users_name = ['temmuz1919', 'haskologlu',
              'lordsinov', 'GOrtadogu', 'akdenizpolitik', 'bpthaber']
for n, k in enumerate(users_name):
    for i, tweet in enumerate(twitterScraper.TwitterSearchScraper('from:{} since:{}-{}-{}'.format(users_name[n], nowYear, nowMonth, nowDay)).get_items()):
        if i > 100:
            break
        tweets.append(
            {"id": tweet.id, "name": tweet.username, "content": tweet.content, "date": str(tweet.date)})
    print(
        'from:{} since:{}-0{}-{}'.format(users_name[n], nowYear, nowMonth, nowDay))

f = open("tweets.json", "w")
j = json.dumps(tweets)
f.write(j)
f.close


@app.route('/', methods=['GET'])
def home_page():
    json_dump = j
    return json_dump


# if __name__ == '__main__':
#     app.run(port=7777)
