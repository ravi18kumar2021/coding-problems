'''
    Write a function that selects all words that have all the same vowels
    (in any order and/or number) as the first word, including the first
    word.
'''
def get_same_vowel_group(words):
    vowel = ''
    result = []
    for i in range(len(words)):
        if i == 0:
            result.append(words[i])
            for j in words[i]:
                if j in vowels:
                    vowel += j
                    vowels.remove(j)
        else:
            count = 0; is_found = False
            for k in words[i]:
                if k in vowel:
                    if count == 0:
                        is_found = True
                    count += 1
                if k in vowels:
                    is_found = False
                    break
            if count == len(vowel) and is_found:
                result.append(words[i])
    print(result)

vowels = ['a', 'e', 'i', 'o', 'u']
#words = ['toe', 'ocelot', 'maniac']
num = int(input("How many words want to enter : "))
words = []
for _ in range(num):
    word = input("Enter a word :")
    words.append(word)
get_same_vowel_group(words)