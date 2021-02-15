vowels = {"a", "e", "i", "o", "u", "y"}
upper_vowels = {"A", "E", "I", "O", "U", "Y"}

word = set(input("Provide a message to search for vowels in: "))

found_lower = vowels.intersection(word)
found_upper = upper_vowels.intersection(word)

for upper_vowel in found_upper:
    found_upper.discard(upper_vowel)
    if upper_vowel.lower() not in found_lower:
        found_upper.add(upper_vowel.lower())

found = found_lower.union(found_upper)

if found:
    print("Found vowels:")
    for vowel in found:
        print(vowel)
else:
    print("No vowels found in this message.")
