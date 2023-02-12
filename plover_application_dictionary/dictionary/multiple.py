from __future__ import annotations
from typing import Tuple

import json

from plover.steno_dictionary import StenoDictionary

from plover_application_dictionary.dictionary import SingleApplicationDictionary


class MultipleApplicationDictionary(StenoDictionary):
    readonly = True

    def __init__(self):
        super().__init__()
        self._single_dictionaries = []

    def _load(self, filename: str) -> None:
        with open(filename) as f:
           data = json.load(f)

        for entry in data:
            single = SingleApplicationDictionary()
            single.load_json(filename, entry)
            self._single_dictionaries.append(single)

            if single.longest_key > self._longest_key:
                self._longest_key = single.longest_key

    def _save(self, filename: str) -> None:
        pass

    def __getitem__(self, key: Tuple[str]) -> str:
        for single in self._single_dictionaries:
            if len(key) > single.longest_key:
                continue
            try:
                return single[key]
            except KeyError:
                continue
        raise KeyError

    def get(self, key: Tuple[str], fallback: str = None) -> str | None:
        try:
            return self[key]
        except KeyError:
            return fallback
