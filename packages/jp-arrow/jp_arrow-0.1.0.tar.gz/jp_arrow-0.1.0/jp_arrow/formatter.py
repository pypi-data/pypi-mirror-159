import sys
from typing import Optional, Pattern, cast

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Final
else:
    from typing import Final  # pragma: no cover

import re
from datetime import datetime
import arrow
from arrow.constants import DEFAULT_LOCALE
from .jp_date import JpDate


FORMAT_JISX0301: Final[str] = "EYY.M.D"
FORMAT_JISX0301_W: Final[str] = "EYYYY.MM.DD"
FORMAT_WAREKI: Final[str] = "EEYY年M月D日"
FORMAT_WAREKI_W: Final[str] = "EEYYYY年MM月DD日"

class DateTimeFormatter(arrow.formatter.DateTimeFormatter):
    _FORMAT_RE: Final[Pattern[str]] = re.compile(
        r"(\[(?:(?=(?P<literal>[^]]))(?P=literal))*\]|E?E?YYY?Y?|MM?M?M?|Do|DD?D?D?D?|d?dd?d?|HH?|hh?|mm?|ss?|SS?S?S?S?S?|ZZ?Z?|a|A|X|x|W)"
    )

    locale: arrow.locales.Locale

    def __init__(self, locale: str = DEFAULT_LOCALE) -> None:
        self.jpdate = JpDate()
        super().__init__(locale)

    def format(cls, dt: datetime, fmt: str) -> str:
        return cls._FORMAT_RE.sub(
            lambda m: cast(str, cls._format_token(dt, m.group(0))), fmt
        )

    def _format_token(self,
        dt: datetime,
        token: Optional[str]
        ) -> Optional[str]:

        if token and token.startswith("[") and token.endswith("]"):
            return token[1:-1]

        if token == "EEYYYY": # 令和01
            return self.jp_era_year(dt.year, padding=True, abbreviation=False)

        if token == "EEYY": # 令和1
            return self.jp_era_year(dt.year, padding=False, abbreviation=False)

        if token == "EYYYY": # R01
            return self.jp_era_year(dt.year, padding=True, abbreviation=True)

        if token == "EYY":  # R1
            return self.jp_era_year(dt.year, padding=False, abbreviation=True)

        if token in ("DDD", "DD", "D"):
            str_date = super()._format_token(dt, token)
            if "ja" in self.locale.names:
                str_date = f'{str_date}日'
            return str_date

        return super()._format_token(dt, token)

    def jp_era_year(self,
        year: int,
        padding: bool=True,
        abbreviation: bool=False,
        ) ->str:

        for era in self.jpdate.era_data:
            if ( self.jpdate.era_data[era]['start_year'] <= year
                 and year <= self.jpdate.era_data[era]['end_year'] ):
                year = year - self.jpdate.era_data[era]['start_year'] + 1
                break
        else:
            return year
            if padding:
                return f'{year:04d}'
            else:
                return f'{year:02d}'

        if abbreviation:
            str_era = f"{self.jpdate.era_data[era]['abbreviation'][2]}"
        else:
            str_era = f"{self.jpdate.era_data[era]['abbreviation'][0]}"
        if "ja" in self.locale.names:
            suffix = '年'
        else:
            suffix = ''
        if padding:
            str_year = f"{str_era}{year:02d}{suffix}"
        else:
            str_year =  f"{str_era}{year:d}{suffix}"

        return str_year
