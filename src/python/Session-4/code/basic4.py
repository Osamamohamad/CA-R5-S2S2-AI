import random
def generate_password(length:str) -> str:
    '''
    this function generates a random password of the specified length using a combination of uppercase letters, lowercase letters, digits, and special characters.
    Args:
        length (str): The desired length of the password.
    Returns:
        str: The generated password.
    '''
    cracters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password=""

    for _ in range(int(length)):
        password += random.choice(cracters)

    return password

def countWords(Words:str) -> dict:
    '''
    this function counts the number of words in a given string.
    Args:
        Words (str): The input string       .
    Returns:
        dict: A dictionary with words as keys and their counts as values.
    '''

    words = Words.split()
    lst=set(words)
    word_count = {}
    for word in lst:
        word_count[word] = words.count(word)


    return word_count
from basic4 import countWords

text = input("Enter a string: ")
word_counts = countWords(text)
print("Word counts:", word_counts)