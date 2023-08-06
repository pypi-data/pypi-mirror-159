# apip
[![Built with python](https://img.shields.io/badge/-Python-3c679c?style=for-the-badge&logo=Python&logoColor=fae583)](https://python.org)

---
An easy, high level wrapper for the Pip API. It uses `subprocess` to
use the Pip CLI and wrap it into an easier to use package in Python.
---

## Installation
**Requires Python 3.7+**

To install `apip` on PyPi, run 
```shell
pip install apip
```
---

## Quickstart
To get started and see what `apip` can do, run some example programs.
```python
>>> import apip
>>> pip = apip.Pip()
>>> pip.install("module")
>>> pip.get("module")
>>> print(pip.list())
>>> pip.uninstall("module")
```
