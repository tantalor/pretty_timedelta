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
  hours, seconds = divmod(seconds, 3600)
  minutes, seconds = divmod(seconds, 60)
  if days > 0:
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


def main():
  import sys
  if not len(sys.argv) > 1:
    print "usage: %s [days [seconds [microseconds [milliseconds [minutes [hours [weeks]]]]]]]" % sys.argv[0]
  else:
    td = timedelta(*[int(s) for s in sys.argv[1:]])
    print pretty_timedelta(td)


if __name__ == '__main__':
  main()
