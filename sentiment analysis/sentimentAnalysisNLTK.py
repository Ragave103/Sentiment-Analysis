import string
import nltk
from nltk.corpus import stopwords
from nltk.sentiment import SentimentIntensityAnalyzer

#nltk.download('vader_lexicon')
fp = open("data.txt",encoding="utf-8").read()

lower_case=fp.lower()
print("After converting to lowercase: \n\n"+lower_case) # after converting to lowercase

#maketrans - translation table
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
print("After removing punctuations : \n\n"+cleaned_text) # after removing punctuations

sentimentAnalyzer = SentimentIntensityAnalyzer()

emotion = sentimentAnalyzer.polarity_scores(cleaned_text)

final = 0
finalSentiment = ""
for i in emotion:
  print(f"{i} -> {emotion[i]}")
  if(emotion[i]>final):
    final=emotion[i]
    finalSentiment=i
    
if(finalSentiment=="neg"):
  print("Sentiment Analysis : Negative")
elif(finalSentiment=="pos"):
  print("Sentiment Analysis : Positive")
else:
  print("Sentiment Analysis : Neutral")
  

  

