text = "programming"

vowel_count = 0
consonant_count = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1

print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
