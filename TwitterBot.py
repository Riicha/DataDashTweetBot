# Dependencies
import tweepy
import time

# Twitter API Keys
consumer_key = 'b2jDtC9vAdTpnuJDZkNPkwEYF'
consumer_secret = 'xEo1L3eRSaE6J7uOIlYP0ohoNp0jikv3LKunjp9arE0YWn5tVo'
access_token = '57237295-K2EPPUBgXZfz83NuA92RxkzETWThD4YW8lt3bhAcW'
access_token_secret = '9GD3xt89mMZNCKWmDwQvnaWw3tQjaz0vgz4l4d90Fb7N0'


# Create quotes to tweet
quote_list = ["Time means a lot to me because, you see, I, too, am also a learner and am often lost in the joy of forever developing and simplifying. If you love life, don’t waste time, for time is what life is made up of",
"Life is what happens when you’re busy making other plans",
"Very little is needed to make a happy life; it is all within yourself, in your way of thinking."]

# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
    
# Create function for tweeting

def QuoteItUp(index):

    i=0
    # Tweet the next quote
    api.update_status(quote_list[index])
    # Print success message
    print("%s Quote tweeted successfully"%(i+1))
    i+=1

# Set timer to run every minute
counter=0
while(counter<3):
    QuoteItUp(counter)
    time.sleep(30)
    counter += 1