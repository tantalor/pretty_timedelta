#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import timedelta, datetime
import unittest

import pretty_timedelta
from pretty_timedelta import\
  pretty_timedelta as ptd,\
  pretty_datetime_from_now as pdt,\
  translate


# shortcuts
def d(n): return timedelta(n)
def h(n): return timedelta(0, 0, 0, 0, 0, n)
def m(n): return timedelta(0, 0, 0, 0, n)
def s(n): return timedelta(0, n)


class TestEnglish(unittest.TestCase):
  
  def setUp(self):
    translate('en')
  
  def testCenturies(self):
    """Centuries in English."""
    self.assertEquals(ptd(d(36524)), "in 99 years")
    self.assertEquals(ptd(d(36525)), "in 1 century")
    self.assertEquals(ptd(d(-36525)), "1 century ago")
    self.assertEquals(ptd(d(73049)), "in 2 centuries")
    self.assertEquals(ptd(d(-73049)), "2 centuries ago")
    
  def testYears(self):
    """Years in English."""
    self.assertEquals(ptd(d(365)), "in 11 months")
    self.assertEquals(ptd(d(366)), "in 1 year")
    self.assertEquals(ptd(d(-366)), "1 year ago")
    self.assertEquals(ptd(d(4000)), "in 10 years")
    self.assertEquals(ptd(d(-4000)), "10 years ago")
    self.assertEquals(ptd(d(36524)), "in 99 years")
    self.assertEquals(ptd(d(-36524)), "99 years ago")
    self.assertEquals(ptd(d(36525)), "in 1 century")
  
  def testMonths(self):
    """Months in English."""
    self.assertEquals(ptd(d(30)), "in 30 days")
    self.assertEquals(ptd(d(31)), "in 1 month")
    self.assertEquals(ptd(d(-31)), "1 month ago")
    self.assertEquals(ptd(d(300)), "in 9 months")
    self.assertEquals(ptd(d(-300)), "9 months ago")
    self.assertEquals(ptd(d(365)), "in 11 months")
    self.assertEquals(ptd(d(-365)), "11 months ago")
    self.assertEquals(ptd(d(366)), "in 1 year")
    
  def testDays(self):
    """Days in English."""
    self.assertEquals(ptd(d(1)), "in 1 day")
    self.assertEquals(ptd(d(2)), "in 2 days")
    self.assertEquals(ptd(d(-1)), "1 day ago")
    self.assertEquals(ptd(d(-2)), "2 days ago")
    
  def testHours(self):
    """Hours in English."""
    self.assertEquals(ptd(h(1)), "in 1 hour")
    self.assertEquals(ptd(h(2)), "in 2 hours")
    self.assertEquals(ptd(h(-1)), "1 hour ago")
    self.assertEquals(ptd(h(-2)), "2 hours ago")
    
  def testMinutes(self):
    """Minutes in English."""
    self.assertEquals(ptd(m(1)), "in 1 minute")
    self.assertEquals(ptd(m(2)), "in 2 minutes")
    self.assertEquals(ptd(m(-1)), "1 minute ago")
    self.assertEquals(ptd(m(-2)), "2 minutes ago")
    
  def testSeconds(self):
    """Seconds in English."""
    self.assertEquals(ptd(s(1)), "in 1 second")
    self.assertEquals(ptd(s(2)), "in 2 seconds")
    self.assertEquals(ptd(s(-1)), "1 second ago")
    self.assertEquals(ptd(s(-2)), "2 seconds ago")
    
  def testJustNow(self):
    """Now in English."""
    self.assertEquals(ptd(d(0)), "just now")


