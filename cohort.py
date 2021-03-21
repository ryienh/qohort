"""Cohort lexical retrieval model simulator

Python implementation of Marslen-Wilson et. al.'s cohort -- a model
of lexical lexical retreival. The original cohort paper is linked here:
TODO add paper
"""
import os
from collections import deque
from typing import Union, List, Any, Tuple

import eng_to_ipa as ipa


class Cohort_Model:

    # begin public member functions
    def __init__(self, lexicon_path=None):

        self.__lexicon = self.__parse_lexicon(lexicon_path)

    def simulate_word_retreival(self, in_word: str) -> Tuple[int, str]:
        """Simulate lexical retrieval of a single word"""

        # input simulate stream with deque
        temp = self.__get_phonemes(in_word, length="single")[0]
        print(temp)
        stream = deque(self.__split_word(temp))  # only one pronounciation needed

        # build candidates
        candidates = {}
        word_initial_phoneme = stream.popleft()

        for word in self.__lexicon:
            for version in word:
                if version[0] == word_initial_phoneme:
                    candidates[version] = True

        print("Initial cohort size", print(len(candidates)))

        found = False
        round = 1
        while found == False:

            in_phoneme = stream.popleft()

            print("Cohort size in round ", round)

        return len(candidates), "hello"

    # begin attributes
    @property
    def lexicon(self):

        if len(self.__lexicon):
            return self.__lexicon
        else:
            print("Warning: Lexicon empty.")
            return None

    # begin private helper functions
    def __parse_lexicon(
        self, lexicon_path: Union[str, bytes, os.PathLike, None]
    ) -> List[List[str]]:

        if lexicon_path is None:
            return List()

        with open(lexicon_path) as file:
            raw_lexicon = file.read()

        return self.__get_phonemes(raw_lexicon)

    def __get_phonemes(self, english: str, length: str = "many") -> List[Any]:

        if length == "many":
            return ipa.ipa_list(english)
        elif length == "single":
            return ipa.ipa_list(english)[0]
        else:
            raise ValueError('length must be one of "many", "single"')

    def __split_word(self, word: str) -> List[str]:
        return [char for char in word]
