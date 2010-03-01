#!/usr/bin/python

import sys
from datetime import timedelta

from pretty_timedelta import pretty_timedelta


def main():
  if not len(sys.argv) > 1:
    print "usage: %s [days [seconds [microseconds [milliseconds [minutes [hours [weeks]]]]]]]" % sys.argv[0]
  else:
    td = timedelta(*[int(s) for s in sys.argv[1:]])
    print pretty_timedelta(td).encode('utf8')


if __name__ == '__main__':
  main()
