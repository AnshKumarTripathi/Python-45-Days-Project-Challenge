import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download the necessary NLTK data
# nltk.download('vader_lexicon')
# nltk.download('punkt')

sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment_scores = sia.polarity_scores(text)
    return sentiment_scores

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)  
    return ' '.join(tokens)

texts = [
    "I absolutely love this product! It's amazing.",
    "I hate this. It's the worst experience ever.",
    "It's okay, nothing special but not bad either."
]

for text in texts:
    preprocessed_text = preprocess_text(text)
    sentiment_scores = analyze_sentiment(preprocessed_text)
    print(f"Text: {text}")
    print(f"Preprocessed Text: {preprocessed_text}")
    print(f"Sentiment Scores: {sentiment_scores}")

custom_text = input("Enter a text to analyze sentiment: ")
preprocessed_custom_text = preprocess_text(custom_text)
custom_sentiment_scores = analyze_sentiment(preprocessed_custom_text)
print(f"Custom Text: {custom_text}")
print(f"Preprocessed Custom Text: {preprocessed_custom_text}")
print(f"Sentiment Scores: {custom_sentiment_scores}")
