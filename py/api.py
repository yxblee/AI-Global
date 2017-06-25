import twitter

api = twitter.Api(consumer_key='DXKLr99ACQ66nOru2eAiuAlDC',
                  consumer_secret='gBwVqldX1CDtg2UkE0pF4Z4GhCfVFLDGQtdxY2lfB7j5NWPc5Q',
                  access_token_key='878745777081696256-S0WCa1qKyUMEkzFPtnvOKDcPvtzroFb',
                  access_token_secret='b40z4o3fpMe780fMfFOyEzODy26J6Sw9Z4QhsUkuzuTDB')

print(api.VerifyCredentials())

statuses = api.GetUserTimeline(screen_name= "realDonaldTrump")
print([s.text for s in statuses])

# users = api.GetFriends()
# print([u.name for u in users])

