def anagram(stringOne, stringTwo):
    stringOne, stringTwo = stringOne.lower(), stringTwo.lower()
    if len(stringOne) != len(stringTwo):
        return False

    seen = dict()
    for letter in stringOne: 
        if letter.isalpha():
            if letter in seen:
                seen[letter] += 1
            else:
                seen[letter] = 1

    for letter in stringTwo:
        if letter.isalpha():
            if letter in seen:
                seen[letter] -= 1
            else:
                seen[letter] = 1

    for k in stringOne:
        if k.isalpha():
            if seen[k] != 0: 
                return False
        return True

out = anagram("-aNna", "n-Ana")
print(out)

out = anagram("-asdd", "dxsi")
print(out)
