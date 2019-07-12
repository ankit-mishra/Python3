'''
Python Regular Expressions

Regular expressions are a powerful language for matching text patterns.
The Python "re" module provides regular expression support.

In Python a regular expression search is typically written as:
  match = re.search(pat, str)

The re.search() method takes a regular expression pattern and a string and searches for that pattern within the string.
If the search is successful, search() returns a match object or None otherwise.
Therefore, the search is usually immediately followed by an if-statement to test if the search succeeded,
 as shown in the following example which searches for the pattern 'word:' followed by a 3 letter word (details below):
'''
import re

str = 'an example word:cat!!'
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')

'''

The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without change
which is very handy for regular expressions .
I recommend that you always write pattern strings with the 'r' just as a habit.

Basic Patterns
The power of regular expressions is that they can specify patterns, not just fixed characters. Here are the most basic patterns which match single chars:

a, X, 9, < -- ordinary characters just match themselves exactly. The meta-characters which do not match themselves because they have special meanings are: . ^ $ * + ? { [ ] \ | ( ) (details below)
. (a period) -- matches any single character except newline '\n'
\w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]. Note that although "word" is the mnemonic for this, it only matches a single word char, not a whole word. \W (upper case W) matches any non-word character.
\b -- boundary between word and non-word
\s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form [ \n\r\t\f]. \S (upper case S) matches any non-whitespace character.
\t, \n, \r -- tab, newline, return
\d -- decimal digit [0-9] (some older regex utilities do not support but \d, but they all support \w and \s)
^ = start, $ = end -- match the start or end of the string
\ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash. If you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to make sure it is treated just as a character.
'''
#The basic rules of regular expression search for a pattern within a string are:

'''
The search proceeds through the string from start to end, stopping at the first match found
All of the pattern must be matched, but not all of the string
If match = re.search(pat, str) is successful, match is not None and in particular match.group() is the matching text
'''
## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
if match:
  print('found', match.group())

match = re.search(r'igs', 'piiig') # not found, match == None
if match:
  print('found', match.group())

## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"
if match:
  print('found', match.group())

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
if match:
  print('found', match.group())

match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"
if match:
  print('found', match.group())


### Repetition Examples
## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"
if match:
  print('found', match.group())

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"
if match:
  print('found', match.group())

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
if match:
  print('found', match.group())

match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
if match:
  print('found', match.group())

match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"
if match:
  print('found', match.group())

## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar') # not found, match == None
if match:
  print('found', match.group())

## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"
if match:
  print('found', match.group())