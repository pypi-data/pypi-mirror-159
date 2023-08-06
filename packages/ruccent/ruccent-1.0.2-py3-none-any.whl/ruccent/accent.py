from typing import NamedTuple, Sequence, Optional, Iterable

import pickle
from gzip import GzipFile as zipfile
from pathlib import Path
from collections import defaultdict
from functools import cache


class TrainRecord(NamedTuple):
    accent: int
    count: int
    text: str

TDataset = Sequence[TrainRecord]
TAccentChance = tuple[int, float]
TTokenStat = dict[str, tuple[TAccentChance, ...]]


@cache
def ngrams(length: int, min_window: int, max_window: int) -> list[slice]:
    max_window = min(length, max_window)
    window_sizes = range(min_window, max_window + 1)
    return [slice(begin, begin + window) 
            for window in window_sizes
            for begin in range(0, length - window + 1)
           ]


class Accent:
    def __init__(self, path: Path = None):
        if path is None:
            path = Path(__file__).parent / 'accent.mdl'
        with zipfile(path, 'rb') as f:
            self.min_window, \
            self.max_window, \
            self.frequency = pickle.load(f)

    def _best_prediction(self, word: str) -> Optional[int]:
        ngram_stat = self.frequency
        length = len(word)
        counter = [0] * length
        for ngram in ngrams(length, self.min_window, self.max_window):
            token = word[ngram]
            if token in ngram_stat:
                for idx, chance in ngram_stat[token]:
                    accent = ngram.start + idx
                    counter[accent] += chance
        if max_chance := max(counter):
            return counter.index(max_chance)

    def predict(self, word: str) -> Optional[int]:
        # the boundary "_word_" improves the quality of prediction
        # a similar modification should also occur during training
        word = f' {word} '
        accent = self._best_prediction(word)
        if accent is not None:
            return accent - 1  # compensate for the change in the target word

class AccentTrain(Accent):
    # noinspection PyMissingConstructor,PyUnusedLocal
    def __init__(self, path: Path = None):
        self.min_window = 0
        self.max_window = 0
        self.frequency = {}

    @staticmethod
    def _collect_ngram(items: TDataset, window: int) -> TTokenStat:
        # data collection
        no_accent_pos = window
        counter = defaultdict(lambda: [0] * (window + 1))
        for accent, count, word in items:
            for ngram in ngrams(len(word), window, window):
                token = word[ngram]
                idx = accent - ngram.start if ngram.start <= accent < ngram.stop else no_accent_pos
                counter[token][idx] += count
        # normalization of probabilities
        stat = {}
        for token, counts in counter.items():
            total = sum(counts)
            labels = tuple((lbl, cnt / total) for lbl, cnt in enumerate(counts[:-1]) if cnt)
            if labels:
                stat[token] = labels
        return stat

    def fit(self, items: Iterable[TrainRecord], ngram: tuple[int,int] = (3,7)):
        self.min_window, max_window = ngram
        items = tuple(TrainRecord(accent + 1, count, f' {text} ') for accent, count, text in items)
        incorrect = items
        window_sizes = range(self.min_window, max_window + 1)
        for window in window_sizes:
            print(f'{window = }')
            stat_w = self._collect_ngram(incorrect, window)
            if not stat_w:
                break
            self.frequency.update(stat_w)
            self.max_window = window
            incorrect = (rec for rec in items if rec.accent != self._best_prediction(rec.text))

    # def _drop_rare(self):
    #     from collections import Counter
    #     freq = self.frequency
    #     counter = Counter()
    #     for _, count, word in items:
    #         for ngram in ngrams(len(word), self.min_window, self.max_window):
    #             token = word[ngram]
    #             if token in freq:
    #                 counter[token] += count
    #
    #     # 0.1% редких не влияет на точность по тексту, сокращая модель на 30-40%
    #     accumulate = counter.total() // 1000
    #     drop = []
    #     for token, count in counter.most_common()[::-1]:
    #         accumulate -= count
    #         if accumulate > 0:
    #             drop.append(token)
    #     for token in drop:
    #         del freq[token]

    def save(self, path: Path = None):
        if path is None:
            path = Path('accent.mdl')
        with zipfile(path, 'wb') as f:
            stored = (self.min_window, self.max_window, self.frequency)
            pickle.dump(stored, f)
