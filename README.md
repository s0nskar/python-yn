# python-yn

> parse yes/no like values

Useful for validating answers of a CLI prompt.

The following values can be recognised:

```python
'y', 'yes', 'true', 'True', 'Y', '1', 'no', 'n', 'false', 'False', '0'
```
*autocorrect feature can handle typos more efficiently*

## Install

```bash
$ pip install yn
```

## Usage

```python
>>> from yn import yn
>>> yn('Really?')
Really? [yes/no]
>>> yn('Do you like it?')
Do you like it? [yes/no]
```