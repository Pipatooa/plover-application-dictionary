from plover.formatting import _Action, _Context

from plover_application_dictionary import WindowTracker


def meta(ctx: _Context, cmdline: str) -> _Action:
    action = ctx.new_action()
    action.text = ":".join(map(get_property, cmdline.split(":")))
    return action


def get_property(prop: str) -> str:
    if prop == "app":
        return WindowTracker.current_app
    if prop == "class":
        return WindowTracker.current_class
    if prop == "title":
        return WindowTracker.current_title
    if prop == "":
        raise KeyError("No application name property specified")
    raise KeyError(f"Unknown window property {prop}")
