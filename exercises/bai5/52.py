import sys

if sys.platform.lower().find('linux') != -1:
    print('It is a linux based OS')
else:
    print('It is not a linux based OS')
