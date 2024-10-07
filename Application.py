"""Interaction with the user and coordination of the program. This is the main
   module of this application.
"""
import BinaryTranslator

#ask the user for a text input
textInput = input("Please enter the text to translate into binary: ")

#use the binary translator to translate the text input
translation = BinaryTranslator.translateText(textInput)

#output the binary translation
print(f"The translation of {textInput} is:\n{translation}")

#ask the user for a number
numInput = int(input("Please enter a number to translate into binary"))

#use the binary translator to translate the number into binary
translation = BinaryTranslator.translateNum(numInput)

#output the binary translation
print(f"The translation for {numInput} is:\n{translation}")