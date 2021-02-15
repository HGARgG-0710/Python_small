def vowel_search(word, vowels):
    been_labeled = False

    for letter in word:
        if letter.lower() in vowels :
            vowels[letter.lower()] += 1

    for vowel, times_found in sorted(vowels.items()):
        if not been_labeled:
            print("\nFound vowels:")
            been_labeled = True
    
        ending = "s" if times_found > 1 else ""
        
        if times_found > 0:
            print(vowel, "-", times_found, "time" + ending)


vowels = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
    "y": 0
}

word = input("Hi, enter the message.\nThe program will output all the vowels in it.\nMessage: ")

vowel_search(word, vowels)
