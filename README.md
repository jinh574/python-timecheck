## Install

    python setup.py build
    python setup.py install

## How to use

### Timer
``` python
from timecheck import Timer

_t = Timer("Timer name")

_t.tic()
for _ in range(100000):
    pass
print(_t.toc())
```

### MultiTimer
``` python
from timecheck import MutlTimer

_t = MultiTimer()

_t['for-state'].tic()
for _ in range(100000):
    pass
print(_t['for-state'].toc())

_t['func-state'].tic()
func()
print(_t['func-state'].toc()
```
