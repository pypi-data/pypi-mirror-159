/*
    WinAPY - Windows API wrapper in C developed for Python.
    Copyright (c) 2022 Itzsten
*/

#include "utils.h"

#pragma comment(lib, "User32.lib")
#pragma comment(lib, "Advapi32.lib")

#define WGWLP_USERDATA       (-21)

typedef struct tagPYENUMCHILDWINDOWPARAMS {
    PyObject* func;
    PyObject* lParam;
} PYENUMCHILDWINDOWPARAMS, * PPYENUMCHILDWINDOWPARAMS, * LPPYENUMCHILDWINDOWPARAMS;

static PyObject* PyGetDC(PyObject* self, PyObject* args) {
    //@description@ Retrieves a handle to a device context (DC) for the client area of a specified window or for the entire screen. You can use the returned handle in subsequent GDI functions to draw in the DC.@@HDC
    //@args@ hwnd|int|Handle to the window to retrieve the Device Context from or None
    LONG hWnd;
    PyObject* pyhWnd;

    if (!PyArg_ParseTuple(args, "O", &pyhWnd)) {
        return NULL;
    }
    if (pyhWnd == Py_None) {
        hWnd = NULL;
    }
    else {
        hWnd = PyLong_AsLong(pyhWnd);
    }

    HDC res = GetDC(hWnd ? (HANDLE)&hWnd : 0);

    if (RaiseExceptionCheck(res)) return NULL;

    return Py_BuildValue("l", (LONG)res);
}
static PyObject* PyGetSystemMetrics(PyObject* self, PyObject* args) {
    //@description@ Retrieves the specified system metric or system configuration setting.@@int
    //@args@ int|nIndex|The system metric or configuration setting to be retrieved.
    INT metric;
    if (!PyArg_ParseTuple(args, "i", &metric)) {
        return NULL;
    }
    INT a = GetSystemMetrics(metric);
    if (RaiseExceptionCheck(a)) { return NULL; }
    return Py_BuildValue("i", a);
}
static PyObject* PyGetDesktopWindow(PyObject* self, PyObject* args) {
    //@description@ Retrieves a handle to the desktop window.@@HWND
    //@args@ None
    LONG window = (LONG)GetDesktopWindow();
    if (RaiseExceptionCheck(window)) { return NULL; }
    return Py_BuildValue("l", window);
}
static PyObject* PyGetLastError(PyObject* self, PyObject* args) {
    //@description@ Retrieves the last error code caused by a WinAPY function.@@int
    //@args@ None
    return Py_BuildValue("i", GetLastError());
}
static PyObject* Pyrand(PyObject* self, PyObject* args) {
    //@description@ Generates a random integer.@@int
    //@args@ None
    return Py_BuildValue("i", rand());
}
static PyObject* PySleep(PyObject* self, PyObject* args) {
    //@description@ Sleeps for the specified duration, in milliseconds.@@NoneType
    //@args@ dwMilliseconds|int|The amount to wait in milliseconds
    LONG amn;
    if (!PyArg_ParseTuple(args, "l", &amn)) return NULL;
    Sleep(amn);
    return Py_BuildValue("O", Py_None);;
}
static PyObject* PyRedrawWindow(PyObject* self, PyObject* args) {
    //@description@ Redraws a portion or the entire specified window.@@bool
    //@args@ hwnd|HWND|Handle to a window, or None@@rect|tuple|Rectangle with coordinates to be redrawn (x1, y1, x2, y2), or None@@region|HRGN|Handle to a region to be redrawn, or None@@flags|int|[optional] Redrawing flags. Default are RDW_ALLCHILDREN, RDW_ERASE and RDW_INVALIDATE
    INT flags = RDW_ALLCHILDREN | RDW_ERASE | RDW_INVALIDATE;

    HWND hwnd;
    HRGN hrgn;

    PyObject* obRect = Py_None;
    PyObject* obRgn = Py_None;
    PyObject* obWnd = Py_None;
    if (!PyArg_ParseTuple(args, "OOO|i", &obWnd, &obRect, &obRgn, &flags)) return NULL;

    RECT rect;
    RECT* pRect;
    if (obRect == Py_None) {
        pRect = NULL;
    }
    else {
        if (!PyArg_ParseTuple(args, "O(iiii)O|i", &obWnd, &rect.left, &rect.top, &rect.right, &rect.bottom, &obRgn, &flags))
            return NULL;
        pRect = &rect;
    }
    if (obWnd == Py_None) {
        hwnd = NULL;
    }
    else {
        hwnd = PyLong_AsLong(obWnd);
    }
    if (obRgn == Py_None) {
        hrgn = NULL;
    }
    else {
        hrgn = PyLong_AsLong(obRgn);
    }

    return Py_BuildValue("O", PyBool_FromLong(RedrawWindow(hwnd, pRect, hrgn, flags)));
}
static PyObject* PyInvalidateRect(PyObject* self, PyObject* args) {
    //@description@ Returns a handle to one of the stock pens, brushes, fonts, or palettes.@@bool
    //@args@ hwnd|HWND|Handle to a window, or None@@rect|tuple|Rectangle with coordinates to be redrawn (x1, y1, x2, y2), or None@@erase|bool|Whether the background within the update region is to be erased when the update region is processed.
    HWND hwnd;
    BOOL erase;

    PyObject* obRect = Py_None;
    PyObject* obWnd = Py_None;
    PyObject* obBool;

    if (!PyArg_ParseTuple(args, "OOO", &obWnd, &obRect, &obBool)) return NULL;

    erase = PyObject_IsTrue(obBool);

    RECT rect;
    RECT* pRect;
    if (obRect == Py_None) {
        pRect = NULL;
    }
    else {
        if (!PyArg_ParseTuple(args, "O(iiii)O", &obWnd, &rect.left, &rect.top, &rect.right, &rect.bottom, &obBool))
            return NULL;
        pRect = &rect;
    }
    if (obWnd == Py_None) {
        hwnd = NULL;
    }
    else {
        hwnd = PyLong_AsLong(obWnd);
    }

    return Py_BuildValue("O", PyBool_FromLong(InvalidateRect(hwnd, pRect, erase)));
}
static PyObject* PyGetClientRect(PyObject* self, PyObject* args) {
    //@description@ Returns the coordinates of a window's client area as a tuple of four integers.@@tuple
    //@args@ hdc|HDC|Handle to a device context
    LONG wnd;
    if (!PyArg_ParseTuple(args, "l", &wnd)) return NULL;
    RECT rect;
    BOOL res = GetClientRect(wnd, &rect);
    if (!res) {
        PyErr_SetFromWindowsErr(87);
        return NULL;
    }
    return Py_BuildValue("(iiii)", rect.top, rect.left, rect.right, rect.bottom);
}
static PyObject* PyWindowFromDC(PyObject* self, PyObject* args) {
    //@description@ Returns a handle to the window associated with the specified display device context.@@HWND
    //@args@ hdc|HDC|Handle to a device context
    LONG wnd;
    if (!PyArg_ParseTuple(args, "l", &wnd)) return NULL;
    HWND res = WindowFromDC(wnd);
    if (!res) {
        PyErr_SetFromWindowsErr(87);
        return NULL;
    }
    return Py_BuildValue("l", res);
}
BOOL WINAPI PyEnumChildWindowsProcHandler(HWND hwnd, LPARAM lparam) {
    LPPYENUMCHILDWINDOWPARAMS pParams = (LPPYENUMCHILDWINDOWPARAMS)lparam;
    if (PyObject_CallFunction(pParams->func, "lO", (LONG)hwnd, pParams->lParam) == NULL) {
        return FALSE;
    }

    return TRUE;
}
static PyObject* PyEnumChildWindows(PyObject* self, PyObject* args) {
    //@description@ Enumerates the child windows that belong to the specified parent window by passing the handle to each child window, in turn, to the specified callback function. The callback function should look like this; ``def callback(hwnd, lparam)``.@@NoneType
    //@args@ hwnd|HWND|Handle to a window to enumerate, or None@@callback|FunctionType|Callback function to be called for every child window found with two arguments commonly named ``hWnd, lParam``.@@lParam|AnyType|[optional] This argument will be passed as the lParam value for the callback function, default is set to None.
    PyObject* func, * hwnd;
    PyObject* lParam = Py_None;
    HWND aHwnd;

    if (!PyArg_ParseTuple(args, "OO|O", &hwnd, &func, &lParam)) return NULL;
    if (!PyCallable_Check(func)) {
        PyErr_SetString(PyExc_TypeError, "argument 2: must be a callable function");
        return NULL;
    }

    if (hwnd == Py_None) {
        aHwnd = NULL;
    }
    else {
        aHwnd = PyLong_AsLong(hwnd);
    }

    // allocate memory in heap to prevent corruption when larger data is transfered
    HANDLE hHeap = GetProcessHeap();
    LPPYENUMCHILDWINDOWPARAMS params = (LPPYENUMCHILDWINDOWPARAMS)HeapAlloc(hHeap, 0, sizeof(PYENUMCHILDWINDOWPARAMS));

    params->func = func;
    params->lParam = lParam;

    EnumChildWindows(aHwnd, PyEnumChildWindowsProcHandler, (LPARAM)params);

    HeapFree(hHeap, 0, params);
    return Py_None;
}
static PyObject* PyGetWindowTextW(PyObject* self, PyObject* args) {
    //@description@ Returns the specified windows' title bar text, as an UTF-16 string.@@str
    //@args@ hwnd|HWND|Handle to a window
    LONG hwnd;
    if (!PyArg_ParseTuple(args, "l", &hwnd)) return NULL;

    INT len = GetWindowTextLengthW(hwnd) + 1;
    if (RaiseExceptionCheck(len - 1)) return NULL;

    WCHAR out[256];

    BOOL res = GetWindowTextW(hwnd, out, len);

    if (RaiseExceptionCheck(res)) {
        return NULL;
    }
    return Py_BuildValue("u", out);
}
static PyObject* PyGetWindowTextA(PyObject* self, PyObject* args) {
    //@description@ Returns the specified windows' title bar text, as an ASCII string.@@str
    //@args@ hwnd|HWND|Handle to a window
    LONG hwnd;
    if (!PyArg_ParseTuple(args, "l", &hwnd)) return NULL;

    INT len = GetWindowTextLengthA(hwnd) + 1;
    if (RaiseExceptionCheck(len - 1)) return NULL;

    CHAR out[256];

    BOOL res = GetWindowTextA(hwnd, out, len);

    if (RaiseExceptionCheck(res)) {
        return NULL;
    }
    return Py_BuildValue("s", out);
}
static PyObject* PyGetWindowTextLengthA(PyObject* self, PyObject* args) {
    //@description@ Returns the length of the specified windows' title bar text, measured from an ASCII string.@@int
    //@args@ hwnd|HWND|Handle to a window
    LONG hwnd;
    if (!PyArg_ParseTuple(args, "l", &hwnd)) return NULL;

    INT res = GetWindowTextLengthA(hwnd);

    if (RaiseExceptionCheck(res)) {
        return NULL;
    }
    return Py_BuildValue("i", res);
}
static PyObject* PyGetWindowTextLengthW(PyObject* self, PyObject* args) {
    //@description@ Returns the length of the specified windows' title bar text, measured from an UTF-16 string.@@int
    //@args@ hwnd|HWND|Handle to a window
    LONG hwnd;
    if (!PyArg_ParseTuple(args, "l", &hwnd)) return NULL;

    INT res = GetWindowTextLengthW(hwnd);

    if (RaiseExceptionCheck(res)) {
        return NULL;
    }
    return Py_BuildValue("i", res);
}
static PyObject* PyGetWindowRect(PyObject* self, PyObject* args) {
    //@description@ Returns the dimensions of the bounding rectangle of the specified window.@@(int, int, int, int)
    //@args@ hwnd|HWND|Handle to a window
    LONG hwnd;
    if (!PyArg_ParseTuple(args, "l", &hwnd)) return NULL;
    RECT rect;

    BOOL res = GetWindowRect(hwnd, &rect);

    if (RaiseExceptionCheck(res)) {
        return NULL;
    }
    return Py_BuildValue("(iiii)", rect.left, rect.top, rect.right, rect.bottom);
}
static PyObject* PyGetWindowPlacement(PyObject* self, PyObject* args) {
    //@description@ Returns the show state and the restored, minimized, and maximized positions of the specified window.@@(int, int, (int, int), (int, int), (int, int, int, int))
    //@args@ hwnd|HWND|Handle to a window
    LONG hwnd;
    if (!PyArg_ParseTuple(args, "l", &hwnd)) return NULL;
    WINDOWPLACEMENT wp;
    wp.length = sizeof(WINDOWPLACEMENT);
    if (RaiseExceptionCheck(GetWindowPlacement(hwnd, &wp))) return NULL;
    return Py_BuildValue("(IIOOO)", wp.flags, wp.showCmd,
        Py_BuildValue("(ii)", wp.ptMinPosition.x, wp.ptMinPosition.y),
        Py_BuildValue("(ii)", wp.ptMaxPosition.x, wp.ptMaxPosition.y),
        Py_BuildValue("(iiii)", wp.rcNormalPosition.left, wp.rcNormalPosition.top,
            wp.rcNormalPosition.right, wp.rcNormalPosition.bottom)
    );
}
static PyObject* PyWindowFromPoint(PyObject* self, PyObject* args) {
    //@description@ Returns a handle to the window that contains the specified point. Returns a handle to the window if it exists at the specified point, otherwise None.@@HWND
    //@args@ point|tuple|The point to be checked, as a tuple of two integers (x, y).
    INT x, y;
    if (!PyArg_ParseTuple(args, "(ii)", &x, &y)) return NULL;

    POINT p;
    p.x = x;
    p.y = y;
    HWND res = WindowFromPoint(p);
    if (res == NULL) {
        return Py_None;
    }
    return Py_BuildValue("l", (LONG)res);
}
static PyObject* PyWindowFromPhysicalPoint(PyObject* self, PyObject* args) {
    //@description@ Returns a handle to the window that contains the specified physical point.@@HWND
    //@args@ point|tuple|The point to be checked, as a tuple of two integers (x, y).
    INT x, y;
    if (!PyArg_ParseTuple(args, "(ii)", &x, &y)) return NULL;

    POINT p;
    p.x = x;
    p.y = y;
    HWND res = WindowFromPhysicalPoint(p);
    if (res == NULL) {
        return Py_None;
    }
    return Py_BuildValue("l", (LONG)res);
}
static PyObject* PySwitchToThisWindow(PyObject* self, PyObject* args) {
    //@description@ [This function is not made for general use. It can be unavailable in future versions of Windows.] Switches focus to the specified window and brings it to the foreground.@@NoneType
    //@args@ hwnd|HWND|Handle to a window@@bAltTab|bool|Specifies whether the window is being switched to using the Alt/Ctl+Tab key sequence or not.
    LONG wnd;
    PyObject* bUnk;
    if (!PyArg_ParseTuple(args, "lO", &wnd, &bUnk)) return NULL;
    if (!PyBool_Check(bUnk)) {
        PyErr_SetString(PyExc_TypeError, "argument 2: excepted bool");
        return NULL;
    }
    SwitchToThisWindow(wnd, PyObject_IsTrue(bUnk));
    return Py_None;
}
static PyObject* PyShowWindow(PyObject* self, PyObject* args) {
    //@description@ Sets the specified window's show state.@@bool
    //@args@ hwnd|HWND|Handle to a window@@nCmdShow|int|The new show state.
    LONG wnd;
    INT nShow;
    if (!PyArg_ParseTuple(args, "li", &wnd, &nShow)) return NULL;

    return PyBool_FromLong(ShowWindow(wnd, nShow));
}
static PyObject* PyReleaseDC(PyObject* self, PyObject* args) {
    //@description@ Releases a device context, making it available to other applications.@@bool
    //@args@ hwnd|HWND|Handle to a window to be released@@hdc|HDC|A handle to a device context to be released
    LONG wnd, hdc;
    if (!PyArg_ParseTuple(args, "ll", &wnd, &hdc)) return NULL;
    return PyBool_FromLong(ReleaseDC(wnd, hdc));
}
static PyObject* PyGetCursorPos(PyObject* self, PyObject* args) {
    //@description@ Returns the position of the mouse cursor, in a tuple of screen coordinates (x, y).@@bool
    //@args@ None
    POINT p;
    if (RaiseExceptionCheck(GetCursorPos(&p))) return NULL;
    return Py_BuildValue("(ii)", p.x, p.y);
}
static PyObject* PySetCursorPos(PyObject* self, PyObject* args) {
    //@description@ Moves the cursor to the specified screen coordinates.@@bool
    //@args@ x|int|The new X-coordinate of the cursor@@y|int|The new Y-coordinate of the cursor
    INT x, y;
    if (!PyArg_ParseTuple(args, "ii", &x, &y)) return NULL;
    if (RaiseExceptionCheck(SetCursorPos(x, y))) return NULL;
    return Py_True;
}
static PyObject* PyLoadIconA(PyObject* self, PyObject* args) {
    //@description@ Loads the specified icon resource from the executable (.exe) file associated with an application instance or a predefined icon.@@HICON
    //@args@ hInstance|int|Handle to the instance whose executable file contains the icon to be loaded, or None.@@IconName|int|The icon to be loaded, parsed as an ASCII string from an integer
    PyObject* hinstance;
    INT icon;
    HINSTANCE hinst = NULL;
    if (!PyArg_ParseTuple(args, "Oi", &hinstance, &icon)) return NULL;
    if (hinstance != Py_None) hinst = PyLong_AsLong(hinstance);

    HICON iconic = LoadIconA(hinst, MAKEINTRESOURCEA(icon));
    if (RaiseExceptionCheck(iconic == NULL)) return NULL;
    return Py_BuildValue("l", iconic);
}
static PyObject* PyLoadIconW(PyObject* self, PyObject* args) {
    //@description@ Loads the specified icon resource from the executable (.exe) file associated with an application instance or a predefined icon.@@HICON
    //@args@ hInstance|int|Handle to the instance whose executable file contains the icon to be loaded, or None.@@IconName|int|The icon to be loaded, parsed as an UTF-16 string from an integer
    PyObject* hinstance;
    INT icon;
    HINSTANCE hinst = NULL;
    if (!PyArg_ParseTuple(args, "Oi", &hinstance, &icon)) return NULL;
    if (hinstance != Py_None) hinst = PyLong_AsLong(hinstance);

    HICON iconic = LoadIconW(hinst, MAKEINTRESOURCEW(icon));
    if (RaiseExceptionCheck(iconic == NULL)) return NULL;
    return Py_BuildValue("l", iconic);
}
static PyObject* PyDrawIcon(PyObject* self, PyObject* args) {
    //@description@ Draws an icon or cursor into the specified device context.@@bool
    //@args@ hdc|HDC|Handle to a device context@@x|int|The X-position to draw the icon at@@y|int|The Y-position to draw the icon at@@icon|HICON|The icon to be drawn
    LONG hdc, icon;
    INT x, y;
    if (!PyArg_ParseTuple(args, "liil", &hdc, &x, &y, &icon)) return NULL;
    if (RaiseExceptionCheck(DrawIcon(hdc, x, y, icon))) return NULL;
    return Py_True;
}
static PyObject* PyDrawIconEx(PyObject* self, PyObject* args) {
    //@description@ Draws an icon or cursor into the specified device context performing the specified raster operations, and stretching or compressing the icon or cursor as specified.@@bool
    //@args@ hdc|HDC|Handle to a device context@@x|int|The X-position to draw the icon at@@y|int|The Y-position to draw the icon at@@icon|HICON|The icon to be drawn@@width|int|The logical width of the icon or cursor.@@height|int|The logical height of the icon or cursor.@@frame|int|The index of the frame to draw, if hIcon identifies an animated cursor. This parameter is ignored if the icon argument does not identify an animated cursor.@@brush|HBRUSH|A handle to a brush that the system uses for flicker-free drawing, or None.@@diFlags|int|Additional flags
    LONG hdc, icon;
    PyObject* obBrush;
    HBRUSH brush = NULL;
    INT x, y, w, h;
    UINT istepIfAniCur, diFlags;
    if (!PyArg_ParseTuple(args, "liiliiIOI", &hdc, &x, &y, &icon, &w, &h, &istepIfAniCur, &obBrush, &diFlags)) return NULL;
    if (obBrush != Py_None)
        brush = PyLong_AsLong(obBrush);
    BOOL res = DrawIconEx(hdc, x, y, icon, w, h, istepIfAniCur, brush, diFlags);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_True;
}
static PyObject* PyLoadImageA(PyObject* self, PyObject* args) {
    //@description@ Loads an icon, cursor, animated cursor, or bitmap.@@HANDLE
    //@args@ hInstance|HINSTANCE|A handle to the module of either a DLL or executable (.exe) that contains the image to be loaded, or None.@@name|int/str|The image to be loaded.@@type|int|The type of image to be loaded.@@width|int|The width, in pixels, of the icon or cursor.@@height|int|The height, in pixels, of the icon or cursor.@@fLoad|int|Any of the following values; ``LR_CREATEDIBSECTION, LR_DEFAULTCOLOR, LR_DEFAULTSIZE, LR_LOADFROMFILE, LR_LOADMAP3DCOLORS, LR_LOADTRANSPARENT, LR_MONOCHROME, LR_SHARED or LR_VGACOLOR``
    PyObject* obHinstance;
    PyObject* obIco;
    LPSTR ico;
    UINT type;
    INT cx, cy;
    UINT fuLoad;
    HINSTANCE inst = NULL;

    if (!PyArg_ParseTuple(args, "OOIiiI", &obHinstance, &obIco, &type, &cx, &cy, &fuLoad)) return NULL;

    if (PyLong_Check(obIco)) {
        ico = MAKEINTRESOURCEA(PyLong_AsLong(obIco));
    }
    else {
        if (!PyArg_ParseTuple(args, "OsIiiI", &obHinstance, &ico, &type, &cx, &cy, &fuLoad)) return NULL;
        ico = MAKEINTRESOURCEA(ico);
    }

    if (obHinstance != Py_None)
        inst = PyLong_AsLong(obHinstance);

    HANDLE res = LoadImageA(inst, ico, type, cx, cy, fuLoad);

    if (RaiseExceptionCheck(res == NULL)) return NULL;

    return Py_BuildValue("l", (LONG)res);
}
static PyObject* PyLoadImageW(PyObject* self, PyObject* args) {
    //@description@ Loads an icon, cursor, animated cursor, or bitmap.@@HANDLE
    //@args@ hInstance|HINSTANCE|A handle to the module of either a DLL or executable (.exe) that contains the image to be loaded, or None.@@name|int/str|The image to be loaded.@@type|int|The type of image to be loaded.@@width|int|The width, in pixels, of the icon or cursor.@@height|int|The height, in pixels, of the icon or cursor.@@fLoad|int|Any of the following values; ``LR_CREATEDIBSECTION, LR_DEFAULTCOLOR, LR_DEFAULTSIZE, LR_LOADFROMFILE, LR_LOADMAP3DCOLORS, LR_LOADTRANSPARENT, LR_MONOCHROME, LR_SHARED or LR_VGACOLOR``
    PyObject* obHinstance;
    PyObject* obIco;
    LPWSTR ico;
    UINT type;
    INT cx, cy;
    UINT fuLoad;
    HINSTANCE inst = NULL;

    if (!PyArg_ParseTuple(args, "OOIiiI", &obHinstance, &obIco, &type, &cx, &cy, &fuLoad)) return NULL;

    if (PyLong_Check(obIco)) {
        ico = MAKEINTRESOURCEW(PyLong_AsLong(obIco));
    }
    else {
        if (!PyArg_ParseTuple(args, "OuIiiI", &obHinstance, &ico, &type, &cx, &cy, &fuLoad)) return NULL;
        ico = MAKEINTRESOURCEW(ico);
    }

    if (obHinstance != Py_None)
        inst = PyLong_AsLong(obHinstance);

    HANDLE res = LoadImageW(inst, ico, type, cx, cy, fuLoad);

    if (RaiseExceptionCheck(res == NULL)) return NULL;

    return Py_BuildValue("l", (LONG)res);
}
static PyObject* PyLoadCursorFromFileA(PyObject* self, PyObject* args) {
    //@description@ Creates a cursor based on data contained in a file.@@HCURSOR
    //@args@ fName|str|The source of the file data to be used to create the cursor. The data in the file must be in either .CUR or .ANI format.
    LPCSTR str;
    if (!PyArg_ParseTuple(args, "s", &str)) return NULL;
    HCURSOR cur = LoadCursorFromFileA(str);
    if (RaiseExceptionCheck(cur == NULL)) return NULL;
    return Py_BuildValue("l", cur);
}
static PyObject* PyLoadCursorFromFileW(PyObject* self, PyObject* args) {
    //@description@ Creates a cursor based on data contained in a file.@@HCURSOR
    //@args@ fName|str|The source of the file data to be used to create the cursor. The data in the file must be in either .CUR or .ANI format.
    LPCWSTR str;
    if (!PyArg_ParseTuple(args, "u", &str)) return NULL;
    HCURSOR cur = LoadCursorFromFileW(str);
    if (RaiseExceptionCheck(cur == NULL)) return NULL;
    return Py_BuildValue("l", cur);
}
static PyObject* PyLoadCursorA(PyObject* self, PyObject* args) {
    //@description@ Loads the specified cursor resource from the executable (.EXE) file associated with an application instance.@@HCURSOR
    //@args@ hInstance|HINSTANCE|A handle to an instance of the module whose executable file contains the cursor to be loaded, or None.@@cursor|int|The name of the cursor resource to be loaded.
    PyObject* obHinst;
    HINSTANCE hinstance = NULL;
    LONG cursor;

    if (!PyArg_ParseTuple(args, "Ol", &obHinst, &cursor)) return NULL;

    if (obHinst != Py_None)
        hinstance = PyLong_AsLong(obHinst);

    HCURSOR cur = LoadCursorA(hinstance, MAKEINTRESOURCEA(cursor));
    if (RaiseExceptionCheck(cur == NULL)) return NULL;
    return Py_BuildValue("l", cur);
}
static PyObject* PyLoadCursorW(PyObject* self, PyObject* args) {
    //@description@ Loads the specified cursor resource from the executable (.EXE) file associated with an application instance.@@HCURSOR
    //@args@ hInstance|HINSTANCE|A handle to an instance of the module whose executable file contains the cursor to be loaded, or None.@@cursor|int|The name of the cursor resource to be loaded.
    PyObject* obHinst;
    HINSTANCE hinstance = NULL;
    LONG cursor;

    if (!PyArg_ParseTuple(args, "Ol", &obHinst, &cursor)) return NULL;

    if (obHinst != Py_None)
        hinstance = PyLong_AsLong(obHinst);

    HCURSOR cur = LoadCursorW(hinstance, MAKEINTRESOURCEW(cursor));
    if (RaiseExceptionCheck(cur == NULL)) return NULL;
    return Py_BuildValue("l", cur);
}
static PyObject* PyGetCursorInfo(PyObject* self, PyObject* args) {
    //@description@ Returns information about the global cursor.@@(int, HCURSOR, (int, int))
    //@args@ None
    CURSORINFO leFisheAuChocolat;
    leFisheAuChocolat.cbSize = sizeof(CURSORINFO);
    GetCursorInfo(&leFisheAuChocolat);
    return Py_BuildValue("(klO)", leFisheAuChocolat.flags, leFisheAuChocolat.hCursor,
        Py_BuildValue("(ii)", leFisheAuChocolat.ptScreenPos.x, leFisheAuChocolat.ptScreenPos.y)
    );
}
static PyObject* PyMessageBoxA(PyObject* self, PyObject* args) {
    //@description@ Displays a modal dialog box that contains a system icon, a set of buttons, and a brief application-specific message, such as status or error information. The message box returns an integer value that indicates which button the user clicked.@@int
    //@args@ hWnd|HWND|The parent window of the Message Box, or None.@@msg|str|The message to be displayed, as an ASCII string.@@title|str|The dialog box title, as an ASCII string.@@type|int|The contents and behavior of the dialog box.
    CHAR* title, * description;
    UINT uType;
    PyObject* obHwnd;

    if (!PyArg_ParseTuple(args, "OssI", &obHwnd, &description, &title, &uType)) return NULL;

    HWND hwnd = obHwnd == Py_None ? NULL : PyLong_AsLong(obHwnd);
    INT res = MessageBoxA(hwnd, title, description, uType);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_BuildValue("i", res);
}
static PyObject* PyMessageBoxW(PyObject* self, PyObject* args) {
    //@description@ Displays a modal dialog box that contains a system icon, a set of buttons, and a brief application-specific message, such as status or error information. The message box returns an integer value that indicates which button the user clicked.@@int
    //@args@ hWnd|HWND|The parent window of the Message Box, or None.@@msg|str|The message to be displayed, as an UTF-16 string.@@title|str|The dialog box title, as an UTF-16 string.@@type|int|The contents and behavior of the dialog box.
    WCHAR* title, * description;
    UINT uType;
    PyObject* obHwnd;

    if (!PyArg_ParseTuple(args, "OuuI", &obHwnd, &description, &title, &uType)) return NULL;

    HWND hwnd = obHwnd == Py_None ? NULL : PyLong_AsLong(obHwnd);
    INT res = MessageBoxW(hwnd, title, description, uType);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_BuildValue("i", res);
}
static PyObject* PyMessageBeep(PyObject* self, PyObject* args) {
    //@description@ Plays a waveform sound. The waveform sound for each sound type is identified by an entry in the registry.@@int
    //@args@ sound|int|The sound to be played. The sounds are set by the user through the Sound control panel application, and then stored in the registry. Any of the Message Box icon values or 0xFFFFFFFF.
    UINT uType;

    if (!PyArg_ParseTuple(args, "I", &uType)) return NULL;

    BOOL res = MessageBeep(uType);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_True;
}
static PyObject* PyBeep(PyObject* self, PyObject* args) {
    //@description@ Generates simple tones on the speaker. The function is synchronous; it performs an alertable wait and does not return control to its caller until the sound finishes.@@bool
    //@args@ freq|int|The frequency of the sound, in hertz. This parameter must be in the range 37 through 32,767@@duration|int|The duration of the sound, in milliseconds.
    DWORD dwFreq, dwDur;

    if (!PyArg_ParseTuple(args, "kk", &dwFreq, &dwDur)) return NULL;

    BOOL res = Beep(dwFreq, dwDur);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_True;
}
static PyObject* PyGetTopWindow(PyObject* self, PyObject* args) {
    //@description@ Examines the Z order of the child windows associated with the specified parent window and retrieves a handle to the child window at the top of the Z order.@@HWND
    //@args@ hWnd|HWND|A handle to the parent window whose child windows are to be examined, or None.
    PyObject* obWnd = Py_None;

    if (!PyArg_ParseTuple(args, "|O", &obWnd)) return NULL;

    HWND hwnd = obWnd == Py_None ? NULL : PyLong_AsLong(obWnd);

    HWND res = GetTopWindow(hwnd);
    if (RaiseExceptionCheck(res == NULL)) return NULL;
    return Py_True;
}
static PyObject* PyExitWindowsEx(PyObject* self, PyObject* args) {
    //@description@ Logs off the interactive user, shuts down the system, or shuts down and restarts the system. It sends the WM_QUERYENDSESSION message to all applications to determine if they can be terminated.@@bool
    //@args@ flags|int|The shutdown type.@@reason|int|The reason for initiating the shutdown.
    UINT flags;
    DWORD reason;
    if (!PyArg_ParseTuple(args, "Ik", &flags, &reason)) return NULL;
    BOOL res = ExitWindowsEx(flags, reason);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_True;
}
static PyObject* PyExitWindows(PyObject* self, PyObject* args) {
    //@description@ Calls the ExitWindowsEx function to log off the interactive user.@@bool
    //@args@ None
    BOOL res = ExitWindows(0, 0);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_True;
}
static PyObject* PyInitiateSystemShutdownA(PyObject* self, PyObject* args) {
    //@description@ Initiates a shutdown and optional restart of the specified computer.@@bool
    //@args@ machine|str|The network name of the computer to be shut down, or None to shut down the current machine.@@message|str|The message to display before shutdown, or None.@@displayTime|int|The length of time that the shutdown dialog box should be displayed, in seconds.@@bForceAppsClosed|bool|Whether applications should be force closed or not.@@bRebootAfterShutdown|bool|Whether the machine should restart or not.
    PyObject* computer, * message;
    DWORD timeout;
    PyObject* forceClose, * reboot;
    LPSTR computerName, messageName;
    BOOL forceName, rebootName;

    if (!PyArg_ParseTuple(args, "OOkOO", &computer, &message, &timeout, &forceClose, &reboot)) return NULL;
    if (computer == Py_None) {
        computerName = NULL;
    }
    else {
        computerName = PyString_ToCharArr(computer);
    }
    if (message == Py_None) {
        messageName = NULL;
    }
    else {
        messageName = PyString_ToCharArr(message);
    }

    if (!PyBool_Check(forceClose)) {
        PyErr_SetString(PyExc_TypeError, "argument 4: excepted bool");
        return NULL;
    }
    if (!PyBool_Check(reboot)) {
        PyErr_SetString(PyExc_TypeError, "argument 5: excepted bool");
        return NULL;
    }
    forceName = PyObject_IsTrue(forceClose);
    rebootName = PyObject_IsTrue(reboot);

    BOOL res = InitiateSystemShutdownA(computerName, messageName, timeout, forceName, rebootName);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_True;
}
static PyObject* PyInitiateSystemShutdownW(PyObject* self, PyObject* args) {
    //@description@ Initiates a shutdown and optional restart of the specified computer.@@bool
    //@args@ machine|str|The network name of the computer to be shut down, or None to shut down the current machine.@@message|str|The message to display before shutdown, or None.@@displayTime|int|The length of time that the shutdown dialog box should be displayed, in seconds.@@bForceAppsClosed|bool|Whether applications should be force closed or not.@@bRebootAfterShutdown|bool|Whether the machine should restart or not.
    PyObject* computer, * message;
    DWORD timeout;
    PyObject* forceClose, * reboot;
    LPWSTR computerName, messageName;
    BOOL forceName, rebootName;

    if (!PyArg_ParseTuple(args, "OOkOO", &computer, &message, &timeout, &forceClose, &reboot)) return NULL;
    if (computer == Py_None) {
        computerName = NULL;
    }
    else {
        computerName = PyUnicode_AsWideCharString(computer, 1024);
    }
    if (message == Py_None) {
        messageName = NULL;
    }
    else {
        messageName = PyUnicode_AsWideCharString(message, 1024);
    }

    if (!PyBool_Check(forceClose)) {
        PyErr_SetString(PyExc_TypeError, "argument 4: excepted bool");
        return NULL;
    }
    if (!PyBool_Check(reboot)) {
        PyErr_SetString(PyExc_TypeError, "argument 5: excepted bool");
        return NULL;
    }
    forceName = PyObject_IsTrue(forceClose);
    rebootName = PyObject_IsTrue(reboot);

    BOOL res = InitiateSystemShutdownW(computerName, messageName, timeout, forceName, rebootName);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_True;
}
static PyObject* PyFillRect(PyObject* self, PyObject* args) {
    //@description@ Fills a rectangle by using the specified brush.@@HWND
    //@args@ hdc|HDC|Handle to a device context@@rect|tuple|Rectangle to be filled; tuple of 4 integers (x1, y1, x2, y2)@@hbr|HBRUSH|Brush to paint the rectangle with
    LONG wnd;
    LONG brush;
    INT x, y, dx, dy;
    if (!PyArg_ParseTuple(args, "l(iiii)l", &wnd, &x, &y, &dx, &dy, &brush)) return NULL;
    RECT r = { x, y, dx, dy };
    BOOL res = FillRect(wnd, &r, brush);
    if (!res) {
        PyErr_SetFromWindowsErr(87);
        return NULL;
    }
    return Py_BuildValue("O", PyBool_FromLong(res));
}

