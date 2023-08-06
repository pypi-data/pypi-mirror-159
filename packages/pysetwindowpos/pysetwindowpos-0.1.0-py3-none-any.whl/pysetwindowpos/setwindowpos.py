from ctypes import *
import ctypes
from ctypes.wintypes import HWND, UINT

# To publish:
# TODO: only export what I actually want to?
# TODO: package for publishing
# TODO: publish on pypi


def set_window_topmost(hwnd):
    HWND_TOPMOST = -1
    SWP_NOSIZE = 0x0001
    SWP_NOMOVE = 0x0002
    # TODO: `ctypes.windll.user32` - why didn't that work? (and then how to set use_last_error?)
    user32 = WinDLL("user32", use_last_error=True)
    SetWindowPos = user32.SetWindowPos
    SetWindowPos.argtypes = [HWND, HWND, c_int, c_int, c_int, c_int, UINT]
    SetWindowPos.restype = c_int
    SetWindowPos.errcheck = _errcheck

    SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, SWP_NOSIZE | SWP_NOMOVE)


def _errcheck(result, func, args):
    if not result:
        raise WinError(get_last_error())


if __name__ == "__main__":

    import tkinter as tk

    root = tk.Tk()
    root.title("pysetwindowpos")
    root.geometry("200x100")
    a = tk.Label(root, text="I'm on top of the world!")
    a.pack()

    def position_window():
        hwnd_frame = int(root.frame(), 16)  # cf. than winfo_id ?
        print("hwnd_frame=", hwnd_frame)
        set_window_topmost(hwnd_frame)

    # Need to wait until main loop starts (i.e., window actually displayed)
    # to find/control window. Doesn't work with `0` as first parameter.
    root.after(1, position_window)

    root.mainloop()
