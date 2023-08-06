# EIAS check relevant

The package that checks date relevant in EIAS system.

## Python

Python3.6.10

## Description

This package is used to reduce the codebase in main EIAS program. It checks that
source dict has `enddate` field which is more then 1970.01.01 and dict also has `request_status`
field which is not equal `CNCL`.

## Dict structure

```python
incoming = {
    'enddate': datetime.datetime,
    'request_status': str,
    ...
}
```

## Build instruction

https://packaging.python.org/en/latest/tutorials/packaging-projects/
