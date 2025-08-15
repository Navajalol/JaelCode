import os

def Main():
    print("hello World")
    osScript()

def osScript():
    userFile = input()
    file = open(userFile, 'r')
    print(file.read())
    
Main()

