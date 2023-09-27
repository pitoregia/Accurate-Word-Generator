import os
from collections import Counter
import itertools

# Load the list of valid words into a set
with open("word_list/ID_wordlist_strict.txt", "r") as f:
    VALID_WORDS = set(line.strip() for line in f)

# Count the number of occurrences of each letter in the input word
letters = input("Enter the letters: ")
letter_counts = Counter(letters)

# Generate all possible combinations of letters
combinations = set()
for i in range(1, len(letters)+1):
  for combination in itertools.product(letters, repeat=i):
    combination_str = "".join(combination)
    # Count the number of occurrences of each letter in the generated word
    combination_counts = Counter(combination_str)
    # Check that the generated word contains at most the same number of occurrences of each letter as the input word
    if all(combination_counts[letter] <= letter_counts[letter] for letter in combination_counts):
      if combination_str in VALID_WORDS:
        combinations.add(combination_str)

# Sort the generated words by length
sorted_words = sorted(combinations, key=len, reverse=True)

# Write the generated words to a file
filename = f"{letters}.txt"
with open(filename, "w") as f:
  for word in sorted_words:
    f.write(word + "\n")

print("Generated", len(combinations), "valid words")
os.startfile(filename)