# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagrams(word, anagram):
    # [assignment] Add your code here
    word_list = list(word)
    word_list.sort()
    anagram_list = list(anagram)
    anagram_list.sort()

    if word_list == anagram_list:
        return True
    else:
        return False


# print(find_anagrams("hello", "check"))
print(find_anagrams("below", "elbow"))
