"""This file provides the actual functions required for the lorem ipsum
implementation"""
from random import choice
from random import choices
from random import randint
from random import random

from icecream import ic

from src.loremify import WordFactory
from src.loremify._getword import AllWords
from src.loremify._math import sample

ic.configureOutput(includeContext=True)
getWord = WordFactory()
getAllWords = AllWords()

ic.configureOutput(includeContext=True)


def sentence(m: int = None, s: float = None) -> str:
  """Returns a sentence with m expected number of words at a variance of s"""
  m = 20 if m is None else m
  s = 3 if s is None else s
  words = getWord(sample(m, s), )
  for (i, word) in enumerate(words):
    if random() > 0.9 and i + 1 < len(words):
      words[i] += ','
  ender = choices(['.', '?', '!'], weights=[10, 2, 1], )[0]
  words[-1] = '%s%s' % (words[-1], ender)
  words[0] = '%s%s' % (words[0][0].upper(), words[0][1:].lower())
  return ' '.join(words)


def paragraph(n: int = None) -> str:
  """Creates a paragraph with a collection of sentences, such that the
  length of the string just exceeds n. Next, words a removed randomly
  until the length is shorter than n. Final adjustments are made by
  replacing words."""
  out = ''
  while len(out) < n:
    out += ' %s' % (sentence())
  while len(out) > n:
    out = popAnyWord(out)
  while len(out) < n:
    wLen = randint(3, 7)
    out = replaceWord(out, wLen, wLen + 1)
  if out[0] == ' ':
    out = out[1:]
  return polish(out)


def polish(msg: str) -> str:
  """Polishes the final outcome by removing newlines and multiple spaces."""
  out = msg
  while out.find('  ') > -1:
    out = out.replace('  ', ' ')
  while out.find('\n') > -1:
    out = out.replace('\n', ' ')
  return out


def containsAny(word: str, chars: list[str]) -> bool:
  """Returns True if any character in chars is contained in word"""
  return any([word.find(char) > -1 for char in chars])


def containsAll(word: str, chars: list[str]) -> bool:
  """Returns True if all characters in chars is contained in word"""
  return all([word.find(char) > -1 for char in chars])


def popAnyWord(msg: str) -> str:
  """Returns the provided string with a word removed."""
  spec = [',', '.', '!', '?']
  wL = msg.split(' ')
  inds = [i for (i, word) in enumerate(wL) if not containsAny(word, spec)]
  del wL[choice(inds)]
  return ' '.join(wL)


def replaceWord(msg: str, oldLen: int, newLen: int) -> str:
  """Replaces random word of length oldLen with a new word of length
  newLen. """
  wL = msg.split(' ')
  wordInds = [i for (i, word) in enumerate(wL) if len(word) == oldLen]
  if not wordInds:
    return msg
  ind = choice(wordInds)
  wL[ind] = choice(getAllWords(newLen))
  return ' '.join(wL)

#
# def mostCommonWordLength(msg: str) -> list[int]:
#   """Finds the most common word length of the provided string"""
#   wLens = [len(word) for word in msg.split(' ')]
#   maxLen = max(wLens)
#   minLen = min(wLens)
#   out = [0 for _ in range(maxLen)]
#   for i in range(maxLen + 1):
#     out[i] = sum([1 if i == len(word) else 0 for word in msg])
#   return out
