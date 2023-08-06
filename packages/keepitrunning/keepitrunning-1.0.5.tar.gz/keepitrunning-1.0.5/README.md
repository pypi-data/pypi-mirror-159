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

## Making it 24/7 (repl.it)
- Execute the code
- Copy the link on "Web" tab
- Go to uptimerobot.com and register or login
- Create a new ping and paste the link
It should be working 24/7 now.

## Note
- This only works for few IDE like repl.it.