# datels

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/datels?style=plastic)](https://github.com/joe-yama/datels) [![PyPI - License](https://img.shields.io/pypi/l/datels?style=plastic)](https://github.com/joe-yama/datels) [![PyPI](https://img.shields.io/pypi/v/datels?style=plastic)](https://pypi.org/project/datels/) [![codecov](https://codecov.io/gh/joe-yama/datels/branch/main/graph/badge.svg?token=RCQSYF637E)](https://codecov.io/gh/joe-yama/datels)

`datels` is a simple CLI that displays a list of dates line by line.

## Installation

To install datels with pip, run: `pip install datels`

## Basic Usage

```bash
$ datels 1994-03-07 1994-03-10
1994/03/07
1994/03/08
1994/03/09
1994/03/10
```

### Date format option

```bash
$ datels 1994-03-07 1994-03-10 --sep="-"
1994-03-07
1994-03-08
1994-03-09
1994-03-10

$ datels 1994-03-07 1994-03-10 --format "%c"
Mon Mar  7 00:00:00 1994
Tue Mar  8 00:00:00 1994
Wed Mar  9 00:00:00 1994
Thu Mar 10 00:00:00 1994
```

See [strftime documentation](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) for more information.

### Inclusive option

```bash
$ datels 1994-03-07 1994-03-10 --inclusive both
1994/03/07
1994/03/08
1994/03/09
1994/03/10

$ datels 1994-03-07 1994-03-10 --inclusive left
1994/03/07
1994/03/08
1994/03/09

$ datels 1994-03-07 1994-03-10 --inclusive right
1994/03/08
1994/03/09
1994/03/10
```

## Using in your python code not CLI

```bash
$ python
>>> from datels import list_dates
>>> dates = list_dates("1994-03-07", "1994-03-10", sep="-", inclusive="both")
>>> dates
['1994-03-07', '1994-03-08', '1994-03-09', '1994-03-10']
>>> # list_dates retuens list of string
>>> type(dates)
<class 'list'>
>>> type(dates[0])
<class 'str'>
```