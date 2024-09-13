"""Translate "Hello world" in binary and say hello to the user in binary language."""

#Translate "Hello world in binary". How?
#Translate H into binary
hOrdinal = ord('H')
hBinValue = bin(hOrdinal)
hBinOutput =  hBinValue[2:]

#Translate e into binary
eBinOutput = bin(ord('e'))[2:]

#Translate l into binary
lBinOutput = bin(ord('l'))[2:]

#Translate o into binary
oBinOutput = bin(ord('o'))[2:]

#compose the greeting out of of its parts
greeting = f"{hBinOutput} {eBinOutput} {lBinOutput} {lBinOutput} {oBinOutput}"

#print the translated greeting to the user
print(greeting)

#another way to compose the greeting is with concatation (adding multiple strings together)
concatGreeting  = hBinOutput + ' ' + eBinOutput + ' ' + lBinOutput + ' ' + lBinOutput + ' ' + oBinOutput

#print the concatenated greeting
print(concatGreeting)

#print multiple strings
print(hBinOutput, eBinOutput, lBinOutput, lBinOutput, oBinOutput, sep = " | ")

