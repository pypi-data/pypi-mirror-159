"""The sentence class creates sentences of total length"""
from __future__ import annotations

from random import choice
from random import choices

from icecream import ic

from loremify import Vocabulary

ic.configureOutput(includeContext=True)


class Sentence:
  """The static methods"""

  @staticmethod
  def wordLen(words: list[str], n: int) -> list[[int, str]]:
    """Given a list of words and an integer, this method returns a list of
    words from the list that has length equal to the integer"""
    words = [word for word in words if word.find(',') < 0]
    words = [word for word in words if word.find('.') < 0]
    words = [word for word in words if word.lower() == word]
    if n < 0:
      return words
    out = [word for word in enumerate(words) if len(word) == n]
    if out:
      return out
    return Sentence.wordLen(words, n - 1)

  @staticmethod
  def adjLen(
    target: list[str],
    source: list[str], d: int = None) -> list[
    str]:
    """Replaces a word in target with a word from source one char shorter."""
    targetN = max([len(word) for word in Sentence.wordLen(target, -1)])
    sourceN = max([len(word) for word in Sentence.wordLen(source, -1)])
    removeWords = []
    insertWords = []
    while not (removeWords and insertWords):
      removeWords = Sentence.wordLen(target, targetN)
      insertWords = Sentence.wordLen(source, sourceN + d)
      targetN -= 1
      sourceN -= 1
    if not (removeWords and insertWords):
      raise ValueError()
    removeWord = choice(removeWords)
    insertWord = choice(insertWords)
    inds = [i for (i, word) in enumerate(target) if word == removeWord[1]]
    target[choice(inds)] = insertWord[1]
    return target

  @staticmethod
  def collectWords():
    """Collects words from the vocabulary"""
    return Vocabulary.getWords() + Vocabulary.getCommonWords() * 9

  @staticmethod
  def atLen(n: int = None) -> str:
    """The strength length is the length of each word increased by 1.
    The expected number of characters between each comma."""
    nCommas = n // 50
    n -= nCommas
    out = []
    words = Sentence.collectWords()
    while sum([len(word) + 1 for word in out]) < n:
      out.append(choice(words))

    while sum([len(word) + 1 for word in out]) > n:
      out = Sentence.adjLen(out, words, -1)

    lots = [i for (i, word) in enumerate(out)]
    for i in range(nCommas):
      ind = choice(lots)
      lots = [i for i in lots if i != ind]
      out[ind] = '%s,' % (out[ind])
    endChars = ['.', '!', '?']
    weights_ = [10, 1, 2]
    out = '%s%s' % (' '.join(out), choices(endChars, weights=weights_, )[0])
    return '%s%s' % (out[0].upper(), out[1:])
