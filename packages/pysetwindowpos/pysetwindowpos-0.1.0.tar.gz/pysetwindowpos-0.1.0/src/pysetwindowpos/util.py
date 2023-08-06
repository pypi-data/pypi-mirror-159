from ctypes import *
import ctypes
from ctypes import WinDLL
from ctypes.wintypes import *

EnumWindows = ctypes.windll.user32.EnumWindows
EnumWindowsProc = ctypes.WINFUNCTYPE(
    # What was (wrongly?) in the SO post: https://stackoverflow.com/questions/14653168/get-hwnd-of-each-window
    # ctypes.c_bool, ctypes.POINTER(ctypes.c_int), ctypes.POINTER(ctypes.c_int)
    ctypes.c_bool,
    HWND,
    ctypes.POINTER(ctypes.c_int),
)
GetWindowText = ctypes.windll.user32.GetWindowTextW
GetWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
IsWindowVisible = ctypes.windll.user32.IsWindowVisible


def _find_hwnd(title):
    """Find HWND by title. Alternate way to get a window handle."""
    windows = []

    def foreach_window(hwnd, lParam):
        if IsWindowVisible(hwnd):
            length = GetWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            GetWindowText(hwnd, buff, length + 1)
            title = buff.value
            if title:
                windows.append((hwnd, title))
        return True

    EnumWindows(EnumWindowsProc(foreach_window), 0)

    found = None
    for w in windows:
        if w[1] == title:
            found = w
    return found[0]


def _find_hwnd_test_callback():
    print("Looking for the window...")
    hwnd = _find_hwnd("pysetwindowpos")
    print("found hwnd=", hwnd)
    print("frame()=", _find_hwnd_test_root.frame())
    print("int(frame(), 16)=", int(_find_hwnd_test_root.frame(), 16))
    print("winfo_id()=", _find_hwnd_test_root.winfo_id())


def _find_hwnd_test():

    import tkinter as tk

    global _find_hwnd_test_root
    _find_hwnd_test_root = root = tk.Tk()
    root.title("pysetwindowpos")
    root.geometry("200x100")
    a = tk.Label(root, text="I'm on top of the world!")
    a.pack()

    # Need to wait until main loop starts (i.e., window actually displayed)
    # to find window. Doesn't work with `0` as first parameter.
    root.after(1, _find_hwnd_test_callback)

    print("Starting tkinter main loop...")
    root.mainloop()


if __name__ == "__main__":
    _find_hwnd_test()
