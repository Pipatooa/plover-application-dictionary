from __future__ import annotations
from typing import Dict, Tuple

import json
import re

from plover.dictionary.helpers import StenoNormalizer
from plover.steno import steno_to_sort_key
from plover.steno_dictionary import StenoDictionary

from plover_application_dictionary.window_tracker import WindowTracker


class SingleApplicationDictionary(StenoDictionary):
    def __init__(self):
        super().__init__()
        self._re_app = ""
        self._re_app_compiled = None
        self._re_class = ""
        self._re_class_compiled = None
        self._re_title = ""
        self._re_title_compiled = None

    def load_json(self, origin_file: str, data: Dict) -> None:
        self._re_app = data["app"]
        self._re_class = data["class"]
        self._re_title = data["title"]

        if self._re_app:
            self._re_app_compiled = re.compile(self._re_app)
        if self._re_class:
            self._re_class_compiled = re.compile(self._re_class)
        if self._re_title:
            self._re_title_compiled = re.compile(self._re_title)

        with StenoNormalizer(origin_file) as normalize_steno:
            self.update((normalize_steno(key), value) for key, value in data["entries"].items())

    def _load(self, filename: str) -> None:
        with open(filename) as f:
            data = json.load(f)
            self.load_json(filename, data)

    def _save(self, filename: str) -> None:
        mappings = [('/'.join(k), v) for k, v in self.items()]
        mappings.sort(key=lambda i: steno_to_sort_key(i[0], strict=False))

        data = {
            "app": self._re_app,
            "class": self._re_class,
            "title": self._re_title,
            "entries": dict(mappings)
        }

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")

    def _active_window_matches(self) -> bool:
        if self._re_app_compiled is not None:
            if not self._re_app_compiled.match(WindowTracker.current_app):
                return False
        if self._re_class_compiled is not None:
            if not self._re_class_compiled.match(WindowTracker.current_class):
                return False
        if self._re_title_compiled is not None:
            if not self._re_title_compiled.match(WindowTracker.current_title):
                return False
        return True

    def __getitem__(self, key: Tuple[str]) -> str:
        if not self._active_window_matches():
            raise KeyError
        return super().__getitem__(key)

    def get(self, key: Tuple[str], fallback: str = None) -> str | None:
        if not self._active_window_matches():
            return fallback
        return super().get(key, fallback)
