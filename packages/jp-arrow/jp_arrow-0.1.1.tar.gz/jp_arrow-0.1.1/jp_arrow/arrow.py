import calendar
import sys
from datetime import date
from datetime import datetime as dt_datetime
from datetime import time as dt_time
from datetime import timedelta
from datetime import tzinfo as dt_tzinfo
from math import trunc
from time import struct_time
from typing import (
    Any,
    ClassVar,
    Generator,
    Iterable,
    List,
    Mapping,
    Optional,
    Tuple,
    Union,
    cast,
    overload,
)

from dateutil import tz as dateutil_tz
from dateutil.relativedelta import relativedelta

import arrow
from arrow import locales, parser, util
from arrow.constants import DEFAULT_LOCALE, DEHUMANIZE_LOCALES
from arrow.locales import TimeFrameLiteral
from .formatter import DateTimeFormatter

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Final, Literal
else:
    from typing import Final, Literal  # pragma: no cover


class Arrow(arrow.arrow.Arrow):

    # string output and formatting

    def format(
        self, fmt: str = "YYYY-MM-DD HH:mm:ssZZ", locale: str = DEFAULT_LOCALE
    ) -> str:
        """Returns a string representation of the :class:`Arrow <arrow.arrow.Arrow>` object,
        formatted according to the provided format string.

        :param fmt: the format string.
        :param locale: the locale to format.

        Usage::

            >>> arrow.utcnow().format('EEYYYY-MM-DD HH:mm:ss ZZ')
            '令和03-07-14 23:19:22 +00:00'

            >>> arrow.utcnow().format('EYYYY-MM-DD HH:mm:ss ZZ')
            'R03-07-14 23:19:30 +00:00'

            >>> arrow.utcnow().format('EYY.M.D HH:mm:ss ZZ')
            'R3.7.14 23:19:40 +00:00'

            >>> arrow.utcnow().format('X')
            '1657840647.0'

            >>> arrow.utcnow().format('MMMM DD, YYYY')
            'July 14, 2022'

            >>> arrow.utcnow().format()
            '2022-07-14 23:25:47+00:00'

        """

        return DateTimeFormatter(locale).format(self._datetime, fmt)

    def __format__(self, formatstr: str) -> str:

        if len(formatstr) > 0:
            return self.format(formatstr)

        return str(self)
