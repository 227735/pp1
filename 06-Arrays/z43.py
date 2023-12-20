def count_words(text):
    words = text.split()
    return len(words)

def longest_to_shortest(text):
    words = text.split()
    sorted_words = sorted(words, key=len, reverse=True)
    return sorted_words

def alphabetically_ordered(text):
    words = text.split()
    return sorted(words, key=str.lower)


text = "An apple a day keeps the doctor away"
