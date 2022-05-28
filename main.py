# Check if two words are anagrams 

def find_anagram(word, anagram):
    if sorted(word) == sorted(anagram):
        result = True
    else:
        result = False

    return 'anagram test result is {} for {} and {}'.format(result,word,anagram)

word = input("Please enter first word: ")
anagram = input("Please enter second word: ")
print(find_anagram(word,anagram))