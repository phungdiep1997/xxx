s = "Hello %s" % ("Tu",)
s
name = "Python"
format = "hello %s"
format
format % (name,)
format2 = "hello %s, I'm %d year old, height: %f m"
format2
format2 % ("Dai", 25)
format2 % ("Dai", 25, 1.72)
import strings
import string
get_ipython().magic(u'pinfo2 string')
string2
format2
get_ipython().magic(u'pinfo2 format2.format')
format2.format("Dai", 27, 1.7)
format3 = "Hello {0}, I'm {1}, height: {2}"
format3.format("Dai", 25, 1.7)
import sqlite3
def factorial(N):
    return N * factorial(N-1)
def fact(N):
    if N <= 1:
        return 1
    else:
        return N * fact(N-1)

fact(5)
