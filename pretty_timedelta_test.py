# -*- coding: utf-8 -*-

from datetime import timedelta
import unittest

from pretty_timedelta import pretty_timedelta as ptd, translate


# shortcuts
def d(n): return timedelta(n)
def h(n): return timedelta(0, 0, 0, 0, 0, n)
def m(n): return timedelta(0, 0, 0, 0, n)
def s(n): return timedelta(0, n)


class TestPrettyTimedelta(unittest.TestCase):
  
  def setUp(self):
    translate('en')
    
  def testDays(self):
    self.assertEquals(ptd(d(1)), "1 day ago")
    self.assertEquals(ptd(d(2)), "2 days ago")
    
  def testHours(self):
    self.assertEquals(ptd(h(1)), "1 hour ago")
    self.assertEquals(ptd(h(2)), "2 hours ago")
    
  def testMinutes(self):
    self.assertEquals(ptd(m(1)), "1 minute ago")
    self.assertEquals(ptd(m(2)), "2 minutes ago")
    
  def testSeconds(self):
    self.assertEquals(ptd(s(1)), "1 second ago")
    self.assertEquals(ptd(s(2)), "2 seconds ago")
    
  def testJustNow(self):
    self.assertEquals(ptd(d(0)), "just now")
    
  def testWithoutAgo(self):
    self.assertEquals(ptd(d(1), with_ago=False), "1 day")
    

class TestSpanishPrettyTimedelta(unittest.TestCase):
  
  def setUp(self):
    translate('es')
    
  def testDays(self):
    self.assertEquals(ptd(d(1)), "hace 1 día")
    self.assertEquals(ptd(d(2)), "hace 2 días")
    
  def testHours(self):
    self.assertEquals(ptd(h(1)), "hace 1 hora")
    self.assertEquals(ptd(h(2)), "hace 2 horas")
    
  def testMinutes(self):
    self.assertEquals(ptd(m(1)), "hace 1 minuto")
    self.assertEquals(ptd(m(2)), "hace 2 minutos")
    
  def testSeconds(self):
    self.assertEquals(ptd(s(1)), "hace 1 segundo")
    self.assertEquals(ptd(s(2)), "hace 2 segundos")
    
  def testJustNow(self):
    self.assertEquals(ptd(d(0)), "ahorita")
    
  def testWithoutAgo(self):
    self.assertEquals(ptd(d(1), with_ago=False), "1 día")
    

if __name__ == '__main__':
  unittest.main()
