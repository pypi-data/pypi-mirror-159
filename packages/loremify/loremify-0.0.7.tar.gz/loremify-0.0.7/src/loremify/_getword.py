"""The getWord function defined here in returns a list of words selected
between the words and common words defined in the two wordlist files. """
from random import choices

from src.loremify._words import commonWords
from src.loremify._words import words


class WordFactory:
  """The factory creates the callable"""

  @staticmethod
  def noSpace(msg: str) -> str:
    """Removes all spaces from string"""
    for erase in [' ', '\n', '\r', '\r\n']:
      while msg.find(erase) > -1:
        msg = msg.replace(erase, '')
    return msg

  def __init__(self):
    self.words = None
    self.commonWords = None
    self._loadWords()

  def _loadWords(self):
    """This method actually loads the words. Can be invoked exactly once."""
    self.commonWords = [
      self.noSpace(word) for word in commonWords if word]
    self.words = [self.noSpace(word) for word in words if word]

  def __call__(self, n: int = None, f: int = None):
    """This method returns a list of length n sampled from the words with
    common words given weight f."""
    n = 1 if n is None else n
    f = 10 if f is None else f
    c, w = self.commonWords, self.words
    return choices(c + w, [f for _ in c] + [1 for _ in w], k=n)


class AllWords(WordFactory):
  """AllWords reimplements __call__ to return all words"""

  def __init__(self):
    WordFactory.__init__(self)

  def __call__(self, n: int = None, *_):
    """Reimplementation simply returning all words of length n, or all
    words if n is smaller than 1 (default)"""
    n = 0 if n is None else n
    if n > 0:
      return [w for w in self.commonWords + self.words if len(w) == n]
    return self.commonWords + self.words
