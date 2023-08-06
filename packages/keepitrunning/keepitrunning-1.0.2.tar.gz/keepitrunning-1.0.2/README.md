# keepitrunning

A simple python library that can be used for hosting your python project 24/7.

## Installation
```bash
pip install keepitrunning
```

## Example
```python
from keepitrunning import Host
api = Host()
api.keep_running(80) # port, default: 8080
```

## Note
- This only works for few IDE like repl.it.