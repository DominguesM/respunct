__author__ = "Maicon Domingues"
__email__ = "dominguesm@outlook.com"

import re
import string
from itertools import zip_longest as iterzip

from simpletransformers.ner import NERModel


class RestorePuncts:
    def __init__(self, words_per_pred=250, overlap=20, use_cuda=False) -> None:
        """
        This package is intended for direct use as a punctuation
        restoration model for the general Portuguese language.

        Punctuation restoration works on arbitrarily large text.
        And uses GPU if it's available otherwise will default to CPU.

        List of punctuations we restore:
            * Upper-casing
            * Period: .
            * Exclamation: !
            * Question Mark: ?
            * Comma:  ,
            * Colon:  :
            * Semi-colon: ;
            * Apostrophe: '
            * Hyphen: -

        Args:
            - words_per_pred (int): maximum size of the parts into which the text will be divided.
            - overlap (int): size of the overlap between the parts
            - use_cuda (bool): indicates the use of the model in GPU

        """
        self.words_per_pred = words_per_pred
        self.valid_labels = [
            "OU",
            "OO",
            ".O",
            "!O",
            ",O",
            ".U",
            "!U",
            ",U",
            ":O",
            ";O",
            ":U",
            "'O",
            "-O",
            "?O",
            "?U",
        ]
        self.overlap = overlap
        self.model = NERModel(
            "bert",
            "dominguesm/bert-restore-punctuation-ptbr",
            labels=self.valid_labels,
            args={"silent": True, "max_seq_length": 512},
            use_cuda=use_cuda,
        )

    def restore_puncts(self, text: str):
        """
        Performs punctuation restoration on arbitrarily large text.

          Args:
              - text (str): Text to punctuate, it can be from a few words to the size you want.
        """

        # normalize the text
        text = self.prepare_text(text)

        # breaks text into smaller parts
        splits = [
            " ".join(split)
            for split in self.split_text(text, self.words_per_pred, self.overlap)
        ]

        # extract predictions, and discard logits
        predictions, _ = self.model.predict(splits)

        # create punctuated prediction
        result = self.make_results(predictions)

        return result

    @staticmethod
    def prepare_text(text: str):
        """
        Given a text, normalizes by removing all punctuation and making the text lowercase.
        """
        text = text.strip()
        text = text.replace("\n", " ").lower()
        text = text.translate(str.maketrans(" ", " ", string.punctuation))
        text = re.sub(" +", " ", text)
        return text

    @staticmethod
    def split_text(text, words_per_pred, overlap):
        """
        Splits text into smaller pieces with overlap.
        This is done because of the model's 512 token limit.

        Args:
            - words_per_pred (int): maximum size of the parts into which the text will be divided.
            - overlap (int): size of the overlap between the parts

        Return example:
            [["word1", "word2" ..], [...] ]
        """
        seq = text.replace("\n", " ").split(" ")
        for x in iterzip(
            *[seq[i :: words_per_pred - overlap] for i in range(words_per_pred)]
        ):
            yield tuple(i for i in x if i is not None) if x[-1] is None else x

    def make_results(self, predictions):
        """
        Given a full text and predictions of each slice combine predictions into a single text again
        """
        text_restored = []
        total_predictions = len(predictions)

        for i, preds in enumerate(predictions):
            if i != (total_predictions - 1):
                preds = preds[0 : -self.overlap]

            for pred in preds:

                text, value = list(pred.items())[0]

                if value[1] == "U":
                    text = text.capitalize()

                if value[0] != "O":
                    text += value[0]

                text_restored.append(text)

        return " ".join(text_restored)
