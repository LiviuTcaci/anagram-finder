# Anagram Finder

This project groups words from an input file into sets of anagrams.

## Objective
Identify and group anagrams from a given input file (one word per line).

## Setup
- Requires Python 3.
- `sample.txt` is in the same directory.

## Usage
Run the script with:
```sh
python anagram_finder.py
```

Each line of output will contain words that are anagrams of each other, separated by spaces.

## Design Decisions & Scalability

### Approach
- The program reads all words from the input file and groups them by sorting the letters in each word. Words with the same sorted letters are anagrams and are grouped together.
- I used a Python dictionary to store groups, which makes the lookup and grouping fast and simple.
- No external libraries are used—just standard Python.

### Maintainability & Performance
- The logic is split into small functions for clarity.
- The dictionary-based grouping is efficient for small to medium files (like the sample provided).

### Scalability
- For 10 million words: The current code reads all words into memory and uses a dictionary to group them. This works fine as long as your computer has enough RAM. On a typical laptop or PC, handling millions of words should be okay, but it might get slow if you run out of memory.
- For 100 billion words: The code would need to change because you can't fit that much data in memory. One idea is to process the file in smaller chunks and write intermediate results to disk, or use a database to store groups. For really huge datasets, you'd probably want to use special tools or frameworks (like Hadoop or Spark) and run the code on a cluster of computers instead of just one.