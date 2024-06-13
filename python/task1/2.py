def is_vowel(letter):
    vowels = 'aeiouAEIOU'
    if letter in vowels:
        return True
    else:
        return False
    
    
letter = input('enter a letter : ')
if is_vowel(letter) == True:
    print(f"{letter} is a vowel")
else:
    print(f"{letter} isn't a vowel")    