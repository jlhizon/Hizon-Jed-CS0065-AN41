from textblob import TextBlob

my_sentences = []
sentence_polarity = []

for x in range(10):
  sentence = input(f"Enter sentence [{x + 1}]: ")
  my_sentences.append(sentence)

  s = TextBlob(sentence)
  p = s.sentiment.polarity
  sentence_polarity.append(p)

labels = [] # To store and count after for the report
print("\nResults: ")
for x, polarity in enumerate(sentence_polarity):
  #Negative p<0, Neutral p=0, Positive p>0
  if polarity <0:
    print(my_sentences[x], " - Negative")
    labels.append("Negative")
  elif polarity == 0:
    print(my_sentences[x], " - Neutral")
    labels.append("Neutral")
  elif polarity > 0 and polarity <= 1:
    print(my_sentences[x], " - Positive")
    labels.append("Positive")

print("\nReport:")
print("Negative :", labels.count("Negative"))
print("Neutral :", labels.count("Neutral"))
print("Positive :", labels.count("Positive"))