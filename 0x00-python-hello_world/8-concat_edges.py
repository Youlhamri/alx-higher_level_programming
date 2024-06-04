#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = f"{str.rsplit(',')[2][:28]} with Python"
str = str[1:]
print(str)