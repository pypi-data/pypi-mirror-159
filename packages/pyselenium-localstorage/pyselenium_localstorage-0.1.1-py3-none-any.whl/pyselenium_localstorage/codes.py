LENGTH = "return window.localStorage.length;"
DICTIONARY = "var ls = window.localStorage, items = {}; " \
             "for (var i = 0, k; i < ls.length; ++i) " \
             "  items[k = ls.key(i)] = ls.getItem(k); " \
             "return items; "
KEYS = "var ls = window.localStorage, keys = []; " \
       "for (var i = 0; i < ls.length; ++i) " \
       "  keys[i] = ls.key(i); " \
       "return keys; "
GET = "return window.localStorage.getItem(arguments[0]);"
SET = "window.localStorage.setItem(arguments[0], arguments[1]);"
DEL = "window.localStorage.removeItem(arguments[0]);"
CLEAR = "window.localStorage.clear();"
