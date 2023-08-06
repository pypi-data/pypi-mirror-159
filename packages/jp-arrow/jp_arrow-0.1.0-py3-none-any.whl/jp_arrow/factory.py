"""
Implements the :class:`ArrowFactory <jp_arrow.factory.ArrowFactory>` class,
providing factory methods for common :class:`Arrow <jp_arrow.arrow.Arrow>`
construction scenarios.

"""

import calendar
from datetime import date, datetime
from datetime import tzinfo as dt_tzinfo
from decimal import Decimal
from time import struct_time
from typing import Any, List, Optional, Tuple, Type, Union, overload

from dateutil import tz as dateutil_tz

import arrow
from arrow.arrow import TZ_EXPR
from arrow.constants import DEFAULT_LOCALE
from arrow.util import is_timestamp, iso_to_gregorian
from .arrow import Arrow
from .jp_date import JpDate


class ArrowFactory(arrow.factory.ArrowFactory):
    """A factory for generating :class:`Arrow <arrow.arrow.Arrow>` objects.

    :param type: (optional) the :class:`Arrow <arrow.arrow.Arrow>`-based class to construct from.
        Defaults to :class:`Arrow <arrow.arrow.Arrow>`.

    """

    type: Type[Arrow]

    def __init__(self, type: Type[Arrow] = Arrow) -> None:
        self.type = type
        self.jpdate = JpDate()
        self.get_docs = super().get.__doc__

    @overload
    def get(
        self,
        *,
        locale: str = DEFAULT_LOCALE,
        tzinfo: Optional[TZ_EXPR] = None,
        normalize_whitespace: bool = False,
    ) -> Arrow:
        ...  # pragma: no cover

    @overload
    def get(
        self,
        __obj: Union[
            Arrow,
            datetime,
            date,
            struct_time,
            dt_tzinfo,
            int,
            float,
            str,
            Tuple[int, int, int],
        ],
        *,
        locale: str = DEFAULT_LOCALE,
        tzinfo: Optional[TZ_EXPR] = None,
        normalize_whitespace: bool = False,
    ) -> Arrow:
        ...  # pragma: no cover

    @overload
    def get(
        self,
        __arg1: Union[datetime, date],
        __arg2: TZ_EXPR,
        *,
        locale: str = DEFAULT_LOCALE,
        tzinfo: Optional[TZ_EXPR] = None,
        normalize_whitespace: bool = False,
    ) -> Arrow:
        ...  # pragma: no cover

    @overload
    def get(
        self,
        __arg1: str,
        __arg2: Union[str, List[str]],
        *,
        locale: str = DEFAULT_LOCALE,
        tzinfo: Optional[TZ_EXPR] = None,
        normalize_whitespace: bool = False,
    ) -> Arrow:
        ...  # pragma: no cover

    def get(self, *args: Any, **kwargs: Any) -> Arrow:
        """
        **One** Japanes ERA-formatted ``str``, to parse it::

            >>> arrow.get('令和03年09月29日 01:26:43')
            <Arrow [2022-09-29T01:26:43+00:00]>

            >>> arrow.get('R03.09.29. 01:26:43')
            <Arrow [2022-09-29T01:26:43+00:00]>
        """
        arg_count = len(args)

        if arg_count != 1:
            return super().get( *args, **kwargs )
        else:
            __1st_arg = args[0]
            if not isinstance(__1st_arg, str):
                return super().get( *args, **kwargs )

        match = self.jpdate.search(__1st_arg)
        # snoop.pp(__1st_arg, JPDATE_PATTERN, match)
        if match:
            era = match.group('ERA')
            year = int(match.group('YEAR') or 0)
            month = int(match.group('MONTH') or 1)
            day = int(match.group('DAY') or 1)
            am = match.group('AM')
            pm = match.group('PM')
            hour = int(match.group('HOUR') or 0)
            if pm:
                hour = hour + 12
            minute = int(match.group('MINUTE') or 0)
            second = int(match.group('SECOND') or 0)
            # snoop.pp(era, year, month, day, hour, minute, second)
            if era in self.jpdate.start_era:
                # snoop.pp(era)
                start_datetime  = self.jpdate.start_era[era]
                # snoop.pp(start_datetime)
                start_era = super().get(start_datetime)
                shift_year = int(year or 1)  -1
                year = start_era.shift(years=shift_year).year
                # snoop.pp(shift_year, year)
                return super().get(year, month, day,
                                   hour, minute, second)
            else:
                raise arrow.parser.ParserError(
                   f'Found Japanese datetime, but something wrong.'
                )
        else:
            return super().get( *args, **kwargs )
