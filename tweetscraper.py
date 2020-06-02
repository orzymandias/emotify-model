import GetOldTweets3 as got
import numpy as np
import webbrowser

text_query = '#terrified'
count = 1000
file_name = 'fear10'
set_until = "2014-02-12"
tweetCriteria = got.manager.TweetCriteria().setQuerySearch(text_query)\
                                           .setMaxTweets(count)\
                                           .setUntil(set_until)

# Creation of list that contains all tweets
tweets = got.manager.TweetManager.getTweets(tweetCriteria)
# Creating list of chosen tweet data
text_tweets = np.asarray([[tweet.text]for tweet in tweets])
label = np.asarray([["fearful"] for i in range(0, count)])
text_tweets = np.append(text_tweets, label, axis=1)
np.savetxt(f"{file_name}.csv", text_tweets, delimiter=",", fmt='%s')
webbrowser.open("https://www.youtube.com/watch?v=7lsdJDiJ0QE")



