# SPDX-License-Identifier: LGPL-3.0-or-later


def tokenize(text, max_ngram_length=1):
    """Convert a string to a list of lemmas."""
    tokens = [""]

    for char in text.lower():
        if char.isalpha() or char == "'":
            tokens[-1] += char
        elif tokens[-1] != "":
            tokens.append("")

    tokens = [string for string in tokens if string]

    if max_ngram_length == 1:
        return tokens
    else:
        ngrams = []
        for ngram_length in range(1, max_ngram_length + 1):
            for index in range(len(tokens) + 1 - ngram_length):
                ngrams.append(" ".join(tokens[index : index + ngram_length]))
        return ngrams
