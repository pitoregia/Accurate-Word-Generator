# Word Generator from Letters

## Background

This code is a Python script that generates all possible valid words from a given set of letters. It uses the `itertools` module to generate all possible combinations of letters, and the `Counter` class to count the occurrences of each letter. The generated words are checked against a list of valid words loaded from a file (ID_wordlist.txt) or you can add your own word list, and the valid words are sorted by length and written to a file.

I made this for Shopee Tebak Kata so you can easily put the letters given and it will automatically give all the possible words (in Bahasa Indonesia).

## Usage

1. Clone the repo
   ```sh
   git clone https://github.com/pitoregia/Accurate-Word-Generator
   ```
2. Run the app
   ```sh
   python generator.py
   ```
 3. Input the letters and it will automatically generated the files.
