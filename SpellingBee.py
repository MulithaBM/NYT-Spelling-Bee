def validate(word_set) :
    count = 0
    center_check = False
    for letter in letter_set :
        if(letter in word_set) :
            count += 1
    if(center_letter in word_set) :
        count += 1
        center_check = True
    if(count == len(word_set) and center_check) :
        return True
    return False

def panagram_check(word_set) :
    if(letter_set.issubset(word_set)) :
        return True
    return False

letters = input("Letters : ")
center_letter = input("center letter : ")

words = []
panagrams = []
letter_set = set(letters)

file = open("US.txt", "r")
for line in file :
    word = line.rstrip()
    word_set = set(word)
    state = validate(word_set)
    if(state) :
        if(panagram_check(word)) :
            panagrams.append(word)
        else :
            words.append(word)
file.close()

words = sorted(words, key = lambda word : (len(set(word).intersection(letter_set)), -len(word)))

print(*words, sep = "\n")
print("Panagrams : ", *panagrams, sep = " " if panagrams else "Panagrams : No panagrams")