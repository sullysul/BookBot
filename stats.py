def get_num_words(text):
    # returns the number of words in the given text
    words = text.split()
    return len(words)


def get_char_counts(text):
    """Returns a dictionary of character frequencies (case-insensitive)."""
    text = text.lower()
    chars = {}
    for c in text:
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars



