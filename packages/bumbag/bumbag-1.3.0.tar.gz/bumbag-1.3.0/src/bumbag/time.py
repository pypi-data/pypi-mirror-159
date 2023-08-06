import calendar
import math
from datetime import date, datetime, timedelta

from dateutil import relativedelta
from toolz import curry

from bumbag.math import iseq


def str_to_date(string):
    """Cast an ISO date string to a date object.

    Parameters
    ----------
    string : str
        Date string in ISO 8601 format, YYYY-MM-DD.

    Returns
    -------
    datetime.date
        Date object.

    Examples
    --------
    >>> str_to_date("2022-01-01")
    datetime.date(2022, 1, 1)
    """
    return datetime.strptime(string, "%Y-%m-%d").date()


def date_to_str(input_date):
    """Cast a date object to an ISO date string.

    Parameters
    ----------
    input_date : datetime.date
        Date object to cast.

    Returns
    -------
    str
        Date string in ISO 8601 format, YYYY-MM-DD.

    Examples
    --------
    >>> from datetime import date
    >>> date_to_str(date(2022, 1, 1))
    '2022-01-01'
    """
    return input_date.isoformat()


def get_last_date_of_month(year, month):
    """Get last date of month.

    Parameters
    ----------
    year : int
        Year of date.
    month : int
        Month of date.

    Returns
    -------
    datetime.date
        Last date of month.

    Examples
    --------
    >>> get_last_date_of_month(2022, 1)
    datetime.date(2022, 1, 31)
    """
    _, number_days_in_month = calendar.monthrange(year, month)
    return date(year, month, number_days_in_month)


def is_leap_year(year):
    """Check if year is a leap year.

    Parameters
    ----------
    year : int
        Year to check.

    Returns
    -------
    bool
        Is leap year.

    Examples
    --------
    >>> is_leap_year(2000)
    True
    >>> is_leap_year(2001)
    False
    """
    return calendar.isleap(year)


def days_between_dates(date1, date2, include_last_date=False):
    """Compute the number of days between two dates.

    Parameters
    ----------
    date1 : datetime.date
        First date to compute the difference from.
    date2 : datetime.date
        Second date to compute the difference from.
    include_last_date : bool, default=False
        Specifies if the larger of the two dates should be excluded.

    Notes
    -----
    - ``date1 < date2`` or ``date2 < date1``: both return the same value.

    Returns
    -------
    int
        Number of days between two days.

    Examples
    --------
    >>> from datetime import date
    >>> days_between_dates(date(2022, 8, 1), date(2022, 8, 1))
    0
    >>> days_between_dates(date(2022, 8, 1), date(2022, 8, 1), True)
    1
    >>> days_between_dates(date(2022, 8, 1), date(2022, 8, 7))
    6
    >>> days_between_dates(date(2022, 8, 1), date(2022, 8, 7), True)
    7
    """
    start, end = (date1, date2) if date1 <= date2 else (date2, date1)
    return (end - start).days + 1 if include_last_date else (end - start).days


def daterange(start, end, exclude_start=False, exclude_end=False):
    """Get sequence of dates.

    Parameters
    ----------
    start : datetime.date
        Start of the date sequence.
    end : datetime.date
        End of the date sequence.
    exclude_start : bool, default=False
        Specifies if the start date of the sequence should be excluded.
    exclude_end : bool, default=False
        Specifies if the end date of the sequence should be excluded.

    Yields
    ------
    datetime.date
        A generator of consecutive dates from ``start`` to ``end``.

    Notes
    -----
    - If ``start == end``, only one element is generated.
    - If ``start > end``, start and end are swapped.

    Examples
    --------
    >>> from datetime import date
    >>> from toolz.curried import pipe, map
    >>> from bumbag.time import date_to_str
    >>> d1 = date(2022, 1, 1)
    >>> d2 = date(2022, 1, 3)
    >>> pipe(daterange(d1, d2), map(date_to_str), list)
    ['2022-01-01', '2022-01-02', '2022-01-03']
    """
    if start > end:
        start, end = end, start

    n_days = days_between_dates(start, end, include_last_date=True)
    for i in range(n_days):
        if (i == 0 and exclude_start) or ((i + 1) == n_days and exclude_end):
            continue
        yield start + timedelta(i)


@curry
def dseq(start, forward):
    """Generate a sequence of consecutive dates.

    Parameters
    ----------
    start : datetime.date
        Start of the sequence (inclusive).
    forward : bool
        Specifies if dates should be generated in a forward or backward manner.

    Yields
    ------
    datetime.date
        A generator of consecutive date objects.

    See Also
    --------
    bumbag.math.iseq : A generator of consecutive integers.

    Notes
    -----
    Function is curried.

    Examples
    --------
    >>> from datetime import date
    >>> from toolz.curried import pipe, take, map
    >>> from bumbag.time import date_to_str
    >>> seed = dseq(date(2022, 1, 1))
    >>> pipe(seed(forward=True), map(date_to_str), take(3), list)
    ['2022-01-01', '2022-01-02', '2022-01-03']
    >>> pipe(seed(forward=False), map(date_to_str), take(3), list)
    ['2022-01-01', '2021-12-31', '2021-12-30']
    """
    for i in iseq(0):
        yield start + timedelta(i) if forward else start - timedelta(i)


def datedelta(reference, days):
    """Compute date relative to reference date in terms of number of days.

    The reference and relative dates are the (inclusive) endpoints of
    a sequence of consecutive dates, where the ``days`` argument corresponds
    to the actual number of days between the dates. As a result, the reference
    date and relative date can directly be used in a BETWEEN statement of
    a SQL query.

    Parameters
    ----------
    reference : datetime.date
        The reference date.
    days : int
        Size of the delta expressed in number of days:
         - If ``days == 0``, returns the reference date.
         - If ``days > 0``, returns date ahead w.r.t. the reference date.
         - If ``days < 0``, returns date ago w.r.t. the reference date.
        The value of ``days`` equals the length of the corrsponding sequence of
        consecutive dates with inclusive endpoints.

    Returns
    -------
    datetime.date
        Relative date.

    Examples
    --------
    >>> from datetime import date
    >>> datedelta(date(2022, 1, 1), 0)
    datetime.date(2022, 1, 1)
    >>> datedelta(date(2022, 1, 1), 3)
    datetime.date(2022, 1, 3)
    >>> datedelta(date(2022, 1, 1), -3)
    datetime.date(2021, 12, 30)
    """
    relative_date = reference + timedelta(days=days)
    return (
        relative_date
        if days == 0
        else relative_date - timedelta(days=1)
        if days > 0
        else relative_date + timedelta(days=1)
    )


def months_between_dates(date1, date2, include_last_date=False):
    """Compute the number of months between two dates.

    Parameters
    ----------
    date1 : datetime.date
        First date to compute the difference from.
    date2 : datetime.date
        Second date to compute the difference from.
    include_last_date : bool, default=False
        Specifies if the larger of the two dates should be excluded.

    Notes
    -----
    - ``date1 < date2`` or ``date2 < date1``: both return the same value.

    Returns
    -------
    int
        Number of months between two days.

    Examples
    --------
    >>> from datetime import date
    >>> months_between_dates(date(2022, 1, 1), date(2022, 1, 1))
    0
    >>> months_between_dates(date(2022, 1, 1), date(2022, 1, 1), True)
    1
    >>> months_between_dates(date(2022, 1, 1), date(2022, 8, 31))
    7
    >>> months_between_dates(date(2022, 1, 1), date(2022, 8, 1), True)
    8
    """
    start, end = (date1, date2) if date1 <= date2 else (date2, date1)
    difference = relativedelta.relativedelta(end, start)
    n_months = difference.months + 12 * difference.years
    return n_months + 1 if include_last_date else n_months


def monthrange(start, end, exclude_start=False, exclude_end=False):
    """Get sequence of months.

    Parameters
    ----------
    start : datetime.date
        Start of the month sequence.
    end : datetime.date
        End of the month sequence.
    exclude_start : bool, default=False
        Specifies if the start month of the sequence should be excluded.
    exclude_end : bool, default=False
        Specifies if the end month of the sequence should be excluded.

    Yields
    ------
    datetime.date
        A generator of consecutive months from ``start`` to ``end``.

    Notes
    -----
    - If ``start == end``, only one element is generated.
    - If ``start > end``, start and end are swapped.

    Examples
    --------
    >>> from datetime import date
    >>> from toolz.curried import pipe, map
    >>> from bumbag.time import date_to_str
    >>> d1 = date(2022, 1, 1)
    >>> d2 = date(2022, 4, 30)
    >>> pipe(monthrange(d1, d2), map(date_to_str), list)
    ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01']
    >>> d1 = date(2022, 1, 31)
    >>> d2 = date(2022, 4, 30)
    >>> pipe(monthrange(d1, d2), map(date_to_str), list)
    ['2022-01-31', '2022-02-28', '2022-03-31', '2022-04-30']
    """
    if start > end:
        start, end = end, start

    n_months = months_between_dates(start, end, include_last_date=True)
    for i in range(n_months):
        if (i == 0 and exclude_start) or ((i + 1) == n_months and exclude_end):
            continue
        yield start + relativedelta.relativedelta(months=i)


@curry
def mseq(start, forward):
    """Generate a sequence of consecutive months.

    Parameters
    ----------
    start : datetime.date
        Start of the sequence (inclusive).
    forward : bool
        Specifies if months should be generated in a forward or backward
        manner.

    Yields
    ------
    datetime.date
        A generator of consecutive months.

    See Also
    --------
    bumbag.math.iseq : A generator of consecutive integers.

    Notes
    -----
    Function is curried.

    Examples
    --------
    >>> from datetime import date
    >>> from toolz.curried import pipe, take, map
    >>> from bumbag.time import date_to_str
    >>> seed = mseq(date(2022, 1, 1))
    >>> pipe(seed(forward=True), map(date_to_str), take(4), list)
    ['2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01']
    >>> pipe(seed(forward=False), map(date_to_str), take(4), list)
    ['2022-01-01', '2021-12-01', '2021-11-01', '2021-10-01']
    """
    for i in iseq(0):
        yield (
            start + relativedelta.relativedelta(months=i)
            if forward
            else start - relativedelta.relativedelta(months=i)
        )


def humantime(seconds):
    """Convert seconds to human-readable time.

    Parameters
    ----------
    seconds : int, float
        Seconds to convert.

    Returns
    -------
    str
        Human-readable time.

    Raises
    ------
    ValueError
        If ``seconds`` is not a positive integer.

    Examples
    --------
    >>> humantime(1)
    '1 second'
    >>> humantime(2)
    '2 seconds'
    >>> humantime(60)
    '1 minute'
    >>> humantime(120)
    '2 minutes'
    >>> humantime(60 * 60 * 24 + 123456)
    '2 days, 10 hours, 17 minutes'
    """
    if seconds < 0:
        raise ValueError(f"seconds={seconds} - must be a non-negative number")

    if math.isclose(seconds, 0):
        return "0 seconds"

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)

    def multiplier(time_with_unit: str) -> str:
        time_without_unit = float(time_with_unit.split(" ")[0])
        return (
            time_with_unit
            if math.isclose(time_without_unit, 1)
            else f"{time_with_unit}s"
        )

    result = []
    if days:
        result.append(multiplier(f"{int(days)} day"))

    if hours:
        result.append(multiplier(f"{int(hours)} hour"))

    if minutes:
        result.append(multiplier(f"{int(minutes)} minute"))

    if seconds and minutes < 2:
        if math.isclose(seconds, int(seconds)):
            result.append(multiplier(f"{int(seconds)} second"))
        else:
            result.append(f"{seconds:0.6f} seconds")

    return ", ".join(result)