class TestDatetimeFromNow(unittest.TestCase):
  
  def setUp(self):
    translate('en')
    self.now = datetime.now()
    class MockDatetime:
      @staticmethod
      def now():
        return self.now
    pretty_timedelta.datetime = MockDatetime
  
  def tearDown(self):
    pretty_timedelta.datetime = datetime

  def testGeneric(self):
    """Generic datetime from now."""
    for n in range(-2, 3): # [-2, 2]
      for f in (d, h, m, s):
        td = f(n)
        dt = self.now + td
        self.assertEquals(pdt(dt), ptd(td))
  
  def testSpecificDatetime(self):
    """Specific datetime from now."""
    self.assertEquals(pdt(self.now+timedelta(5)), "in 5 days")
    self.assertEquals(pdt(self.now-timedelta(5)), "5 days ago")
    

class TestSpanish(unittest.TestCase):
  
  def setUp(self):
    translate('es')
  
  def testCenturies(self):
    """Centuries in Spanish."""
    self.assertEquals(ptd(d(36524)), u"en 99 años")
    self.assertEquals(ptd(d(36525)), "en 1 siglo")
    self.assertEquals(ptd(d(-36525)), "hace 1 siglo")
    self.assertEquals(ptd(d(73049)), "en 2 siglos")
    self.assertEquals(ptd(d(-73049)), "hace 2 siglos")
    
  def testYears(self):
    """Years en Spanish."""
    self.assertEquals(ptd(d(365)), "en 11 meses")
    self.assertEquals(ptd(d(366)), u"en 1 año")
    self.assertEquals(ptd(d(-366)), u"hace 1 año")
    self.assertEquals(ptd(d(4000)), u"en 10 años")
    self.assertEquals(ptd(d(-4000)), u"hace 10 años")
    self.assertEquals(ptd(d(36524)), u"en 99 años")
    self.assertEquals(ptd(d(-36524)), u"hace 99 años")
    self.assertEquals(ptd(d(36525)), "en 1 siglo")
  
  def testMonths(self):
    """Months en Spanish."""
    self.assertEquals(ptd(d(30)), u"en 30 días")
    self.assertEquals(ptd(d(31)), "en 1 mes")
    self.assertEquals(ptd(d(-31)), "hace 1 mes")
    self.assertEquals(ptd(d(300)), "en 9 meses")
    self.assertEquals(ptd(d(-300)), "hace 9 meses")
    self.assertEquals(ptd(d(365)), "en 11 meses")
    self.assertEquals(ptd(d(-365)), "hace 11 meses")
    self.assertEquals(ptd(d(366)), u"en 1 año")
    
  def testDays(self):
    """Days in Spanish."""
    self.assertEquals(ptd(d(1)), u"en 1 día")
    self.assertEquals(ptd(d(2)), u"en 2 días")
    self.assertEquals(ptd(d(-1)), u"hace 1 día")
    self.assertEquals(ptd(d(-2)), u"hace 2 días")
    
  def testHours(self):
    """Hours in Spanish."""
    self.assertEquals(ptd(h(1)), "en 1 hora")
    self.assertEquals(ptd(h(2)), "en 2 horas")
    self.assertEquals(ptd(h(-1)), "hace 1 hora")
    self.assertEquals(ptd(h(-2)), "hace 2 horas")
    
  def testMinutes(self):
    """Minutes in Spanish."""
    self.assertEquals(ptd(m(1)), "en 1 minuto")
    self.assertEquals(ptd(m(2)), "en 2 minutos")
    self.assertEquals(ptd(m(-1)), "hace 1 minuto")
    self.assertEquals(ptd(m(-2)), "hace 2 minutos")
    
  def testSeconds(self):
    """Seconds in Spanish."""
    self.assertEquals(ptd(s(1)), "en 1 segundo")
    self.assertEquals(ptd(s(2)), "en 2 segundos")
    self.assertEquals(ptd(s(-1)), "hace 1 segundo")
    self.assertEquals(ptd(s(-2)), "hace 2 segundos")
    
  def testJustNow(self):
    """Now in Spanish."""
    self.assertEquals(ptd(d(0)), "ahorita")
    

if __name__ == '__main__':
  unittest.main()
