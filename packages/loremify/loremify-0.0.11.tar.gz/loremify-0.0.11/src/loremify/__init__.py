"""Lorem Ipsum implementation in python"""
from __future__ import annotations

from ._words import Vocabulary
from ._sentence import Sentence
from ._paragraph import Paragraph


def lorem(n: int = None) -> str:
  """Main entry point"""
  n = 600 if n is None else n
  return Paragraph.atCharLen(n)
