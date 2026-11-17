'''
Dataset for the positive and negative words are
retrieved from: https://www.kaggle.com/datasets/mukulkirti/positive-and-negative-word-listrar

Make sure to use "words.csv" provided in the same Github directory.
'''
import pandas as pd
import string

df = pd.read_csv("words.csv")

positive_set = set(df["positive_words"].dropna().tolist())
negative_set = set(df["negative_words"].dropna().tolist())


def number_happy(sentence):
  positive_count = 0
  words = sentence.split()
  for word in words:
    if word in positive_set:
      positive_count += 1
  return positive_count

def number_sad(sentence):
  negative_count = 0
  words = sentence.split()
  for word in words:
    if word in negative_set:
      negative_count += 1
  return negative_count

def check_happy(sentence):
  if number_happy(sentence) > number_sad(sentence):
    return "Happy Sentence"
  elif number_happy(sentence) < number_sad(sentence):
    return "Sad Sentence"
  else:
    return "Neutral Sentence"

def clean_sentence(temp_sentence):
  sentence = temp_sentence.lower()
  for p in string.punctuation:
    sentence = sentence.replace(p, " ")
  return sentence

def main():
  temp_sentence = input(f"Enter sentence: ")
  sentence = clean_sentence(temp_sentence)
  print("\n")
  print(f"Number of happy words: {number_happy(sentence)}")
  print(f"Number of sad words: {number_sad(sentence)}")
  print(f"\nSentence Tone: {check_happy(sentence)}")


if __name__ == "__main__":
    main()
