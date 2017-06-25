import twitter
import tweepy

try:
	import simplejson as json
except ImportError:
	import json

api2 = twitter.Api(consumer_key='DXKLr99ACQ66nOru2eAiuAlDC',
                  consumer_secret='gBwVqldX1CDtg2UkE0pF4Z4GhCfVFLDGQtdxY2lfB7j5NWPc5Q',
                  access_token_key='878745777081696256-S0WCa1qKyUMEkzFPtnvOKDcPvtzroFb',
                  access_token_secret='b40z4o3fpMe780fMfFOyEzODy26J6Sw9Z4QhsUkuzuTDB')

# print(api.VerifyCredentials())

statuses = api2.GetUserTimeline(screen_name= "realDonaldTrump")
print([s.text for s in statuses])

# users = api2.GetFriends()
# print([u.name for u in users])

# with open('status.txt', 'w', encoding='utf-8') as outfile:
#     json.dump(statuses, outfile, ensure_ascii=False)

# with open('output.json', 'w', encoding='utf-8') as f:
#     # api2.GetStreamFilter will return a generator that yields one status
#     # message (i.e., Tweet) at a time as a JSON dictionary.
#     for line in api.GetStreamFilter(track=['#party']):
#         f.write(json.dumps(line))
#         f.write('\n')


auth = tweepy.OAuthHandler('DXKLr99ACQ66nOru2eAiuAlDC', 'gBwVqldX1CDtg2UkE0pF4Z4GhCfVFLDGQtdxY2lfB7j5NWPc5Q')
auth.set_access_token('878745777081696256-S0WCa1qKyUMEkzFPtnvOKDcPvtzroFb', 'b40z4o3fpMe780fMfFOyEzODy26J6Sw9Z4QhsUkuzuTDB')

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

user = api.get_user('fun')
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)



tweets = api.search(['#fun'])
# print (tweet)
with open('output.json', 'w', encoding='utf-8') as f:
	for tweet in tweets:
		f.write(tweet)
		f.write('\n')

	# for media in tweet.entities.get("media",[{}]):
	#     #checks if there is any media-entity
	#     if media.get("type",None) == "photo":
	#         # checks if the entity is of the type "photo"
	#         image_content=requests.get(media["media_url"])
	#         # save to file etc.
	#         print (image_content)

