import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


nltk.download('vader_lexicon')

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample text
text = "It is very bad product."



# Perform sentiment analysis
sentiment_score = sia.polarity_scores(text)
print(text)
print(sentiment_score)
