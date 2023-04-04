#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def printDictionary(LibDict): # TO PRINT THE DICTIONARY
    for key, value in LibDict.items():
        print(key, ":-")
        for innerKey, innerValue in value.items():
            print("\t",innerKey, ":", innerValue)

def search(LibDict):  # TO SEARCH DICTIONARY IN A NESTED DICTIONARY
    isFound = False
    outerSearch = input("Enter Outer Key to search:")
    if outerSearch not in LibDict:
        print("Value Not Found")
        isFound = True
    else:
        innerSearch = input("Enter Inner Key to search:")
        for key, values in LibDict.items():
            for innerKey, innerValues in values.items():
                if innerSearch == innerKey:
                    isFound = True
                    break
            if isFound == True:
                break
        if isFound == True:
            print(f"Value of {outerSearch} and {innerSearch} is {LibDict[outerSearch][innerSearch]}")
        else:
            print("Value Not Found")
            
def add(LibDict): # TO ADD A NESTED DICTIONARY
    outerSearch = input("Enter Outer Key to add:")
    if outerSearch in LibDict:
        print("Key Already found")
    else:
        name = input("Enter Book name:")
        Author = input("Enter Author name:")
        Pyear = input("Enter Publish Year:")
        newDict = {
            "Name" : name,
            "Author": Author,
            "Publish Year": Pyear
        }
        LibDict[outerSearch] = newDict

def remove(LibDict): # TO REMOVE A DICTIONARY
    outerSearch = input("Enter Outer Key to remove:")
    if outerSearch not in LibDict:
        print("Outer Key is not present")
    else:
        del LibDict[outerSearch]

#CREATING DICTIONARY

LibDict = {
    "Book1" : {
        "Name" : "A Breif History of Time",
        "Author" : "Stephan Hawking",
        "Publish year" : "1988"
    },
    "Book2" : {
        "Name" : "The Universe in a NutShell",
        "Author" : "Stephan Hawking",
        "Publish year" : "2001"
    },
    "Book3" : {
        "Name" : "The Meaning of Relativity",
        "Author" : "Albert Einstein",
        "Publish year" : "1922"
    }
}
#PRINTING DICTIONARY
printDictionary(LibDict)
#SEARCHING DESIRED VALUE BY USER
search(LibDict)
#ADD VALUE IN A DIRECTORY
add(LibDict)
print("\t--------------------------------")
print("\t---AFTER ADDING DIRECTORY IS ---")
print("\t--------------------------------")
printDictionary(LibDict)
#REMOVE VALUE IN A DIRECTORY
remove(LibDict)
print("\t----------------------------------")
print("\t---AFTER DELETING DIRECTORY IS ---")
print("\t----------------------------------")
printDictionary(LibDict)


# In[ ]:




