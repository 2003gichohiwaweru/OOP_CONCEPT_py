class Person:

    def __init__(self, name, age): # class constructor

        self.name = name 

        self.age = age 



    def displayInfo(self): # class method

        print('Person Name: ', self.name,', Age: ', self.age)

p1 = Person('Mutemi', 65)
p1.displayInfo()



class Book:

    def __init__(self,author):

        self.author=author



book1=Book("V.M.Shah")

book2=book1
"""
In this project, you are tasked to create a program that automates searching for a word definition in a dictionary. Follow the instructions to implement



Dictionary Project is provided here: 



We should have a data source (Download from the link above)
Learn how to load json data into a python dictionary
Create a function that returns a definition of a word
Consider a condition that the entered word is not in a dictionary
Consider input from user having different cases – upper/ lower case or mixed eg: RAIN/rain/RaIN
Make your dictionary program more intelligent incase users input a word with wrong spelling the program should be able to suggest the word that might be intended.
eg . pott instead of pot or rainn instead of rain. Tip: use difflib library here
"""

import json
import difflib

def load_dictionary():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return data


def get_definition(word, dictionary):
    word = word.lower()  # Convert input to lowercase
    
    if word in dictionary:
        return dictionary[word]
    else:
        similar_words = difflib.get_close_matches(word, dictionary.keys(), n=1, cutoff=0.8)
        if similar_words:
            suggestion = similar_words[0]
            return f"Word not found. Did you mean '{suggestion}'?"
        else:
            return "Word not found. No suggestions available."

def main():

    

    dictionary = load_dictionary()
    while True:
        word = input("Enter a word to get its definition (type 'quit' to exit): ")
        if word.lower() == 'quit':
            break
        definition = get_definition(word, dictionary)
        print(definition)
if __name__ == "__main__":
    main()
