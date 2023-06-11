# Day 19 - File Handling

# Exercises: Level 1

# 1. Write a function which count number of lines and number of words in a text. All the files are in the data the folder:
def count_lines_and_words(file_path):
    line_count = 0
    word_count = 0

    with open(file_path, 'r') as f:
        for line in f:
            line_count += 1  # Counting lines

            words = line.split()
            word_count += len(words)  # Counting words
    return line_count, word_count

# or
def count_lines_and_words_v2(file_path):
    with open(file_path) as f:
        lines = f.readlines()  # list of lines
        words = []
        for line in lines:
            words.extend(line.split())
        return len(lines), len(words)


#   a) Read obama_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('./data/obama_speech.txt')
print(f'Number of lines: {lines}\nNumber of words: {words}')

#   b) Read michelle_obama_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('./data/michelle_obama_speech.txt')
print(f'Number of lines: {lines}\nNumber of words: {words}')

#   c) Read donald_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('./data/donald_speech.txt')
print(f'Number of lines: {lines}\nNumber of words: {words}')

#   d) Read melina_trump_speech.txt file and count number of lines and words
lines, words = count_lines_and_words('./data/melina_trump_speech.txt')
print(f'Number of lines: {lines}\nNumber of words: {words}')

# 2. Read the countries_data.json data file in data directory, create a function that finds the ten most spoken languages
import json

def most_spoken_languages(filename,n):
    with open(filename, encoding='utf-8') as f:
        countries_list = json.load(f)
        languages_in_countries =[]
    for country in countries_list:
        languages_in_countries.extend(country["languages"])
    
    language_count = dict((language, languages_in_countries.count(language)) for language in languages_in_countries)
    languages_count_list = list(language_count.items())
    languages_sorted_by_count = sorted(languages_count_list, key=lambda x: x[1], reverse=True)
    most_spoken_languages= languages_sorted_by_count[:n]  
    return [(count, language) for language, count in most_spoken_languages] 

print(most_spoken_languages('./data/countries_data.json', 10))
print(most_spoken_languages('./data/countries_data.json', 3))

# 3. Read the countries_data.json data file in data directory, create a function that creates a list of the ten most populated countries
import json
def most_populated_countries(filename, top):
    with open(filename, encoding='utf-8') as f:
        countries_list = json.load(f)
    sorted_countries = sorted(countries_list, key=lambda x: x['population'], reverse=True)
    top_countries = sorted_countries[:top]
    result = [{'country': country['name'], 'population': country['population']} for country in top_countries]
    return result

print(most_populated_countries('./data/countries_data.json',10))
print(most_populated_countries('./data/countries_data.json',3))

# Exercises: Level 2

# 4. Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re

def extract_email_addresses(file_path):
    email_addresses = []
    with open(file_path, 'r') as f:
        for line in f:
            match = re.search(r"(?i)From: (\S+@\S+)", line)
            if match:
                email_addresses.append(match.group(1))
    return email_addresses

email_list = extract_email_addresses('./data/email_exchange_big.txt')

print(email_list)

# 5. Find the most common words in the English language. Call the name of your function find_most_common_words, it will take two parameters - a string or a file and a positive integer, indicating the number of words. Your function will return an array of tuples in descending order. 
from collections import Counter
import re
    
def find_most_frequent_words(text,n):
    with open(text, 'r') as file:
        text = file.read()
    words = re.findall(r'\b\w+\b', text.lower())
    word_count=  Counter(words)
    return [(count, word) for word, count in word_count.most_common(n)]

# 6. Use the function, find_most_frequent_words to find: 
#   a) The ten most frequent words used in Obama's speech 
print(find_most_frequent_words('./data/obama_speech.txt', 10))
#   b) The ten most frequent words used in Michelle's speech 
print(find_most_frequent_words('./data/michelle_obama_speech.txt', 10))
#   c) The ten most frequent words used in Trump's speech 
print(find_most_frequent_words('./data/donald_speech.txt', 10))
#   d) The ten most frequent words used in Melina's speech
print(find_most_frequent_words('./data/melina_trump_speech.txt', 10))

# 7. Write a python application that checks similarity between two texts. It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. For instance check the similarity between the transcripts of Michelle's and Melina's speech. You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). List of stop words is:
stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]

import re
from collections import Counter
from math import sqrt

# Clean the text by converting to lowercase, removing punctuation, and extra whitespaces
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

# Remove stop words from the text
def remove_stop_words(text, stop_words):
    words = text.split()
    filtered_words = [word for word in words if word not in stop_words]
    return ' '.join(filtered_words)

# Calculate the similarity between two texts using cosine similarity
def check_text_similarity(text1, text2):
    cleaned_text1 = clean_text(text1)
    cleaned_text2 = clean_text(text2)
    
    filtered_text1 = remove_stop_words(cleaned_text1, stop_words)
    filtered_text2 = remove_stop_words(cleaned_text2, stop_words)
    
    # Create word frequency vectors
    vector1 = Counter(filtered_text1.split())
    vector2 = Counter(filtered_text2.split())
    
    # Calculate dot product
    dot_product = sum(vector1[key] * vector2[key] for key in vector1 if key in vector2)
    
    # Calculate magnitude of vectors
    magnitude1 = sqrt(sum(vector1[key] ** 2 for key in vector1))
    magnitude2 = sqrt(sum(vector2[key] ** 2 for key in vector2))
    
    # Calculate cosine similarity
    similarity = dot_product / (magnitude1 * magnitude2)
    
    return similarity

# Read text from a file
def read_text_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text


# Example with string input
#speech1 = "Michelle's speech text here"
#speech2 = "Melina's speech text here"

#similarity_score = check_text_similarity(speech1, speech2)
#print("Similarity score:", similarity_score)

# Example with file input

speech1 = read_text_from_file('./data/melina_trump_speech.txt')
speech2 = read_text_from_file('./data/michelle_obama_speech.txt')

similarity_score = check_text_similarity(speech1, speech2)
print("Similarity score:", similarity_score)
