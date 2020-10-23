## Author: Feras
## Description: A function that counts the length of a string without using len()

userInput = input('Enter a string:\n')

def stringLength(userInput):
    result = 0
    for string in userInput:
        if string != None:
            result += 1
    return result
print('The length of the string is',stringLength(userInput))
