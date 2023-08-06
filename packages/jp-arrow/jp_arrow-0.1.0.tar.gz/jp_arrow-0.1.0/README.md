# jp_arrow.
Conver date/datetime from/to Japanese date/datetime.

This module highly depend on "arrow".

## Install

`pip install jp_arrow`

## How to use

```python
In [1]: import jp_arrow

In [2]: jp_arrow.utcnow().format('EEYYYYMMDD', locale='ja')
Out[2]: '令和04年0715日'

In [3]:
```

```
In [2]: dt = jp_arrow.get('平成36年01月13日')

In [3]: dt
Out[3]: <Arrow [2024-01-13T00:00:00+00:00]>

In [4]: dt.format(jp_arrow.FORMAT_WAREKI)
Out[4]: '令和6年1月13日'

In [5]: dt.format(jp_arrow.FORMAT_WAREKI_W)
Out[5]: '令和06年01月13日'

In [6]: dt.format(jp_arrow.FORMAT_JISX0301)
Out[6]: 'R6.1.13'

In [7]: dt.format(jp_arrow.FORMAT_JISX0301_W)
Out[7]: 'R06.01.13'

In [8]:
```

