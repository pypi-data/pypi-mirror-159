# Can't Stop strategy helper

Using the algorithm from [Solitaire Laboratory](http://www.solitairelaboratory.com/cantstop.html),
`cant-stop` tells you if you should stop or continue your current turn of the dice game
[Can't Stop](https://boardgamegeek.com/boardgame/41/cant-stop).

# Installation

`cant-stop` is available on [PyPI](https://pypi.org/project/python-cant-stop/):

```bash
~$ pip install python-cant-stop
...
~$ cant-stop -h
```

## Installation from source

This assumes you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git),
[Python 3.9+](https://www.python.org/downloads/), and
[poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) installed
already.

```bash
~$ git clone git@gitlab.com:henxing/cant_stop.git
~$ cd cant_stop
cant_stop$ poetry install
...
cant_stop$ poetry run wordle-helper -h
```