static PyObject* PyGetKeyboardLayout(PyObject* _, PyObject* args) {
    DWORD thread;
    if (!PyArg_ParseTuple(args, "k", &thread)) return NULL;
    HKL res = GetKeyboardLayout(thread);
    return Py_BuildValue("(lL)", LOWORD(res), HIWORD(res));
}

static PyObject* PyActivateKeyboardLayout(PyObject* _, PyObject* args) {
    INT hkl;
    UINT flags;
    if (!PyArg_ParseTuple(args, "iI", &hkl, &flags)) return NULL;
    HKL res = ActivateKeyboardLayout(hkl, flags);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_BuildValue("L", res);
}

static PyObject* PyBlockInput(PyObject* _, PyObject* args) {
    PyObject* b;
    if (!PyArg_ParseTuple(args, "O", &b)) return NULL;
    if (!PyBool_Check(b)) {
        PyErr_SetString(PyExc_TypeError, "argument 1: excepted bool object");
        return NULL;
    }
    BOOL bBlock = PyObject_IsTrue(b);
    BOOL res = BlockInput(bBlock);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_BuildValue("i", 0);
}

static PyObject* PyAbortSystemShutdownA(PyObject* _, PyObject* args) {
    PyObject* computer;
    CHAR* comp = NULL;
    if (!PyArg_ParseTuple(args, "O", &computer)) return NULL;
    if (computer != Py_None) comp = PyUnicode_AsUTF8(computer);
    if (RaiseExceptionCheck(AbortSystemShutdownA(comp))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyAbortSystemShutdownW(PyObject* _, PyObject* args) {
    PyObject* computer;
    WCHAR* comp = NULL;
    if (!PyArg_ParseTuple(args, "O", &computer)) return NULL;
    if (computer != Py_None) {
        Py_ssize_t sz = PyUnicode_GetLength(computer);
        comp = PyUnicode_AsWideCharString(computer, &sz);
    }
    if (RaiseExceptionCheck(AbortSystemShutdownW(comp))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyGetConsoleWindow(PyObject* _, PyObject* args) {
    HWND res = GetConsoleWindow();
    return Py_BuildValue("O", res == NULL ? Py_None : PyLong_FromLongLong(res));
}
static PyObject* PyGetCommandLineA(PyObject* _, PyObject* args) {
    return Py_BuildValue("s", GetCommandLineA());
}
static PyObject* PyGetCommandLineW(PyObject* _, PyObject* args) {
    return Py_BuildValue("u", GetCommandLineW());
}
static PyObject* PyCloseHandle(PyObject* _, PyObject* args) {
    HANDLE h;
    if (!PyArg_ParseTuple(args, "L", &h)) return NULL;
    if (RaiseExceptionCheck(CloseHandle(h))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyCopyFileA(PyObject* _, PyObject* args) {
    CHAR* currentFile;
    CHAR* newFile;
    PyObject* boolFailIfExists;
    if (!PyArg_ParseTuple(args, "ssO", &currentFile, &newFile, &boolFailIfExists)) return NULL;

    if (!PyBool_Check(boolFailIfExists)) {
        PyErr_SetString(PyExc_TypeError, "argument 3: excepted bool object");
        return NULL;
    }
    BOOL bFailIfExist = PyObject_IsTrue(boolFailIfExists);
    if (RaiseExceptionCheck(CopyFileA(currentFile, newFile, bFailIfExist))) return NULL;

    return Py_BuildValue("i", 0);
}
static PyObject* PyCopyFileW(PyObject* _, PyObject* args) {
    WCHAR* currentFile;
    WCHAR* newFile;
    PyObject* boolFailIfExists;
    if (!PyArg_ParseTuple(args, "uuO", &currentFile, &newFile, &boolFailIfExists)) return NULL;

    if (!PyBool_Check(boolFailIfExists)) {
        PyErr_SetString(PyExc_TypeError, "argument 3: excepted bool object");
        return NULL;
    }
    BOOL bFailIfExist = PyObject_IsTrue(boolFailIfExists);
    if (RaiseExceptionCheck(CopyFileW(currentFile, newFile, bFailIfExist))) return NULL;

    return Py_BuildValue("i", 0);
}
static PyObject* PyDeleteFileA(PyObject* _, PyObject* args) {
    CHAR* targetFile;
    if (!PyArg_ParseTuple(args, "s", &targetFile)) return NULL;
    if (RaiseExceptionCheck(DeleteFileA(targetFile))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyDeleteFileW(PyObject* _, PyObject* args) {
    WCHAR* targetFile;
    if (!PyArg_ParseTuple(args, "u", &targetFile)) return NULL;
    if (RaiseExceptionCheck(DeleteFileW(targetFile))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyGetComputerNameA(PyObject* _, PyObject* args) {
    CHAR sz[MAX_COMPUTERNAME_LENGTH + 1];
    DWORD len = sizeof(sz) / sizeof(CHAR);
    if (RaiseExceptionCheck(GetComputerNameA(sz, &len))) return NULL;
    return Py_BuildValue("s", sz);
}
static PyObject* PyGetComputerNameW(PyObject* _, PyObject* args) {
    WCHAR buffer[MAX_COMPUTERNAME_LENGTH + 1];
    DWORD sz = sizeof(buffer) / sizeof(WCHAR);
    if (RaiseExceptionCheck(GetComputerNameW(buffer, &sz))) return NULL;
    return Py_BuildValue("u", buffer);
}
static PyObject* PyGetComputerNameExA(PyObject* _, PyObject* args) {
    COMPUTER_NAME_FORMAT targetName;
    if (!PyArg_ParseTuple(args, "i", &targetName)) return NULL;
    DWORD szRequired;
    GetComputerNameExA(targetName, NULL, &szRequired);
    LPSTR s = malloc(sizeof(CHAR) * szRequired);
    if (RaiseExceptionCheck(GetComputerNameExA(targetName, s, &szRequired))) return NULL;
    return Py_BuildValue("s", s);
}
static PyObject* PyGetComputerNameExW(PyObject* _, PyObject* args) {
    COMPUTER_NAME_FORMAT targetName;
    if (!PyArg_ParseTuple(args, "i", &targetName)) return NULL;
    DWORD szRequired;
    GetComputerNameExW(targetName, NULL, &szRequired);
    LPWSTR s = malloc(sizeof(CHAR) * szRequired);
    if (RaiseExceptionCheck(GetComputerNameExW(targetName, s, &szRequired))) return NULL;
    return Py_BuildValue("u", s);
}
static PyObject* PyPlaySoundA(PyObject* _, PyObject* args) {
    LPCSTR str;
    PyObject* obSound;
    HMODULE mod = NULL;
    PyObject* obMod;
    DWORD flags;
    if (!PyArg_ParseTuple(args, "OOk", &obSound, &obMod, &flags)) return NULL;
    if (obMod != Py_None) mod = PyLong_AsLongLong(obMod);

    if (PyLong_Check(obSound)) {
        str = (LPCSTR)(PyLong_AsLongLong(obSound));
    } else {
        if (obSound == Py_None) {
            str = NULL;
        } else {
            str = PyString_ToCharArr(obSound);
        }
    }

    if (!PlaySoundA(str, mod, flags)) {
        PyErr_SetFromWindowsErr(87);
        return NULL;
    }

    return Py_BuildValue("i", 0);
}
static PyObject* PyPlaySoundW(PyObject* _, PyObject* args) {
    LPCWSTR str;
    PyObject* obSound;
    HMODULE mod = NULL;
    PyObject* obMod;
    DWORD flags;
    if (!PyArg_ParseTuple(args, "OOk", &obSound, &obMod, &flags)) return NULL;
    if (obMod != Py_None) mod = PyLong_AsLongLong(obMod);

    if (PyLong_Check(obSound)) {
        str = (LPCWSTR)(PyLong_AsLongLong(obSound));
    }
    else {
        if (obSound == Py_None) {
            str = NULL;
        } else {
            str = PyUnicode_AsWideCharString(obSound, NULL);
        }
    }

    if (!PlaySoundW(str, mod, flags)) {
        PyErr_SetFromWindowsErr(87);
        return NULL;
    }

    return Py_BuildValue("i", 0);
}
static PyObject* PySendMessageW(PyObject* _, PyObject* args) {
    HWND h;
    UINT msg;
    LONGLONG lParamX;
    LONGLONG lParamY = -6294576;
    ULONGLONG wParam;
    LPARAM lRes;
    PyOb oblParamX;
    if (!PyArg_ParseTuple(args, "lIKO|L", &h, &msg, &wParam, &oblParamX, &lParamY)) return NULL;

    if (PyLong_Check(oblParamX)){
        lRes = PyLong_AsLongLong(oblParamX);
    } else {
        lRes = (LPARAM)PyUnicode_AsWideCharString(oblParamX, NULL);
    }

    if (lParamY != -6294576) {
        lRes = MAKELPARAM(PyLong_AsLong(oblParamX), lParamY);
    }
    LONGLONG res = SendMessageW(h, msg, wParam, lRes);
    return Py_BuildValue("L", res);
}
static PyObject* PySendMessageA(PyObject* _, PyObject* args) {
    HWND h;
    UINT msg;
    LONGLONG lParamX;
    LONGLONG lParamY = -6294576;
    ULONGLONG wParam;
    LPARAM lRes;
    PyOb oblParamX;
    if (!PyArg_ParseTuple(args, "lIKO|L", &h, &msg, &wParam, &oblParamX, &lParamY)) return NULL;

    if (PyLong_Check(oblParamX)) {
        lRes = PyLong_AsLongLong(oblParamX);
    } else {
        lRes = (LPARAM)PyString_ToCharArr(oblParamX);
    }
    if (lParamY != -6294576) {
        lRes = MAKELPARAM(PyLong_AsLong(oblParamX), lParamY);
    }
    LONGLONG res = SendMessageA(h, msg, wParam, lRes);
    return Py_BuildValue("L", res);
}
static PyObject* PyGetModuleHandleA(PyObject* _, PyObject* args) {
    PyObject* obModule = Py_None;
    LPCSTR mod = NULL;
    if (!PyArg_ParseTuple(args, "|O", &obModule)) return NULL;
    if (obModule != Py_None) {
        mod = PyString_ToCharArr(obModule);
    }
    HMODULE model = GetModuleHandleA(mod);
    if (RaiseExceptionCheck(model)) return NULL;
    return Py_BuildValue("L", model);
}
static PyObject* PyGetModuleHandleW(PyObject* _, PyObject* args) {
    PyObject* obModule = Py_None;
    LPCWSTR mod = NULL;
    if (!PyArg_ParseTuple(args, "|O", &obModule)) return NULL;
    if (obModule != Py_None) {
        mod = PyUnicode_AsWideCharString(obModule, NULL);
    }
    HMODULE model = GetModuleHandleW(mod);
    if (RaiseExceptionCheck(model)) return NULL;
    return Py_BuildValue("L", model);
}
static PyObject* PyDestroyIcon(PyObject* _, PyObject* args) {
    HICON ic;
    if (!PyArg_ParseTuple(args, "L", &ic)) return NULL;
    if (RaiseExceptionCheck(DestroyIcon(ic))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyMessageBoxIndirectA(PyObject* _, PyObject* args) {
    MSGBOXPARAMSA par;
    HICON ic;
    HWND h = NULL;
    par.dwLanguageId = MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT);
    par.dwContextHelpId = 0;
    par.lpfnMsgBoxCallback = NULL;
    par.cbSize = sizeof(MSGBOXPARAMSA);
    PyObject* obHwnd;
    if (!PyArg_ParseTuple(args, "OLsskL|k", &obHwnd, &par.hInstance, &par.lpszText, &par.lpszCaption, &par.dwStyle,
        &ic, &par.dwLanguageId
    )) return NULL;
    if (obHwnd != Py_None) h = PyLong_AsLong(obHwnd);
    par.lpszIcon = MAKEINTRESOURCEA(ic);
    par.hwndOwner = h;
    INT res = MessageBoxIndirectA(&par);
    if (!res) {
        PyErr_SetString(PyExc_MemoryError, "Too little memory is available to create the message box!");
        return NULL;
    }
    return Py_BuildValue("i", res);
}
static PyObject* PyMessageBoxIndirectW(PyObject* _, PyObject* args) {
    MSGBOXPARAMSW par;
    HICON ic;
    HWND h = NULL;
    par.dwLanguageId = MAKELANGID(LANG_NEUTRAL, SUBLANG_DEFAULT);
    par.dwContextHelpId = NULL;
    par.lpfnMsgBoxCallback = NULL;
    par.cbSize = sizeof(MSGBOXPARAMSW);
    PyObject* obHwnd;
    if (!PyArg_ParseTuple(args, "OLuukL|k", &obHwnd, &par.hInstance, &par.lpszText, &par.lpszCaption, &par.dwStyle,
        &ic, &par.dwLanguageId
    )) return NULL;
    if (obHwnd != Py_None) h = PyLong_AsLong(obHwnd);
    par.hwndOwner = h;
    par.lpszIcon = MAKEINTRESOURCEW(ic);
    INT res = MessageBoxIndirectW(&par);
    if (!res) {
        PyErr_SetString(PyExc_MemoryError, "Too little memory is available to create the message box!");
        return NULL;
    }
    return Py_BuildValue("i", res);
}
static PyOb PyEnableWindow(PyOb _, PyOb args) {
    HWND h;
    BOOL enabled;
    PyOb obEnabled;
    if (!PyArg_ParseTuple(args, "lO", &h, &obEnabled)) return NULL;
    if (!PyBool_Check(obEnabled)) {
        PyErr_SetString(PyExc_TypeError, "argument 2: excepted bool object");
        return NULL;
    }
    enabled = PyObject_IsTrue(obEnabled);
    if (RaiseExceptionCheck(EnableWindow(h, enabled))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyOb PySetDlgItemTextA(PyOb _, PyOb args) {
    LPSTR s;
    HWND h;
    INT ctrl;
    if (!PyArg_ParseTuple(args, "lis", &h, &ctrl, &s)) return NULL;
    if (RaiseExceptionCheck(SetDlgItemTextA(h, ctrl, s))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyOb PySetDlgItemTextW(PyOb _, PyOb args) {
    LPWSTR s;
    HWND h;
    INT ctrl;
    if (!PyArg_ParseTuple(args, "liu", &h, &ctrl, &s)) return NULL;
    if (RaiseExceptionCheck(SetDlgItemTextW(h, ctrl, s))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyOb PyGetDlgCtrlID(PyOb _, PyOb args) {
    HWND h;
    if (!PyArg_ParseTuple(args, "l", &h)) return NULL;
    INT res = GetDlgCtrlID(h);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_BuildValue("i", res);
}
static PyOb PyGetDialogBaseUnits(PyOb _, PyOb args) {
    LONG res = GetDialogBaseUnits();
    return Py_BuildValue("(ll)", LOWORD(res), HIWORD(res));
}
static PyOb PySendDlgItemMessageA(PyOb _, PyOb args) {
    HWND hDlg;
    INT item;
    UINT msg;
    PyOb obLParam;
    PyOb obWParam;
    WPARAM wParam;
    LPARAM lParam;
    
    if (!PyArg_ParseTuple(args, "liIOO", &hDlg, &item, &msg, &obWParam, &obLParam)) return NULL;

    if (PyLong_Check(obWParam)) {
        wParam = PyLong_AsUnsignedLongLong(obWParam);
    } else {
        wParam = PyString_ToCharArr(obWParam);
    }

    if (PyLong_Check(obLParam)) {
        lParam = PyLong_AsUnsignedLongLong(obLParam);
    }
    else {
        if (PyTuple_Check(obLParam)) {
            if (PyTuple_GET_SIZE(obLParam) != 2) {
                PyErr_SetString(PyExc_ValueError, "argument 2: must be a tuple of two integers, string or int object");
                return NULL;
            }
            lParam = MAKELPARAM(PyLong_AsLong(PyTuple_GetItem(obLParam, 0)), PyLong_AsLong(PyTuple_GetItem(obLParam, 1)));
        }
        else {
            lParam = PyString_ToCharArr(obLParam);
        }
    }
    LRESULT res = SendDlgItemMessageA(hDlg, item, msg, wParam, lParam);
    return Py_BuildValue("L", res);
}
static PyOb PySendDlgItemMessageW(PyOb _, PyOb args) {
    HWND hDlg;
    INT item;
    UINT msg;
    PyOb obLParam;
    PyOb obWParam;
    WPARAM wParam;
    LPARAM lParam;

    if (!PyArg_ParseTuple(args, "liIOO", &hDlg, &item, &msg, &obWParam, &obLParam)) return NULL;

    if (PyLong_Check(obWParam)) {
        wParam = PyLong_AsUnsignedLongLong(obWParam);
    }
    else {
        wParam = PyString_ToCharArr(obWParam);
    }

    if (PyLong_Check(obLParam)) {
        lParam = PyLong_AsUnsignedLongLong(obLParam);
    }
    else {
        if (PyTuple_Check(obLParam)) {
            if (PyTuple_GET_SIZE(obLParam) != 2) {
                PyErr_SetString(PyExc_ValueError, "argument 2: must be a tuple of two integers, string or int object");
                return NULL;
            }
            lParam = MAKELPARAM(PyLong_AsLong(PyTuple_GetItem(obLParam, 0)), PyLong_AsLong(PyTuple_GetItem(obLParam, 1)));
        }
        else {
            lParam = PyUnicode_AsWideCharString(obLParam, NULL);
        }
    }
    LRESULT res = SendDlgItemMessageW(hDlg, item, msg, wParam, lParam);
    return Py_BuildValue("L", res);
}
static PyObject* PyLOWORD(PyObject* _, PyObject* args) {
    LONG i;
    if (!PyArg_ParseTuple(args, "l", &i)) return NULL;
    return Py_BuildValue("H", LOWORD(i));
}
static PyObject* PyHIWORD(PyObject* _, PyObject* args) {
    LONG i;
    if (!PyArg_ParseTuple(args, "l", &i)) return NULL;
    return Py_BuildValue("H", HIWORD(i));
}

typedef struct __PyWindowData {
    PyObject* callback;
} PyWindowData, *PPyWindowData, *LPPyWindowData;

LRESULT CALLBACK PyWndProcHandlerA(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    PyWindowData* wndptr = (PyWindowData*)GetWindowLongPtr(hwnd, WGWLP_USERDATA);
    if (wndptr == NULL) {
        return DefWindowProcA(hwnd, uMsg, wParam, lParam);
    }

    PyObject* ob = PyObject_CallFunction(wndptr->callback, "lIKL", hwnd, uMsg, wParam, lParam);

    if (uMsg == WM_QUIT) {
        free(wndptr);
    }

    if (ob == NULL) {
        return FALSE;
    }
    return PyLong_AsLongLong(ob);
}
LRESULT CALLBACK PyWndProcHandlerW(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    PyWindowData* wndptr = (PyWindowData*)GetWindowLongPtr(hwnd, WGWLP_USERDATA);
    if (wndptr == NULL) {
        return DefWindowProcW(hwnd, uMsg, wParam, lParam);
    }

    PyObject* ob = PyObject_CallFunction(wndptr->callback, "lIKL", hwnd, uMsg, wParam, lParam);

    if (uMsg == WM_QUIT) {
        free(wndptr);
    }

    if (ob == NULL) {
        return FALSE;
    }
    return PyLong_AsLongLong(ob);
}

static PyObject* PyRegisterClassA(PyObject* _, PyObject* args) {
    PyObject* wndClass;
    WNDCLASSA wnd;
    if (!PyArg_ParseTuple(args, "O", &wndClass)) return NULL;

    if (!PyDict_Check(wndClass)) {
        PyErr_SetString(PyExc_TypeError, "argument 1: excepted dictionary object filled with class settings");
        return NULL;
    }

    wnd.hCursor = NULL;
    wnd.cbClsExtra = 0;
    wnd.cbWndExtra = 0;
    wnd.hIcon = NULL;
    wnd.lpszMenuName = NULL;

    PyObject* key, * value;
    Py_ssize_t pos = 0;

    while (PyDict_Next(wndClass, &pos, &key, &value)) {
        if (PyObject_RichCompareBool(key, Py_BuildValue("s", "style"), Py_EQ)) {
            ULONG style = PyLong_AsUnsignedLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key style: excepted integer object");
                return NULL;
            }
            wnd.style = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "lpfnWndProc"), Py_EQ)) {
            if (!PyCallable_Check(value)) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key lpfnWndProc: excepted callable object");
                return NULL;
            }
            wnd.lpfnWndProc = PyWndProcHandlerA; // -.-
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "hIcon"), Py_EQ)) {
            if (value == Py_None) continue;
            LONGLONG style = PyLong_AsLongLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key hIcon: excepted integer (handle to an icon) object");
                return NULL;
            }
            wnd.hIcon = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "hCursor"), Py_EQ)) {
            if (value == Py_None) continue;
            LONGLONG style = PyLong_AsLongLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key hCursor: excepted integer (handle to a cursor) object");
                return NULL;
            }
            wnd.hCursor = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "cbClsExtra"), Py_EQ)) {
            LONG style = PyLong_AsLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key cbClsExtra: excepted integer object");
                return NULL;
            }
            wnd.cbClsExtra = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "cbWndExtra"), Py_EQ)) {
            LONG style = PyLong_AsLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key cbWndExtra: excepted integer object");
                return NULL;
            }
            wnd.cbWndExtra = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "hInstance"), Py_EQ)) {
            LONGLONG hInst = PyLong_AsLongLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key hInstance: excepted integer (handle to instance) object");
                return NULL;
            }
            wnd.hInstance = hInst;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "hbrBackground"), Py_EQ)) {
            if (value == Py_None) continue;
            LONGLONG brush = PyLong_AsLongLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key hbrBackground: excepted integer (handle to brush) object");
                return NULL;
            }
            wnd.hbrBackground = brush;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "lpszMenuName"), Py_EQ)) {
            if (value == Py_None) continue;
            LPSTR name = PyString_ToCharArr(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key lpszMenuName: excepted str object");
                return NULL;
            }
            wnd.lpszMenuName = name;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "lpszClassName"), Py_EQ)) {
            if (value == Py_None) continue;
            if (PyLong_Check(value)) {
                wnd.lpszClassName = (LPSTR)PyLong_AsLongLong(value);
            }
            else { wnd.lpszClassName = PyString_ToCharArr(value); }
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key lpszMenuName: excepted str or handle to atom object");
                return NULL;
            }
        }
    }
    ATOM res = RegisterClassA(&wnd);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_BuildValue("H", res);
}
static PyObject* PyRegisterClassW(PyObject* _, PyObject* args) {
    PyObject* wndClass;
    WNDCLASSW wnd;
    if (!PyArg_ParseTuple(args, "O", &wndClass)) return NULL;

    if (!PyDict_Check(wndClass)) {
        PyErr_SetString(PyExc_TypeError, "argument 1: excepted dictionary object filled with class settings");
        return NULL;
    }

    wnd.hCursor = NULL;
    wnd.cbClsExtra = 0;
    wnd.cbWndExtra = 0;
    wnd.hIcon = NULL;
    wnd.lpszMenuName = NULL;

    PyObject* key, * value;
    Py_ssize_t pos = 0;

    while (PyDict_Next(wndClass, &pos, &key, &value)) {
        if (PyObject_RichCompareBool(key, Py_BuildValue("s", "style"), Py_EQ)) {
            ULONG style = PyLong_AsUnsignedLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key style: excepted integer object");
                return NULL;
            }
            wnd.style = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "lpfnWndProc"), Py_EQ)) {
            if (!PyCallable_Check(value)) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key lpfnWndProc: excepted callable object");
                return NULL;
            }
            wnd.lpfnWndProc = PyWndProcHandlerW; // -.-
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "hIcon"), Py_EQ)) {
            if (value == Py_None) continue;
            LONGLONG style = PyLong_AsLongLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key hIcon: excepted integer (handle to an icon) object");
                return NULL;
            }
            wnd.hIcon = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "hCursor"), Py_EQ)) {
            if (value == Py_None) continue;
            LONGLONG style = PyLong_AsLongLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key hCursor: excepted integer (handle to a cursor) object");
                return NULL;
            }
            wnd.hCursor = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "cbClsExtra"), Py_EQ)) {
            LONG style = PyLong_AsLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key cbClsExtra: excepted integer object");
                return NULL;
            }
            wnd.cbClsExtra = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "cbWndExtra"), Py_EQ)) {
            LONG style = PyLong_AsLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key cbWndExtra: excepted integer object");
                return NULL;
            }
            wnd.cbWndExtra = style;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "hInstance"), Py_EQ)) {
            LONGLONG hInst = PyLong_AsLongLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key hInstance: excepted integer (handle to instance) object");
                return NULL;
            }
            wnd.hInstance = hInst;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "hbrBackground"), Py_EQ)) {
            if (value == Py_None) continue;
            LONGLONG brush = PyLong_AsLongLong(value);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key hbrBackground: excepted integer (handle to brush) object");
                return NULL;
            }
            wnd.hbrBackground = brush;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "lpszMenuName"), Py_EQ)) {
            if (value == Py_None) continue;
            LPWSTR name = PyUnicode_AsWideCharString(value, NULL);
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key lpszMenuName: excepted str object");
                return NULL;
            }
            wnd.lpszMenuName = name;
        }
        else if (PyObject_RichCompareBool(key, Py_BuildValue("s", "lpszClassName"), Py_EQ)) {
            if (value == Py_None) continue;
            if (PyLong_Check(value)) {
                wnd.lpszClassName = (LPWSTR)PyLong_AsLongLong(value);
            }
            else { wnd.lpszClassName = PyUnicode_AsWideCharString(value, NULL); }
            if (PyErr_Occurred()) {
                PyErr_SetString(PyExc_ValueError, "argument 1: key lpszMenuName: excepted str or handle to atom object");
                return NULL;
            }
        }
    }
    ATOM res = RegisterClassW(&wnd);
    if (RaiseExceptionCheck(res)) return NULL;
    return Py_BuildValue("H", res);
}
static PyObject* PyUnregisterClassA(PyObject* _, PyObject* args) {
    PyObject* obClass;
    LPSTR name = NULL;
    LONGLONG hInstance;
    if (!PyArg_ParseTuple(args, "OL", &obClass, &hInstance)) return NULL;

    if (PyLong_Check(obClass)) name = MAKELONG(PyLong_AsLongLong(obClass), 0);
    else name = PyString_ToCharArr(obClass);

    if (RaiseExceptionCheck(UnregisterClassA(name, hInstance))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyUnregisterClassW(PyObject* _, PyObject* args) {
    PyObject* obClass;
    LPWSTR name = NULL;
    LONGLONG hInstance;
    if (!PyArg_ParseTuple(args, "OL", &obClass, &hInstance)) return NULL;

    if (PyLong_Check(obClass)) name = MAKELONG(PyLong_AsLongLong(obClass), 0);
    else name = PyUnicode_AsWideCharString(obClass, NULL);

    if (RaiseExceptionCheck(UnregisterClassW(name, hInstance))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyCreateWindowExA(PyObject* _, PyObject* args) {
    DWORD dwExStyle;
    PyObject* wndproc;
    LPSTR lpWindowName;
    DWORD dwStyle;
    long X;
    long Y;
    long width;
    long height;
    PyObject* obParent;
    PyObject* obHMenu;
    HINSTANCE hInstance;
    PyObject* obLParam = Py_None;

    HWND hwndParent = NULL;
    HWND hMenu = NULL;

    if (!PyArg_ParseTuple(args, "kOskllllOOL", &dwExStyle, &wndproc, &lpWindowName, &dwStyle, &X, &Y, &width, &height, &obParent, &obHMenu, &hInstance)) return NULL;
    
    if (!PyDict_Check(wndproc)) {
        PyErr_SetString(PyExc_TypeError, "argument 2: Excepted same dictionary containing window settings passed to RegisterClass");
        return NULL;
    }

    PyObject* callback;
    PyObject* obAtom;

    if (!PyDict_Contains(wndproc, Py_BuildValue("s", "lpfnWndProc"))) {
        PyErr_SetString(PyExc_ValueError, "argument 2: required key lpfnWndProc missing");
        return NULL;
    }
    if (!PyDict_Contains(wndproc, Py_BuildValue("s", "lpszClassName"))) {
        PyErr_SetString(PyExc_ValueError, "argument 2: required key lpszClassName missing");
        return NULL;
    }

    callback = PyDict_GetItemString(wndproc, "lpfnWndProc");
    obAtom   = PyDict_GetItemString(wndproc, "lpszClassName");
    if (!PyUnicode_Check(obAtom)) {
        PyErr_SetString(PyExc_ValueError, "argument 2: key lpszClassName: str object excepted");
        return NULL;
    }
    LPSTR atom = PyString_ToCharArr(obAtom);

    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_ValueError, "argument 2: key lpfnWndProc: callable object excepted");
        return NULL;
    }

    if (obParent != Py_None) hwndParent = PyLong_AsLong(obParent);
    if (obHMenu != Py_None)  hMenu = PyLong_AsLong(obParent);

    PPyWindowData data = malloc(sizeof(PyWindowData));
    data->callback = callback;
    HWND hwnd = CreateWindowExA(
        dwExStyle,
        atom,
        lpWindowName,
        dwStyle,
        X,
        Y,
        width,
        height,
        hwndParent,
        hMenu,
        hInstance,
        (LPVOID)callback
    );

    if (RaiseExceptionCheck(hwnd == NULL)) return NULL;

    SetWindowLongPtr(hwnd, GWLP_USERDATA, data);
    return Py_BuildValue("L", hwnd);
}
static PyObject* PyCreateWindowExW(PyObject* _, PyObject* args) {
    DWORD dwExStyle;
    PyObject* wndproc;
    wchar_t* title;
    PyObject* obTitle;
    DWORD dwStyle;
    long X;
    long Y;
    long width;
    long height;
    PyObject* obParent;
    PyObject* obHMenu;
    HINSTANCE hInstance;
    PyObject* obLParam = Py_None;

    HWND hwndParent = NULL;
    HWND hMenu = NULL;

    if (!PyArg_ParseTuple(args, "kOOkllllOOL", &dwExStyle, &wndproc, &obTitle, &dwStyle, &X, &Y, &width, &height, &obParent, &obHMenu, &hInstance)) return NULL;

    if (!PyDict_Check(wndproc)) {
        PyErr_SetString(PyExc_TypeError, "argument 2: Excepted same dictionary containing window settings passed to RegisterClass");
        return NULL;
    }

    PyObject* callback;
    PyObject* obAtom;

    if (!PyDict_Contains(wndproc, Py_BuildValue("s", "lpfnWndProc"))) {
        PyErr_SetString(PyExc_ValueError, "argument 2: required key lpfnWndProc missing");
        return NULL;
    }
    if (!PyDict_Contains(wndproc, Py_BuildValue("s", "lpszClassName"))) {
        PyErr_SetString(PyExc_ValueError, "argument 2: required key lpszClassName missing");
        return NULL;
    }

    callback = PyDict_GetItemString(wndproc, "lpfnWndProc");
    obAtom = PyDict_GetItemString(wndproc, "lpszClassName");
    if (!PyUnicode_Check(obAtom)) {
        PyErr_SetString(PyExc_ValueError, "argument 2: key lpszClassName: str object excepted");
        return NULL;
    }
    LPWSTR atom = PyUnicode_AsWideCharString(obAtom, NULL);

    if (!PyCallable_Check(callback)) {
        PyErr_SetString(PyExc_ValueError, "argument 2: key lpfnWndProc: callable object excepted");
        return NULL;
    }

    if (!PyUnicode_Check(obTitle)) {
        PyErr_SetString(PyExc_TypeError, "argument 3: str object excepted");
        return NULL;
    }

    title = PyUnicode_AsWideCharString(obTitle, NULL);

    if (obParent != Py_None) hwndParent = PyLong_AsLong(obParent);
    if (obHMenu != Py_None) hMenu = PyLong_AsLong(obParent);


    PPyWindowData data = malloc(sizeof(PyWindowData));
    data->callback = callback;
    HWND hwnd = CreateWindowExW(
        dwExStyle,
        atom,
        title,
        dwStyle,
        X,
        Y,
        width,
        height,
        hwndParent,
        hMenu,
        hInstance,
        NULL
    );

    PyMem_Free(title);

    if (RaiseExceptionCheck(hwnd == NULL)) return NULL;

    SetWindowLongPtr(hwnd, GWLP_USERDATA, data);
    return Py_BuildValue("L", hwnd);
}

static PyObject* PyDefWindowProcA(PyObject* _, PyObject* args) {
    HWND hwnd;
    UINT msg;
    LONG_PTR lParam;
    UINT_PTR wParam;

    if (!PyArg_ParseTuple(args, "lIKL", &hwnd, &msg, &wParam, &lParam)) return NULL;
    return Py_BuildValue("L", DefWindowProcA(hwnd, msg, wParam, lParam));
}
static PyObject* PyDefWindowProcW(PyObject* _, PyObject* args) {
    HWND hwnd;
    UINT msg;
    LONG_PTR lParam;
    UINT_PTR wParam;

    if (!PyArg_ParseTuple(args, "lIKL", &hwnd, &msg, &wParam, &lParam)) return NULL;
    return Py_BuildValue("L", DefWindowProcW(hwnd, msg, wParam, lParam));
}
static PyObject* PyGetMessageA(PyObject* _, PyObject* args) {
    MSG msg;
    PyObject* obHwnd;
    HWND h = NULL;
    UINT wMsgFilterMin;
    UINT wMsgFilterMax;
    if (!PyArg_ParseTuple(args, "OII", &obHwnd, &wMsgFilterMin, &wMsgFilterMax)) return NULL;
    if (obHwnd != Py_None) h = PyLong_AsLong(obHwnd);
    if (RaiseExceptionCheck(GetMessageA(&msg, h, wMsgFilterMin, wMsgFilterMax) == -1)) return NULL;
    return Py_BuildValue("(lIKLkO)", msg.hwnd, msg.message, msg.wParam, msg.lParam, msg.time, Py_BuildValue("(ii)", msg.pt.x, msg.pt.y));
}
static PyObject* PyGetMessageW(PyObject* _, PyObject* args) {
    MSG msg;
    PyObject* obHwnd;
    HWND h = NULL;
    UINT wMsgFilterMin;
    UINT wMsgFilterMax;
    if (!PyArg_ParseTuple(args, "OII", &obHwnd, &wMsgFilterMin, &wMsgFilterMax)) return NULL;
    if (obHwnd != Py_None) h = PyLong_AsLong(obHwnd);
    if (RaiseExceptionCheck(GetMessageW(&msg, h, wMsgFilterMin, wMsgFilterMax) == -1)) return NULL;
    return Py_BuildValue("(lIKLkO)", msg.hwnd, msg.message, msg.wParam, msg.lParam, msg.time, Py_BuildValue("(ii)", msg.pt.x, msg.pt.y));
}
static PyObject* PyTranslateMessage(PyObject* _, PyObject* args) {
    MSG msg;
    PyObject* pt;
    if (!PyArg_ParseTuple(args, "(lIKLkO)", &msg.hwnd, &msg.message, &msg.wParam, &msg.lParam, &msg.time, &pt)) return NULL;
    msg.pt.x = PyTuple_GetItem(pt, 0);
    msg.pt.y = PyTuple_GetItem(pt, 1);
    if (RaiseExceptionCheck(TranslateMessage(&msg))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyDispatchMessageA(PyObject* _, PyObject* args) {
    MSG msg;
    PyObject* pt;
    if (!PyArg_ParseTuple(args, "(lIKLkO)", &msg.hwnd, &msg.message, &msg.wParam, &msg.lParam, &msg.time, &pt)) return NULL;
    msg.pt.x = PyTuple_GetItem(pt, 0);
    msg.pt.y = PyTuple_GetItem(pt, 1);
    LRESULT res = DispatchMessageA(&msg);
    return Py_BuildValue("L", res);
}
static PyObject* PyDispatchMessageW(PyObject* _, PyObject* args) {
    MSG msg;
    PyObject* pt;
    if (!PyArg_ParseTuple(args, "(lIKLkO)", &msg.hwnd, &msg.message, &msg.wParam, &msg.lParam, &msg.time, &pt)) return NULL;
    msg.pt.x = PyTuple_GetItem(pt, 0);
    msg.pt.y = PyTuple_GetItem(pt, 1);
    LRESULT res = DispatchMessageW(&msg);
    return Py_BuildValue("L", res);
}
static PyObject* PyPumpMessagesW(PyObject* _, PyObject* args) {
    MSG msg;
    while (GetMessageW(&msg, NULL, 0, 0) > 0)
    {
        TranslateMessage(&msg);
        DispatchMessageW(&msg);
    }
    return Py_BuildValue("i", 0);
}
static PyObject* PyPumpMessagesA(PyObject* _, PyObject* args) {
    MSG msg;
    while (GetMessageA(&msg, NULL, 0, 0) > 0)
    {
        TranslateMessage(&msg);
        DispatchMessageA(&msg);
    }
    return Py_BuildValue("i", 0);
}
static PyObject* PyPostQuitMessage(PyObject* _, PyObject* args) {
    INT statusCode = 0;
    if (!PyArg_ParseTuple(args, "|i", &statusCode)) return NULL;
    PostQuitMessage(statusCode);
    return Py_BuildValue("i", 0);
}
static PyObject* PyDestroyWindow(PyObject* _, PyObject* args) {
    HWND h;
    if (!PyArg_ParseTuple(args, "l", &h)) return NULL;
    if (RaiseExceptionCheck(DestroyWindow(h))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyBeginPaint(PyObject* _, PyObject* args) {
    PAINTSTRUCT pst;
    HWND h;
    if (!PyArg_ParseTuple(args, "l", &h)) return NULL;
    HDC res = BeginPaint(h, &pst);
    if (res == NULL) {
        PyErr_SetString(PyExc_ValueError, "BeginPaint failed. The window handle is likely invalid.");
        return NULL;
    }
    return Py_BuildValue("(lO)",
        res,
        Py_BuildValue(
            "(lOOOOO)",
            pst.hdc,
            PyBool_FromLong(pst.fErase),
            Py_BuildValue("(iiii)", pst.rcPaint.left, pst.rcPaint.top, pst.rcPaint.right, pst.rcPaint.bottom),
            PyBool_FromLong(pst.fRestore),
            PyBool_FromLong(pst.fIncUpdate),
            PyByteArray_FromStringAndSize(pst.rgbReserved, 32)
        )
    );
}
static PyObject* PyEndPaint(PyObject* _, PyObject* args) {
    PAINTSTRUCT pst;
    HWND h;
    PyObject* obPs;
    if (!PyArg_ParseTuple(args, "lO", &h, &obPs)) return NULL;
    if (!PyTuple_Check(obPs)) {
        PyErr_SetString(PyExc_TypeError, "argument 2: excepted paint structure returned as second item from BeginPaint");
        return NULL;
    }
    pst.hdc = PyLong_AsLong(PyTuple_GetItem(obPs, 0));
    pst.fErase = PyObject_IsTrue(PyTuple_GetItem(obPs, 1));
    pst.rcPaint.left   = PyLong_AsLong(PyTuple_GetItem(PyTuple_GetItem(obPs, 2), 0));
    pst.rcPaint.top    = PyLong_AsLong(PyTuple_GetItem(PyTuple_GetItem(obPs, 2), 1));
    pst.rcPaint.right  = PyLong_AsLong(PyTuple_GetItem(PyTuple_GetItem(obPs, 2), 2));
    pst.rcPaint.bottom = PyLong_AsLong(PyTuple_GetItem(PyTuple_GetItem(obPs, 2), 3));
    pst.fRestore = PyObject_IsTrue(PyTuple_GetItem(obPs, 3));
    pst.fIncUpdate = PyObject_IsTrue(PyTuple_GetItem(obPs, 4));
    UCHAR* b = PyByteArray_AsString(PyTuple_GetItem(obPs, 5));
    for (INT i = 0; i < 32; i++) {
        pst.rgbReserved[i] = b[i];
    }
    EndPaint(h, &pst);
    return Py_BuildValue("i", 0);
}
static PyObject* PyUpdateWindow(PyObject* _, PyObject* args) {
    HWND h;
    if (!PyArg_ParseTuple(args, "l", &h)) return NULL;
    if (!UpdateWindow(h)) {
        PyErr_SetFromWindowsErr(87);
        return NULL;
    }
    return Py_BuildValue("i", 0);
}
static PyObject* PyGetUpdateRect(PyObject* _, PyObject* args) {
    HWND hwnd;
    PyObject* bErase;
    if (!PyArg_ParseTuple(args, "lO", &hwnd, &bErase)) return NULL;
    if (!PyBool_Check(bErase)) {
        PyErr_SetString(PyExc_TypeError, "argument 2: must be a bool object");
        return NULL;
    }
    BOOL beras = PyObject_IsTrue(bErase);
    RECT res;
    if (GetUpdateRect(hwnd, &res, beras)) {
        return Py_BuildValue("(iiii)", res.left, res.top, res.right, res.bottom);
    }
    return Py_BuildValue("O", Py_None);
}
static PyObject* PyIntersectRect(PyObject* _, PyObject* args) {
    RECT r1;
    RECT r2;
    if (!PyArg_ParseTuple(args, "(iiii)(iiii)", &r1.left,&r1.top,&r1.right,&r1.bottom, &r2.left, &r2.top, &r2.right, &r2.bottom)) return NULL;
    RECT res;
    BOOL intersect = IntersectRect(&res, &r1, &r2);
    return Py_BuildValue("(OO)", PyBool_FromLong(intersect), Py_BuildValue("(iiii)", res.left, res.top, res.right, res.bottom));
}
DWORD PyThreadHandler(LPVOID lpFunc) {
    PyObject_CallNoArgs((PyObject*)lpFunc);
    return 0;
}

static PyObject* PyCreateThread(PyObject* _, PyObject* args) {
    SIZE_T stack;
    PyObject* func;
    DWORD flags = 0;
    LPTHREAD_START_ROUTINE fanc = PyThreadHandler;

    if (!PyArg_ParseTuple(args, "KO|k", &stack, &func, &flags)) return NULL;

    if (!PyCallable_Check(func)) {
        if (!PyLong_Check(func)) {
            PyErr_SetString(PyExc_TypeError, "argument 2: must be callable function or address of pointer to a valid function");
            return NULL;
        }
        fanc = PyLong_AsLongLong(func);
    }

    DWORD dwThreadId;
    HANDLE hThread = CreateThread(NULL, stack, fanc, func, flags, &dwThreadId);
    if (RaiseExceptionCheck(hThread != NULL)) return NULL;
    return Py_BuildValue("(Lk)", hThread, dwThreadId);
}
static PyObject* PyTerminateThread(PyObject* _, PyObject* args) {
    HANDLE hThread;
    DWORD dwExitCode;
    if (!PyArg_ParseTuple(args, "Lk", &hThread, &dwExitCode)) return NULL;
    if (RaiseExceptionCheck(TerminateThread(hThread, dwExitCode))) return NULL;
    return Py_BuildValue("i", 0);
}
static PyObject* PyWaitForSingleObject(PyObject* _, PyObject* args) {
    HANDLE handle;
    DWORD dwMilliseconds;
    if (!PyArg_ParseTuple(args, "Lk", &handle, &dwMilliseconds)) return NULL;
    DWORD res = WaitForSingleObject(handle, dwMilliseconds);
    if (RaiseExceptionCheck(res != WAIT_FAILED)) return NULL;
    return Py_BuildValue("k", res);
}
static PyObject* PyWaitForMultipleObjects(PyObject* _, PyObject* args) {
    PyObject* objects;
    BOOL bWaitForAll;
    DWORD dwMilliseconds;
    if (!PyArg_ParseTuple(args, "Opk", &objects, &bWaitForAll, &dwMilliseconds)) return NULL;
    if ((!PyTuple_Check(objects)) || (PyTuple_GET_SIZE(objects) < 1)) {
        PyErr_SetString(PyExc_TypeError, "argument 1: excepted tuple object containing handles");
        return NULL;
    }
    DWORD nCount = PyTuple_GET_SIZE(objects);
    if (nCount > 64) {
        PyErr_SetString(PyExc_ValueError, "argument 1: maximum length for waitable objects is 64");
        return NULL;
    }
    PHANDLE pHandles = malloc(sizeof(HANDLE) * nCount);
    if (pHandles == NULL) return PyErr_NoMemory();

    for (INT i = 0; i < nCount; i++) {
        pHandles[i] = PyLong_AsLongLong(PyTuple_GetItem(objects, i));
    }
 
    DWORD dwRes = WaitForMultipleObjects(nCount, pHandles, bWaitForAll, dwMilliseconds);
    
    free(pHandles);
    if (RaiseExceptionCheck(dwRes != WAIT_FAILED)) return NULL;
    return Py_BuildValue("k", dwRes);
}


static PyMethodDef module_methods[] = {
    { "WaitForMultipleObjects", PyWaitForMultipleObjects, METH_VARARGS },
    { "WaitForSingleObject", PyWaitForSingleObject, METH_VARARGS },
    { "TerminateThread", PyTerminateThread, METH_VARARGS },
    { "CreateThread", PyCreateThread, METH_VARARGS },
    { "IntersectRect", PyIntersectRect, METH_VARARGS },
    { "GetUpdateRect", PyGetUpdateRect, METH_VARARGS },
    { "UpdateWindow", PyUpdateWindow, METH_VARARGS },
    { "EndPaint", PyEndPaint, METH_VARARGS },
    { "BeginPaint", PyBeginPaint, METH_VARARGS },
    { "DestroyWindow", PyDestroyWindow, METH_VARARGS },
    { "PostQuitMessage", PyPostQuitMessage, METH_VARARGS },
    { "PumpMessages",  PyPumpMessagesW, METH_NOARGS },
    { "PumpMessagesW", PyPumpMessagesW, METH_NOARGS },
    { "PumpMessagesA", PyPumpMessagesA, METH_NOARGS },
    { "DispatchMessage",  PyDispatchMessageW, METH_VARARGS },
    { "DispatchMessageW", PyDispatchMessageW, METH_VARARGS },
    { "DispatchMessageA", PyDispatchMessageA, METH_VARARGS },
    { "TranslateMessage", PyTranslateMessage, METH_VARARGS },
    { "GetMessage",  PyGetMessageW, METH_VARARGS },
    { "GetMessageW", PyGetMessageW, METH_VARARGS },
    { "GetMessageA", PyGetMessageA, METH_VARARGS },
    { "DefWindowProc",  PyDefWindowProcW, METH_VARARGS },
    { "DefWindowProcW", PyDefWindowProcW, METH_VARARGS },
    { "DefWindowProcA", PyDefWindowProcA, METH_VARARGS },
    { "CreateWindowEx",  PyCreateWindowExW, METH_VARARGS },
    { "CreateWindowExW", PyCreateWindowExW, METH_VARARGS },
    { "CreateWindowExA", PyCreateWindowExA, METH_VARARGS },
    { "UnregisterClass",  PyUnregisterClassW, METH_VARARGS },
    { "UnregisterClassW", PyUnregisterClassW, METH_VARARGS },
    { "UnregisterClassA", PyUnregisterClassA, METH_VARARGS },
    { "RegisterClass",  PyRegisterClassW, METH_VARARGS },
    { "RegisterClassW", PyRegisterClassW, METH_VARARGS },
    { "RegisterClassA", PyRegisterClassA, METH_VARARGS },
    { "HIWORD", PyHIWORD, METH_VARARGS },
    { "LOWORD", PyLOWORD, METH_VARARGS },
    { "SendDlgItemMessage",  PySendDlgItemMessageW, METH_VARARGS },
    { "SendDlgItemMessageW", PySendDlgItemMessageW, METH_VARARGS },
    { "SendDlgItemMessageA", PySendDlgItemMessageA, METH_VARARGS },
    { "GetDialogBaseUnits", PyGetDialogBaseUnits, METH_NOARGS },
    { "GetDlgCtrlID", PyGetDlgCtrlID, METH_VARARGS },
    { "SetDlgItemText",  PySetDlgItemTextW, METH_VARARGS },
    { "SetDlgItemTextW", PySetDlgItemTextW, METH_VARARGS },
    { "SetDlgItemTextA", PySetDlgItemTextA, METH_VARARGS },
    { "EnableWindow", PyEnableWindow, METH_VARARGS },
    { "MessageBoxIndirect",  PyMessageBoxIndirectW, METH_VARARGS },
    { "MessageBoxIndirectW", PyMessageBoxIndirectW, METH_VARARGS },
    { "MessageBoxIndirectA", PyMessageBoxIndirectA, METH_VARARGS },
    { "DestroyIcon", PyDestroyIcon, METH_VARARGS },
    { "GetModuleHandle",  PyGetModuleHandleW, METH_VARARGS },
    { "GetModuleHandleW", PyGetModuleHandleW, METH_VARARGS },
    { "GetModuleHandleA", PyGetModuleHandleA, METH_VARARGS },
    { "SendMessage",  PySendMessageW, METH_VARARGS },
    { "SendMessageW", PySendMessageW, METH_VARARGS },
    { "SendMessageA", PySendMessageA, METH_VARARGS },
    { "PlaySound",  PyPlaySoundW, METH_VARARGS },
    { "PlaySoundW", PyPlaySoundW, METH_VARARGS },
    { "PlaySoundA", PyPlaySoundA, METH_VARARGS },
    { "GetComputerNameEx",  PyGetComputerNameExW, METH_VARARGS },
    { "GetComputerNameExW", PyGetComputerNameExW, METH_VARARGS },
    { "GetComputerNameExA", PyGetComputerNameExA, METH_VARARGS },
    { "GetComputerName",  PyGetComputerNameW, METH_NOARGS },
    { "GetComputerNameW", PyGetComputerNameW, METH_NOARGS },
    { "GetComputerNameA", PyGetComputerNameA, METH_NOARGS },
    { "DeleteFile",  PyDeleteFileW, METH_VARARGS },
    { "DeleteFileW", PyDeleteFileW, METH_VARARGS },
    { "DeleteFileA", PyDeleteFileA, METH_VARARGS },
    { "CopyFileW", PyCopyFileW, METH_VARARGS },
    { "CopyFileA", PyCopyFileA, METH_VARARGS },
    { "CopyFile",  PyCopyFileW, METH_VARARGS },
    { "CloseHandle", PyCloseHandle, METH_VARARGS },
    { "GetCommandLine",  PyGetCommandLineW, METH_NOARGS },
    { "GetCommandLineA", PyGetCommandLineA, METH_NOARGS },
    { "GetCommandLineW", PyGetCommandLineW, METH_NOARGS },
    { "GetConsoleWindow", PyGetConsoleWindow, METH_NOARGS },
    { "AbortSystemShutdownA", PyAbortSystemShutdownA, METH_VARARGS },
    { "AbortSystemShutdownW", PyAbortSystemShutdownW, METH_VARARGS },
    { "AbortSystemShutdown",  PyAbortSystemShutdownW, METH_VARARGS },
    { "BlockInput", PyBlockInput, METH_VARARGS },
    { "ActivateKeyboardLayout", PyActivateKeyboardLayout, METH_VARARGS },
    { "GetKeyboardLayout", PyGetKeyboardLayout, METH_VARARGS },
    { "GetDC", (PyCFunction)PyGetDC, METH_VARARGS },
    { "GetSystemMetrics", (PyCFunction)PyGetSystemMetrics, METH_VARARGS },
    { "GetDesktopWindow", (PyCFunction)PyGetDesktopWindow,  METH_NOARGS },
    { "GetLastError", (PyCFunction)PyGetLastError, METH_NOARGS },
    { "rand", Pyrand, METH_NOARGS },
    { "Sleep", PySleep, METH_VARARGS },
    { "RedrawWindow", PyRedrawWindow, METH_VARARGS },
    { "InvalidateRect", PyInvalidateRect, METH_VARARGS },
    { "GetClientRect", PyGetClientRect, METH_VARARGS },
    { "WindowFromDC", PyWindowFromDC, METH_VARARGS },
    { "EnumChildWindows", PyEnumChildWindows, METH_VARARGS },
    { "GetWindowTextA", PyGetWindowTextA, METH_VARARGS },
    { "GetWindowTextW", PyGetWindowTextW, METH_VARARGS },
    { "GetWindowText",  PyGetWindowTextW, METH_VARARGS },
    { "GetWindowTextLengthA", PyGetWindowTextLengthA, METH_VARARGS },
    { "GetWindowTextLengthW", PyGetWindowTextLengthW, METH_VARARGS },
    { "GetWindowTextLength" , PyGetWindowTextLengthW, METH_VARARGS },
    { "GetWindowRect", PyGetWindowRect, METH_VARARGS },
    { "GetWindowPlacement", PyGetWindowPlacement, METH_VARARGS },
    { "WindowFromPoint", PyWindowFromPoint, METH_VARARGS },
    { "WindowFromPhysicalPoint", PyWindowFromPhysicalPoint, METH_VARARGS },
    { "SwitchToThisWindow", PySwitchToThisWindow, METH_VARARGS },
    { "ShowWindow", PyShowWindow, METH_VARARGS },
    { "ReleaseDC", PyReleaseDC, METH_VARARGS },
    { "GetCursorPos", PyGetCursorPos, METH_NOARGS },
    { "SetCursorPos", PySetCursorPos, METH_VARARGS },
    { "LoadIconA", PyLoadIconA, METH_VARARGS },
    { "DrawIcon", PyDrawIcon, METH_VARARGS },
    { "LoadIconW", PyLoadIconW, METH_VARARGS },
    { "LoadIcon",  PyLoadIconW, METH_VARARGS },
    { "DrawIconEx", PyDrawIconEx, METH_VARARGS },
    { "LoadImageA", PyLoadImageA, METH_VARARGS },
    { "LoadImageW", PyLoadImageW, METH_VARARGS },
    { "LoadImage",  PyLoadImageW, METH_VARARGS },
    { "LoadCursorFromFileA", PyLoadCursorFromFileA, METH_VARARGS },
    { "LoadCursorFromFileW", PyLoadCursorFromFileW, METH_VARARGS },
    { "LoadCursorFromFile",  PyLoadCursorFromFileW, METH_VARARGS },
    { "LoadCursorA", PyLoadCursorA, METH_VARARGS },
    { "LoadCursorW", PyLoadCursorW, METH_VARARGS },
    { "LoadCursor",  PyLoadCursorW, METH_VARARGS },
    { "GetCursorInfo", PyGetCursorInfo, METH_NOARGS },
    { "MessageBoxA", PyMessageBoxA, METH_VARARGS },
    { "MessageBoxW", PyMessageBoxW, METH_VARARGS },
    { "MessageBox",  PyMessageBoxW, METH_VARARGS },
    { "GetTopWindow", PyGetTopWindow, METH_VARARGS },
    { "MessageBeep", PyMessageBeep , METH_VARARGS },
    { "Beep", PyBeep, METH_VARARGS },
    { "ExitWindowsEx", PyExitWindowsEx , METH_VARARGS },
    { "ExitWindows", PyExitWindows, METH_NOARGS },
    { "InitiateSystemShutdownA", PyInitiateSystemShutdownA, METH_VARARGS },
    { "InitiateSystemShutdownW", PyInitiateSystemShutdownW, METH_VARARGS },
    { "InitiateSystemShutdown",  PyInitiateSystemShutdownW, METH_VARARGS },
    { "FillRect", PyFillRect, METH_VARARGS },

    /* sentinel */
    { 0 }
};

static struct PyModuleDef ModuleCombinations =
{
    PyModuleDef_HEAD_INIT,
    "winapy_user", /* name of module */
    NULL,
    -1,   /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables. */
    module_methods
};


void PyInit_winapy_user(void) {
    PyModule_Create(&ModuleCombinations);
}