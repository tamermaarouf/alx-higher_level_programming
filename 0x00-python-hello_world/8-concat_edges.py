#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[str.rfind('object'):str.find('that')] + str[str.find('power'):str.find('very')] + str[:6]
print(str)
