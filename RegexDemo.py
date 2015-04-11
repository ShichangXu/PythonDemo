__author__ = 'xsc'
import re

'''
re.match(pattern, string, flags=0)
If zero or more characters at the beginning of string match the regular expression pattern, return a corresponding MatchObject instance.
 Return None if the string does not match the pattern; note that this is different from a zero-length match.
Note that even in MULTILINE mode, re.match() will only match at the beginning of the string and not at the beginning of each line.
If you want to locate a match anywhere in string, use search() instead (see also search() vs. match()).
'''
pattern = "is\d+"
match_string = "is450"
match_result = re.match(pattern, match_string)
if match_result is not None:
    print match_result.group()
