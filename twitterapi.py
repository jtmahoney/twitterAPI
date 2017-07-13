import sys
import operator
import requests
import json
import twitter
import enchant
import re
import string

handle="@realDonaldTrump"
#handle="@BarakObama"
#handle="@DNC"

twitter_consumer_key = ''
twitter_consumer_secret = ''
twitter_access_token = ''
twitter_access_secret = ''
twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)
statuses = twitter_api.GetUserTimeline(screen_name=handle, count=200, include_rts=False)

#twitter_api.UpdateImage('/Users/josephmahoney/Pictures/pineapple.gif')

real_words = []
non_words = []

for status in statuses[:1000]:
    sentence_words = status.text.split()
    for word in sentence_words:
        word = re.sub(r'[^\w\s]','',word)
        try:
            dic = enchant.Dict("en_US")
            if dic.check(word)==True:
                real_words.append(word.lower())
            else:
                non_words.append(word.lower())
        except:
            pass

unique_words = set(real_words)
num = len(unique_words)

print num
print unique_words
#print non_words
