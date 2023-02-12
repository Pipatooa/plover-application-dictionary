try:
    from pywinctl import getActiveWindow
except ImportError:
    import sys
    import plover_application_dictionary.fake_tk as tkinter
    sys.modules["tkinter"] = tkinter
    from pywinctl import getActiveWindow


class WindowTracker:
    current_app = ""
    current_class = ""
    current_title = ""

    @staticmethod
    def check_active_window() -> None:
        try:
            window = getActiveWindow()
            WindowTracker.current_title = window.title
        except:
            WindowTracker.current_title = ""

        try:
            WindowTracker.current_app = window.getAppName()
        except:
            WindowTracker.current_app = ""

        try:
            WindowTracker.current_class = window.getHandle().get_wm_class()[0]
        except:
            WindowTracker.current_class = ""
