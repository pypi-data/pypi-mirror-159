# SPDX-License-Identifier: LGPL-3.0-or-later

import gptc.tokenizer, gptc.compiler, gptc.exceptions, gptc.weighting
import warnings


class Classifier:
    """A text classifier.

    Parameters
    ----------
    model : dict
        A compiled GPTC model.

    max_ngram_length : int
        The maximum ngram length to use when tokenizing input. If this is
        greater than the value used when the model was compiled, it will be
        silently lowered to that value.

    Attributes
    ----------
    model : dict
        The model used.

    """

    def __init__(self, model, max_ngram_length=1):
        if model.get("__version__", 0) != 3:
            raise gptc.exceptions.UnsupportedModelError(
                f"unsupported model version"
            )
        self.model = model
        self.max_ngram_length = min(
            max_ngram_length, model.get("__ngrams__", 1)
        )

    def confidence(self, text):
        """Classify text with confidence.

        Parameters
        ----------
        text : str
            The text to classify

        Returns
        -------
        dict
            {category:probability, category:probability...} or {} if no words
            matching any categories in the model were found

        """

        model = self.model

        text = gptc.tokenizer.tokenize(text, self.max_ngram_length)
        probs = {}
        for word in text:
            try:
                weight, weighted_numbers = gptc.weighting.weight(
                    [i / 65535 for i in model[word]]
                )
                for category, value in enumerate(weighted_numbers):
                    try:
                        probs[category] += value
                    except KeyError:
                        probs[category] = value
            except KeyError:
                pass
        probs = {
            model["__names__"][category]: value
            for category, value in probs.items()
        }
        total = sum(probs.values())
        probs = {category: value / total for category, value in probs.items()}
        return probs

    def classify(self, text):
        """Classify text.

        Parameters
        ----------
        text : str
            The text to classify

        Returns
        -------
        str or None
            The most likely category, or None if no words matching any
            category in the model were found.

        """
        probs = self.confidence(text)
        try:
            return sorted(probs.items(), key=lambda x: x[1])[-1][0]
        except IndexError:
            return None
