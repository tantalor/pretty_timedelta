#!/usr/bin/env python

from distutils.core import setup

import os
import os.path

MODULE_DIR = 'pretty_timedelta'
LOCALE_DIR = 'locale'

lang_dirs = [
  fn for fn in [
    os.path.join(LOCALE_DIR, fn) for fn
    in os.listdir(os.path.join(MODULE_DIR, LOCALE_DIR))
  ]
  if os.path.isdir(os.path.join(MODULE_DIR, fn))
]

lang_files = [os.path.join(fn, 'LC_MESSAGES', 'pretty_timedelta.mo') for fn in lang_dirs]

setup(
  name='pretty_timedelta',
  description='Formats timedelta objects as pretty text in any language.',
  author='John Tantalo',
  author_email='john.tantalo@gmail.com',
  url='http://github.com/tantalor/pretty_timedelta',
  packages=['pretty_timedelta'],
  package_data={'pretty_timedelta': lang_files},
)
