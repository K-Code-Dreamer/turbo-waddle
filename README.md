# turbo-waddle

import json
from difflib import get_close_matches

words_data = json.load(open("Dictionary.json"))

def word_meaning(word):
  
    word = word.lower()
    
    if word in words_data:
        return words_data[word]
      
    elif word.title() in words_data:
        return words_data[word.title()]
      
    elif word.upper() in words_data:
        return words_data[word.upper()]
      
    elif len(get_close_matches(word, words_data.keys())) >0:
       
        similar_words_list = list(map(str, get_close_matches(word, words_data.keys())))
        
        ans = input("Did you mean %s instead? Enter 'Y' for yes or 'N' for No " % similar_words_list)
        
        if ans.lower() == 'y':
            # asking user to select the word
            index = input("Enter the position number of word to select the word. Ex 1 or 2 or 3 : ")
            return word_meaning(get_close_matches(word, words_data.keys())[int(index)-1])
        elif ans.lower() == 'n':
            print("Wrong Search!!! Please try again")
        else:
            print("Sorry, We don't understand you!!!!")
    else:
        print("Wrong Search!!! Please try again")

def Input():
    word = input("Enter the word you want to search :")
    print(word_meaning(word))
    Repeat()

def Repeat():
    Again = input("Would you like to search another word? Y/N ")
    if Again == "Y":
        Input()
    elif Again == "N":
        print("Thank you")

Input()
