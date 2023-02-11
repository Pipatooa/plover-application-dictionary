import threading
import time

from plover.engine import StenoEngine
from plover_application_dictionary.window_tracker import WindowTracker

THREAD_INTERVAL = 0.25


class ApplicationDictionaryExtension:
    def __init__(self, engine: StenoEngine) -> None:
        self._engine = engine
        self._t = threading.Thread(target=ApplicationDictionaryExtension.thread_work)
        self._t.start()

    def start(self) -> None:
        pass

    def stop(self) -> None:
        pass

    @staticmethod
    def thread_work() -> None:
        while True:
            WindowTracker.check_active_window()
            time.sleep(THREAD_INTERVAL)
