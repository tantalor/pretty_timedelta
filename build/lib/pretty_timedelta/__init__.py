from datetime import timedelta, datetime
import gettext
from gettext import translation
from os import path


def translate(*languages):
  localedir = path.join(path.dirname(__file__), 'locale')
  t = translation(
    fallback=1,
    languages=languages or None,
    domain='pretty_timedelta',
    localedir=localedir,
  )
  # install
  global _
  _ = t.ugettext

# install the translation (defaults to English)
# e.g., export LC_MESSAGES=es
translate()


# source: http://google.com
__SECONDS_PER_YEAR__ = 31556926
__SECONDS_PER_DAY__ = 86400
__SECONDS_PER_HOUR__ = 3600
__SECONDS_PER_MINUTE__ = 60
__MONTHS_PER_YEAR__ = 12
__YEARS_PER_CENTURY__ = 100

def pretty_timedelta(td):
  """Returns a pretty string for timedeltas, e.g., 5 minutes ago."""
  tp = time_part(td)
  if tp:
    if td > timedelta(0):
      return _("in %s") % tp
    else:
      return _("%s ago") % tp
  else:
    return _("just now")


def pretty_datetime_from_now(dt):
  """Returns a pretty string for datetimes relative to now."""
  return pretty_timedelta(dt - datetime.now())


def time_part(td):
  td = abs(td)
  days = td.days
  seconds = td.seconds
  total_seconds = days * __SECONDS_PER_DAY__ + seconds
  hours, seconds = divmod(seconds, __SECONDS_PER_HOUR__)
  minutes, seconds = divmod(seconds, __SECONDS_PER_MINUTE__)
  if total_seconds >= __SECONDS_PER_YEAR__:
    years = total_seconds / __SECONDS_PER_YEAR__
    if years >= __YEARS_PER_CENTURY__:
      centuries = years / __YEARS_PER_CENTURY__
      if centuries == 1:
        return _("1 century")
      else:
        return _("%s centuries") % centuries
    elif years == 1:
      return _("1 year")
    else:
      return _("%s years") % years
  elif total_seconds * __MONTHS_PER_YEAR__ >= __SECONDS_PER_YEAR__:
    months = total_seconds * __MONTHS_PER_YEAR__ / __SECONDS_PER_YEAR__
    if months == 1:
      return _("1 month")
    else:
      return _("%s months") % months
  elif days > 0:
    if days == 1:
      return _("1 day")
    else:
      return _("%s days") % days
  elif hours > 0:
    if hours == 1:
      return _("1 hour")
    else:
      return _("%s hours") % hours
  elif minutes > 0:
    if minutes == 1:
      return _("1 minute")
    else:
      return _("%s minutes") % minutes
  elif seconds > 0:
    if seconds == 1:
      return _("1 second")
    else:
      return _("%s seconds") % seconds
