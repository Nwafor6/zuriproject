# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    if anagram.lower() in word.lower():      
        return True
    return False

print(find_anagram('prince', 'Glory'))


