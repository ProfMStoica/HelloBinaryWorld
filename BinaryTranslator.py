"""Translates text and numbers into binary"""

"""Translate text into its binary representation"""
def translateText(textToTranslate):
    binTranslation = ""
    
    #repeat translation each character in the input text
    for index in range(len(textToTranslate)):
        #get the numeric value of the current character
        numValue = ord(textToTranslate[index])
        
        #translate the numberic value into binary
        binValue = bin(numValue)
        
        #add the translated character to the translation
        binTranslation =  binTranslation + binValue[2:] + " "
    return binTranslation


"""Translate a given number into its binary representaiton"""
def translateNum(numToTranslate):
    #TODO: implement number translation
    binTranslation = ""
    pass
    return binTranslation

