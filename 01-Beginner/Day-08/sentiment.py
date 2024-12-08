import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

texts = [
  "I love Python!",
  "I hate writing comments!!",
  "It's okay to be nice sometimes."
  "Some people are good, some people are bad, but i am Rich"
]

for text in texts:
  sentiment_socres = sia.polarity_scores(text)
  print(f"Text: {text}")
  print(f"Sentiment Scores: {sentiment_socres}")