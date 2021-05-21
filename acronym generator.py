#Abreviations are short forms Like Dr, Prof, etc
#Acronyms contains the 1st letters of each word
#Initialism is when the abbreviation or accronym is SPELLED 
#in pronunciation. Ex- URL, LOL, LMFAO###


#ACRONYM GENERATOR
print("Acronym Generator")
inp= input("Enter a phrase :")
a=inp.split()
acr=""
for i in a:
    acr=acr+i[0].upper()
    
print("Your acronym:", acr)