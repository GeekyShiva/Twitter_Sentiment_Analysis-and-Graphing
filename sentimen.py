from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

# consumer key, consumer secret, access token, access secret.
ckey = "asdfsafsafsaf"
csecret = "asdfasdfsadfsa"
atoken = "asdfsadfsafsaf-asdfsaf"
asecret = "asdfsadfsadfsadfsadfsad"


class listener(StreamListener):
    def on_data(self, data):
        try:                                      ## handling reconnecting issue
        all_data = json.loads(data)

        tweet = all_data["text"]
        sentiment_value, confidence = s.sentiment(tweet)

        print (tweet, sentiment_value, confidence)
        time.sleep(0.2) ## Error handling in case of restricted tweets

        if confidence*100>=80:         ##Scaling can be reconfigured.
            output =  open("twitter-out.txt","a")
            output.write(sentiment_value)
            output.write('\n')
            output.close()

        return True
        except:
        return True                             ## if this returns false at run time try not reconnecting at same time

    def on_error(self, status):
        print (status)


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])