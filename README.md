# Pretty Timedelta

Pretty Timedelta is a simple python module for formatting [timedelta](http://docs.python.org/library/datetime.html#datetime.timedelta) objects as pretty text in any language you want.

## Example

You can use the `pretty_datetime()` function as so.

    from datetime import timedelta
    from pretty_datetime import pretty_datetime

    five_minutes = timedelta(0, 0, 0, 0, 5)
    print pretty_datetime(five_minutes) # "5 minutes ago"

Or directly from the command line:

    $ python pretty_timedelta.py 0 0 0 0 5
    5 minutes ago

## Localization

Pretty Timedelta can support almost any langauge via the [gettext](http://www.gnu.org/software/gettext/) utility. Currently, it supports English and Spanish.

If you want to try it in Spanish, try setting your `LANGUAGE` environment variable.

    $ export LANGUAGE=es
    $ python pretty_timedelta.py 0 0 0 0 5
    hace 5 minutos

## Tests

Pretty Timedelta comes with a bunch of tests, of course.

    $ python pretty_timedelta_test.py 
    ............
    ----------------------------------------------------------------------
    Ran 12 tests in 0.003s

    OK

## LICENSE

Pretty Timedelta is packaged with the [MIT Licence](http://en.wikipedia.org/wiki/MIT_License), reproduced below.

    (The MIT License)

    Copyright © 2009 John Tantalo

    Permission is hereby granted, free of charge, to any person obtaining a copy of
    this software and associated documentation files (the ‘Software’), to deal in
    the Software without restriction, including without limitation the rights to
    use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
    the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED ‘AS IS’, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
    FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
    COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
    IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
    CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

