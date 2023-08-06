# SPDX-License-Identifier: LGPL-3.0-or-later

import gptc.tokenizer


def compile(raw_model, max_ngram_length=1):
    """Compile a raw model.

    Parameters
    ----------
    raw_model : list of dict
        A raw GPTC model.

    max_ngram_length : int
        Maximum ngram lenght to compile with.

    Returns
    -------
    dict
        A compiled GPTC model.

    """

    categories = {}

    for portion in raw_model:
        text = gptc.tokenizer.tokenize(portion["text"], max_ngram_length)
        category = portion["category"]
        try:
            categories[category] += text
        except KeyError:
            categories[category] = text

    categories_by_count = {}

    names = []

    for category, text in categories.items():
        if not category in names:
            names.append(category)

        categories_by_count[category] = {}
        for word in text:
            try:
                categories_by_count[category][word] += 1 / len(
                    categories[category]
                )
            except KeyError:
                categories_by_count[category][word] = 1 / len(
                    categories[category]
                )
    word_weights = {}
    for category, words in categories_by_count.items():
        for word, value in words.items():
            try:
                word_weights[word][category] = value
            except KeyError:
                word_weights[word] = {category: value}

    model = {}
    for word, weights in word_weights.items():
        total = sum(weights.values())
        model[word] = []
        for category in names:
            model[word].append(
                round((weights.get(category, 0) / total) * 65535)
            )

    model["__names__"] = names
    model["__ngrams__"] = max_ngram_length
    model["__version__"] = 3

    return model
