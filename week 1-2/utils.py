import string
from collections import Counter

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

def get_stats(cleaned, original):
    words = cleaned.split()
    word_count = len(words)
    char_count = len(original)
    char_no_space = len(original.replace(" ", ""))
    sentence_count = original.count('.') + original.count('!') + original.count('?')
    avg_word_len = round(sum(len(word) for word in words) / word_count, 2) if word_count else 0
    top_words = Counter(words).most_common(5)

    return {
        "Total Words": word_count,
        "Total Characters": char_count,
        "Characters (No Spaces)": char_no_space,
        "Sentence Count": sentence_count,
        "Average Word Length": avg_word_len,
        "Top 5 Words": top_words
    }