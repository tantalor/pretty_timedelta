from datetime import timedelta
from gettext import translation


def translate(*languages):
  translation(
    fallback=1,
    languages=languages or None,
    domain='pretty_timedelta',
    localedir='locale/',
  ).install()

# install the translation (defaults to English)
# e.g., export LC_MESSAGES=es
translate()


def pretty_timedelta(td, with_ago=True):
  days = td.days
  seconds = td.seconds
  hours, seconds = divmod(seconds, 3600)
  minutes, seconds = divmod(seconds, 60)
  if days > 0:
    if days == 1:
      ret = _("1 day")
    else:
      ret = _("%s days") % days
  elif hours > 0:
    if hours == 1:
      ret = _("1 hour")
    else:
      ret = _("%s hours") % hours
  elif minutes > 0:
    if minutes == 1:
      ret = _("1 minute")
    else:
      ret = _("%s minutes") % minutes
  elif seconds > 0:
    if seconds == 1:
      ret = _("1 second")
    else:
      ret = _("%s seconds") % seconds
  else:
    ret = None
  if ret:
    if with_ago:
      return _("%s ago") % ret
    else:
      return ret
  else:
    return _("just now")


def main():
  import sys
  if not len(sys.argv) > 1:
    print "usage: %s [days [seconds [microseconds [milliseconds [minutes [hours [weeks]]]]]]]" % sys.argv[0]
  else:
    td = timedelta(*[int(s) for s in sys.argv[1:]])
    print pretty_timedelta(td)


if __name__ == '__main__':
  main()
