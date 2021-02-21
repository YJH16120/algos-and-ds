# Problem
Given two strings check if they are anagrams of each other. Spaces or punctuation does not matter.
For example:  
"dog" is an anagram of "God", ignore the capitilization as well.
"public relations" is an anagram of "Crap built on lies".

There are 3 ways to find the solution, method 1:   
```py
def anagram(stringOne, stringTwo):
    stringOne = stringOne.replace(" ", "").lower()
    stringTwo = stringTwo.replace(" ", "").lower()

    return sorted(stringOne) == sorted(stringTwo)
```  
Method 2:  
```py
def anagram(stringOne, stringTwo):
    stringOne = [x.lower() for x in stringOne if x.isalpha()]
    stringTwo = [x.lower() for x in stringTwo if x.isalpha()]

    return sorted(stringOne) == sorted(stringTwo)
```
Method 3:
```py
def anagram(stringOne, stringTwo):
    if len(stringOne) != len(stringTwo): # An anagram must contain the same number of characters
        return False

    seen = dict() # an empty dictionary to store letters and how many times they appear
    for letter in stringOne: 
        if letter.isalpha():
            if letter in seen: # If the letter is in seen increment it by 1, meaning it appears how many times in string one
                seen[letter] += 1
            else:
                seen[letter] = 1 # If the letter is not in seen, make a new entry and set the number of occurances to 1

    for letter in stringTwo:
        if letter.isalpha():
            if letter in seen:
                seen[letter] -= 1 # Same thing done here except in reverse. If it appears then reduce the count by one. 
            else:
                seen[letter] = 1 # If the letter has never appeared before set it to 1.

    """Checks to see if the occurances of all letters has been reduced to 0. Because for them to be anagrams,
    the amount of letters will remain constant. Since you're just rearranging the order of the letters."""
    for k in stringOne:
        if k.islapha():
        if seen[k] != 0: 
            return False
    return True
```
The point of method 3 is to expose you to the fact that many solutions that require a solution from within an array needs the use of a dictionary.