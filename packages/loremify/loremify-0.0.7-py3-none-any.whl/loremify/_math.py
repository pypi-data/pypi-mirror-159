"""This module provides a few convenient math functions. These are not
optimized for performance, but for convenience."""
from __future__ import annotations

from random import random

pi = 3.14159265358979323846


def factorial(n: int) -> int:
  """Factorial function in the positive integers"""
  if n < 0:
    raise ValueError('Expected positive integer, but received %d' % (n))
  if n in [0, 1]:
    return 1
  out = 1
  for i in range(n):
    out *= (i + 1)
  return out


def erf(z: float) -> float:
  """Error function by Taylor expansion in the real numbers"""
  if z < 0:
    return -erf(-z)
  if z == 0:
    return 0
  out = 0
  for i in range(12):
    term = z ** (2 * i + 1) / factorial(i) / (2 * i + 1)
    out += (-term if i % 2 else term)
  return out


def invErf(z: float) -> float:
  """Inverse error function by Taylor expansion in the real numbers"""
  out = z + pi / 12 * z ** 3 + 7 / 480 * pi ** 2 * z ** 5
  out += 127 / 40320 * pi ** 3 * z ** 7 + 4369 / 5806080 * pi ** 4 * z ** 9
  return 34807 / 182476800 * pi ** 5 * z ** 11 + out


def invCDF(p: float, m: float = None, s: float = None) -> float:
  """Inverse Cumulative Distribution Function for normal distribution"""
  if p * p > 1:
    raise ValueError('Expected probability to be in unit range, '
                     'but received %.12f' % (p))
  m = 0 if m is None else m
  s = 1 if s is None else s
  return m + s * 2 ** 0.5 * invErf(2 * p - 1)


def sample(m: float = None, s: float = None, p: float = None) -> int:
  """Returns a single number sampled from the given mean and variance."""
  p = random() if p is None else p
  m = 0 if m is None else m
  s = 1 if s is None else s
  return max(int(invCDF(p, m, s)), 1)
