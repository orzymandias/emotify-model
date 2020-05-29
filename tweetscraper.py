import GetOldTweets3 as got
import numpy as np

text_query = 'angry'
count = 1000
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query)\
                                           .setMaxTweets(count)\

# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
text_tweets = np.asarray([[tweet.text]for tweet in tweets])
label = np.asarray([["anger"] for i in range(0, count)])
text_tweets = np.append(text_tweets, label, axis=1)
np.savetxt("angry.csv", text_tweets, delimiter=",", fmt='%s')



