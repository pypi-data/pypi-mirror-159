"""Lorem Ipsum implementation in Python"""
from __future__ import annotations


class Vocabulary:
  """This class provides access to the words used."""

  @staticmethod
  def getWords() -> list[str]:
    """Returns a list of normal words"""
    return [
      'exercitationem', 'perferendis', 'perspiciatis', 'laborum', 'eveniet',
      'sunt', 'iure', 'nam', 'nobis', 'eum', 'cum', 'officiis', 'excepturi',
      'odio', 'consectetur', 'quasi', 'aut', 'quisquam', 'vel', 'eligendi',
      'itaque', 'non', 'odit', 'tempore', 'quaerat', 'dignissimos',
      'facilis', 'neque', 'nihil', 'expedita', 'vitae', 'vero', 'ipsum',
      'nisi', 'animi', 'cumque', 'pariatur', 'velit', 'modi', 'natus',
      'iusto', 'eaque', 'sequi', 'illo', 'sed', 'ex', 'et', 'voluptatibus',
      'tempora', 'veritatis', 'ratione', 'assumenda', 'incidunt', 'nostrum',
      'placeat', 'aliquid', 'fuga', 'provident', 'praesentium', 'rem',
      'necessitatibus', 'suscipit', 'adipisci', 'quidem', 'possimus',
      'voluptas', 'debitis', 'sint', 'accusantium', 'unde', 'sapiente',
      'voluptate', 'qui', 'aspernatur', 'laudantium', 'soluta', 'amet',
      'quo', 'aliquam', 'saepe', 'culpa', 'libero', 'ipsa', 'dicta',
      'reiciendis', 'nesciunt', 'doloribus', 'autem', 'impedit', 'minima',
      'maiores', 'repudiandae', 'ipsam', 'obcaecati', 'ullam', 'enim',
      'totam', 'delectus', 'ducimus', 'quis', 'voluptates', 'dolores',
      'molestiae', 'harum', 'dolorem', 'quia', 'voluptatem', 'molestias',
      'magni', 'distinctio', 'omnis', 'illum', 'dolorum', 'voluptatum', 'ea',
      'quas', 'quam', 'corporis', 'quae', 'blanditiis', 'atque', 'deserunt',
      'laboriosam', 'earum', 'consequuntur', 'hic', 'cupiditate',
      'quibusdam', 'accusamus', 'ut', 'rerum', 'error', 'minus', 'eius',
      'ab', 'ad', 'nemo', 'fugit', 'officia', 'at', 'in', 'id', 'quos',
      'reprehenderit', 'numquam', 'iste', 'fugiat', 'sit', 'inventore',
      'beatae', 'repellendus', 'magnam', 'recusandae', 'quod', 'explicabo',
      'doloremque', 'aperiam', 'consequatur', 'asperiores', 'commodi',
      'optio', 'dolor', 'labore', 'temporibus', 'repellat', 'veniam',
      'architecto', 'est', 'esse', 'mollitia', 'nulla', 'a', 'similique',
      'eos', 'alias', 'dolore', 'tenetur', 'deleniti', 'porro', 'facere',
      'maxime', 'corrupti',
    ]

  @staticmethod
  def getCommonWords() -> list[str]:
    """Returns a list of common words"""
    return [
      'lorem', 'ipsum', 'dolor', 'sit', 'amet', 'consectetur',
      'adipisicing', 'elit', 'sed', 'do', 'eiusmod', 'tempor', 'incididunt',
      'ut', 'labore', 'et', 'dolore', 'magna', 'aliqua',
    ]
