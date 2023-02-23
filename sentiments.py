# in order to run this programme you will need to install textblob in console
# pip install textblob

# to enable noun phrase and other analyses, we installed a further package in console
# python -m textblob.download_corpora

from textblob import TextBlob

# Define the text to be analyzed
# text = "I fricking adore pizza, it's my all-time favorite food ever!"
text = "I hate cheesy pizza, it's disgusting!"

# Create a TextBlob object and perform sentiment analysis
blob = TextBlob(text)
print(blob.noun_phrases)
sentiment_score = blob.sentiment.polarity

# Print the sentiment score
print("Sentiment score:", sentiment_score)
