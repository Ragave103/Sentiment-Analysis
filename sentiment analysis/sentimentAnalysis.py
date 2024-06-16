# This program uses stopwords of NLTK (Natural Language Toolkit) only for Sentiment Analysis
import string

from nltk.corpus import stopwords



fp = open("data.txt",encoding="utf-8").read()

lower_case=fp.lower()
print("After converting to lowercase: \n\n"+lower_case) # after converting to lowercase

#maketrans - translation table
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
print("After removing punctuations : \n\n"+cleaned_text) # after removing punctuations

#download stopwords before using them
#nltk.download('stopwords')   

stopWords = list(stopwords.words("english"))
print(" Stopwords: \n\n")
print(stopWords) # printing stopwords downloaded from nltk


new_text = [text for text in cleaned_text.split() if text not in stopWords]

print("After removing Stopwords: \n\n") 
print(new_text) # after removing stopwords

emotion_total ={"happy":0,"sad":0,"neutral":0}
with open("emotionWords.txt",'r') as f:
  for line in f:
    line = line.replace(',','').replace("'",'')
    word,emotion = line.split(":")
    if(word in new_text):
      emotion_total[emotion.strip()]+=1
    
final = 0
finalEmotion = ""
for i in emotion_total:
  print(f"{i} -> {emotion_total[i]}")
  if(emotion_total[i]>final):
    final=emotion_total[i]
    finalEmotion =i
    
print(f"Sentiment analysis : {finalEmotion}")
  

  
