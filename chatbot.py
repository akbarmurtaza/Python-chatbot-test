# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 17:42:42 2018

@author: 
"""

def main():
    print("Hello ! Welcome to tech support chatbot! Enter your query for an answer :")
    print("Press 1 For Querying")
    print("Press 2 To Exit")
    while(1):
        choice= input("Enter choice(From 1/2):")
        if choice=='1':
                str1 = str(input("Enter Query: "))
                queryanswer(str1)
        if choice=='2':
            exit()


def queryanswer(query):
    
    answers = ["Try plugging the device into an electrical outlet",
               "Try turning the device off and on again",
               "Access the settings at 108.12.21.99 inside your web browser",
               "Our product is an internet modem which allows you to connect to the internet",
               "Insert the ethernet cable into the ethernet port",
               "I do not understand your problem, kindly contact tech support"]
 
    if ('on' in query or 'off' or 'wont' in query or 'power' in query and 'device' in query ):            
        print(answers[0])
    if ('not' in query  or 'working' in query or 'isnt' in query or 'is not' in query):
        print(answers[1])
    if ('where' in query  or 'how' in query or 'do' in query or 'access' in query or 'settings' in query or 'configure' in query and 'device' in query ):
        print(answers[2])  
    if ('product' in query or 'specification' in query or 'of' in query or 'the' in query and 'product' in query ):
        print(answers[3])  
    if ('how' in query  or 'connect' in query or 'internet' in query):
        print(answers[4])  
    if ('what' in query  or 'is' in query or 'your' in query or 'are' in query or 'called' in query or 'are' in query or 'you' in query and 'name' in query ):
        print('My name is chatbot001')

        
main()      