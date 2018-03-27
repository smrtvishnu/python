>>> from string import whitespace
>>> s = "TN 81   NZ\t\t0025\nfoo"
# Python 2
>>> s.translate(None, whitespace)
'TN81NZ0025foo'
# Python 3
>>> s.translate(dict.fromkeys(map(ord, whitespace)))
'TN81NZ0025foo'
