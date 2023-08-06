import re
from typing import (
    Any, Optional, Union, Final, Tuple, List, overload, Match
)
from datetime import tzinfo as dt_tzinfo
from decimal import Decimal
from datetime import date, datetime
from time import struct_time

import arrow
from arrow.arrow import TZ_EXPR, Arrow
from arrow.constants import DEFAULT_LOCALE
# import snoop

FORMAT_WAREKI: Final[str] = 'EEYYYY-MM-DD HH'
FORMAT_WAREKI_SHORT: Final[str] = 'EYY-MM-DD HH'

# Grok for Japanese Era.
ERA_MEIJI = r'明治|明|M'
ERA_TAISHO = r'大正|大|T'
ERA_SHOWA = r'昭和|昭|S'
ERA_HEISEI = r'|平成|平|H'
ERA_REIWA = r'令和|令|R'
ERA_PATTERN = (
      f'{ERA_MEIJI}|'
      f'{ERA_TAISHO}|'
      f'{ERA_SHOWA}|'
      f'{ERA_HEISEI}|'
      f'{ERA_REIWA}'
    )

JPDATE_PATTERN = (
    rf'(?P<ERA>{ERA_PATTERN})?'
    r'(?P<YEAR>[0-9]+)[\.年]'
    r'((?P<MONTH>[0-9]+)[\.月]?((?P<DAY>[0-9]+)[\.日]?)?)?'
    r'('
      r'((?P<AM>午前|AM|am)|(?P<PM>午後|PM|pm))?'
      r'(?P<HOUR>[0-9]+)[:時]'
      r'((?P<MINUTE>[0-9]+)[:分]((?P<SECOND>[0-9]+)[:秒])?)?'
    r')?'
)


class JpDate(object):
    def __init__(self, *args: Any):
        self.jpdate_pattern = re.compile(
                   rf'(?!.*{ERA_PATTERN}.*)?'
                   rf'{JPDATE_PATTERN}'
                   r'(.*)?'
                )
        self.__transtable = str.maketrans('０１２３４５６７８９：',
                                          '0123456789:')
        self.era_data = {
            'MEIJI': {
                'start_year': 1867,
                'end_year': 1912,
                'start_datetime': '1867-10-24T00:00:00+00:00',
                'end_datetime': '1912-07-20T23:59:59+00:00',
                'abbreviation': ['明治', '明', 'M' ],
                'pattern': r'(ERA_MEIJI)'
            },
            'TAISHO': {
                'start_year': 1912,
                'end_year': 1926,
                'start_datetime': '1912-07-30T00:00:00+00:00',
                'end_datetime': '1926-12-24T23:59:59+00:00',
                'abbreviation': ['大正', '大', 'T' ],
                'pattern': r'(ERA_TAISHO)'
            },
            'SHOWA': {
                'start_year': 1926,
                'end_year': 1989,
                'start_datetime': '1926-12-25T00:00:00+00:00',
                'end_datetime': '1989-01-07T23:59:59+00:00',
                'abbreviation': ['昭和', '昭', 'S' ],
                'pattern': r'(ERA_SHOW)'
            },
            'HEISEI': {
                'start_year': 1989,
                'end_year': 2019,
                'start_datetime': '1989-01-08T00:00:00+00:00',
                'end_datetime': '2019-04-30T23:59:59+00:00',
                'abbreviation': ['平成', '平', 'H' ],
                'pattern': r'(ERA_HEISEI)'
            },
            'REIWA': {
                'start_year': 2019,
                'end_year': 9999,
                'start_datetime': '2019-05-01T00:00:00+00:00',
                'end_datetime': '9999-12-31T23:59:59+00:00',
                'abbreviation': ['令和', '令', 'R' ],
                'pattern': r'(ERA_REIWA)'
            },
        }
        self.start_era = dict()
        for era in self.era_data.keys():
            for name in self.era_data[era]['abbreviation']:
                self.start_era[name] = \
                     self.era_data[era]['start_datetime']

        self.end_era = dict()
        for era in self.era_data.keys():
            for name in self.era_data[era]['abbreviation']:
                self.end_era[name] = \
                    self.era_data[era]['end_datetime']


    def normalize_datetime(self,
        date: str
        )-> str:
        date = ( str.strip(date)
                     .translate(self.__transtable)
                     .replace('元年', '01年') )
        return date

    def search(self, str_date: str)-> Match:
        str_date = self.normalize_datetime(str_date)
        return self.jpdate_pattern.search(str_date)
