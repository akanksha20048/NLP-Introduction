# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:08:12 2020

@author: akanksha_pandey
"""

import codecs
import string
import nltk
import re
from re import *


#Read the file
file_path = "C:/Users/Akanksha/Downloads/20news-19997/20_newsgroups/rec.motorcycles/101725"


#Question 01
def read_file(file):
    fp = codecs.open(file, 'r', encoding = 'utf-8', errors = 'ignore')
    text = fp.read()
    from nltk.tokenize import RegexpTokenizer
    tokenizer = RegexpTokenizer('\w+')
    filterdText=tokenizer.tokenize(text)
    print("Number of words:",len(filterdText))
    from nltk.tokenize import sent_tokenize
    print("Number of sentences:",len(sent_tokenize(text)))

#Question 02
def read_file2(file):
    fp = codecs.open(file, 'r', encoding = 'utf-8', errors = 'ignore')
    text = fp.read()
    r = compile(r'(\b[aeiouAEIOU][a-zA-Z]*[0-9]*)', MULTILINE)
    print("Number of Words Starting with vowels:",len(r.findall(text)))
    r = compile(r'\b[b-df-hj-np-tv-zB-DF-HJ-NP-TV-Z][a-zA-Z]*[0-9]*', MULTILINE)
    print("Number of words starting with consonants:",len(r.findall(text)))

#Question 03
def read_file3(file):
    fp = codecs.open(file, 'r', encoding = 'utf-8', errors = 'ignore')
    text = fp.read()
    r = compile(r'\S+@\S+[.]\S+', MULTILINE)
    print("email-ids:",r.findall(text))

#Question 04
def read_file4(file):
    fp = codecs.open(file, 'r', encoding = 'utf-8', errors = 'ignore')
    text = fp.read()
    text = text.lower()
    from nltk.tokenize import sent_tokenize
    tokenizer = sent_tokenize(text)
    word = input("enter the first word of sentence : ")
    word = word.lower()
    count = 0
    for w in tokenizer:
        if re.findall('^'+word+" ",w):
            print(w)
            count = count+1
    print(" ")
    print("Count is: ",count)

#Question 05
def read_file5(file):
    fp = codecs.open(file, 'r', encoding = 'utf-8', errors = 'ignore')
    text = fp.read()
    text = text.lower()
    from nltk.tokenize import sent_tokenize
    tokenizer = sent_tokenize(text)
    word = input("enter the last word of sentence : ")
    word = word.lower()
    count = 0
    i = 1
    for w in tokenizer:
        if re.findall(" "+word+".?$",w):
            print(w)
            print(" ")
            count = count+1
    print(" ")
    print("Count is: ",count)

#Question 06
def read_file6(file):
    fp = codecs.open(file, 'r', encoding = 'utf-8', errors = 'ignore')
    text = fp.read()
    text = text.lower()
    from nltk.tokenize import sent_tokenize
    tokenizer = sent_tokenize(text)
    word = input("enter the word to be searched : ")
    word = word.lower()
    count = 0
    i = 1
    for w in tokenizer:
        if re.findall(word,w):
            print(" ")
            count = count + 1
            print(i," sentence which has: ",word, " is: ")
            print(w)
            print("______________________________________________________________")
            i = i+1
    print(" ")
    print("Total count is: ",count)

#Question 07
def read_file7(file):
    fp = codecs.open(file, 'r', encoding = 'utf-8', errors = 'ignore')
    text = fp.read()
    r = compile(r'[a-z A-Z]*[0-9]*\?', MULTILINE)
    print(r.findall(text))

#Question 08
def read_file8(file):
    fp = codecs.open(file, 'r', encoding = 'utf-8', errors = 'ignore')
    text = fp.read()
    r = compile(r'([012]*[0-9]) [a-zA-Z]* [0-9][0-9][0-9]*[0-9]* (2[0-3]|[01][0-9]):([0-5][0-9]):([0-5]?[0-9])', MULTILINE) 
    time = r.findall(text)
    for t in range (len(time)): 
        for ms in range (len(time[t])):
            if ms == 0:
                continue;
            if ms == 2:
                print(time[t][ms],"minutes", end = " ")
            if ms == 3:
                print(time[t][ms],"seconds")

#Question 09
def read_file9(file):
    fp = codecs.open(file, 'r', encoding = 'utf-8', errors = 'ignore')
    text = fp.read()
    r = compile(r'(\b(?:[A-Z][a-z]*){2,})', MULTILINE)
    print(r.findall(text))

#Menu driven program

while True:
    option = input("Please Enter the question number (press 0 to exit): ")
    if option == '0':
        break
    if option == '1':
        read_file(file_path)
    elif option == '2':
        read_file2(file_path)
    elif option == '3':
        read_file3(file_path)
    elif option == '4':
        read_file4(file_path)
    elif option == '5':
        read_file5(file_path)
    elif option == '6':
        read_file6(file_path)
    elif option == '7':
        read_file7(file_path)
    elif option == '8':
        read_file8(file_path)
    elif option == '9':
        read_file9(file_path)
    else:
        print("Wrong question number")