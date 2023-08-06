"""Creates a paragraph by concatenating sentences"""
from random import shuffle

from loremify import Sentence


class Paragraph:
  """Static methods"""

  @staticmethod
  def atCharLen(n_: int) -> str:
    """Creates a paragraph of length n containing s sentences."""
    S = []
    n = n_
    while n > 20:
      S.append(int(n * 0.6))
      n -= S[-1]
    S.append(n + 1)
    shuffle(S)
    out = [Sentence.atLen(s) for s in S]
    return ' '.join(out)
