import tweepy

bearer_token = 'your_bearer_token'

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        print(tweet.text)

stream = MyStream(bearer_token)

stream.add_rules(tweepy.StreamRule("keyword"))

stream.filter(tweet_fields=["context_annotations", "created_at"], expansions=["author_id"])

from textblob import TextBlob

def preprocess(text):
    return text

class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):
        tweet_text = preprocess(tweet.text)
        sentiment = TextBlob(tweet_text).sentiment
        print(f"Tweet: {tweet_text}\nSentiment: {sentiment}")

stream = MyStream(bearer_token)

stream.add_rules(tweepy.StreamRule("keyword"))

stream.filter(tweet_fields=["context_annotations", "created_at"], expansions=["author_id"])