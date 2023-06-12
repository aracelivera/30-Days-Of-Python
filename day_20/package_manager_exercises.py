# Day 20 - Package manager

# Exercises

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

# pip install requests
import requests
from collections import Counter
import re

def find_most_frequent_words(url, num_words):
    # Fetch the text content from the URL
    response = requests.get(url)
    text = response.text

    # Clean the text by converting to lowercase, removing punctuation, and extra whitespaces
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())

    # Split the text into words
    words = cleaned_text.split()

    # Count the occurrences of each word
    word_counts = Counter(words)

    # Get the most frequent words
    most_frequent_words = word_counts.most_common(num_words)

    return most_frequent_words


url = 'http://www.gutenberg.org/files/1112/1112.txt'
most_frequent_words = find_most_frequent_words(url, 10)
print(most_frequent_words)

