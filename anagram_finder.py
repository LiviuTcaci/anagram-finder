def read_words(filename):
    words = []
    with open(filename, 'r') as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                words.append(stripped)
    return words

def group_anagrams(words):
    anagram_dict = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagram_dict:
            anagram_dict[key] = []
        anagram_dict[key].append(word)
    return anagram_dict.values()

def main():
    words = read_words('sample.txt')
    groups = group_anagrams(words)
    for group in groups:
        print(' '.join(group))

if __name__ == '__main__':
    main() 