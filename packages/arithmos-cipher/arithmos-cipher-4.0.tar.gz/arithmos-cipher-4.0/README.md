[![Repo Visitors](https://visitor-badge.glitch.me/badge?page_id=LyQuid12.arithmos-cipher&left_text=Repo%20Visitors)](https://github.com/LyQuid12/arithmos-cipher)
[![Downloads](https://pepy.tech/badge/arithmos-cipher)](https://pepy.tech/project/arithmos-cipher)
[![PyPI - Version](https://img.shields.io/pypi/v/arithmos-cipher?label=PyPI%20Version&logo=pypi)](https://pypi.org/project/arithmos-cipher)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/arithmos-cipher?label=Python%20Version&logo=python)](https://pypi.org/project/arithmos-cipher#data)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/LyQuid12/arithmos-cipher?label=Pull%20Requests)](https://github.com/LyQuid12/arithmos-cipher/pulls)
[![Discord](https://img.shields.io/discord/887650006977347594?color=blue&label=EterNomm&logo=discord)](https://discord.com/invite/qpT2AeYZRN)

# Arithmos Cipher
Arithmos Cipher is the most simple [Cryptography](https://en.wikipedia.org/wiki/Cryptography) that I created myself in [Python](https://python.org). Arithmos is taken from the Greek word (Arithmós or αριθμός) which means "Number". *Not recommended for encrypting important thing*.

## Explanation of how it works
Basically, the given sentences will be exchanged with numbers in alphabetical order (Example: `a = 01` to `z = 26` and `A = 27` to `Z = 52`). For alphabet with one digit will be added `0` in front of it. Each one of the alphabet has a `2` digit number. And for `uppercase letters` starting from the number `27` after lowercase `(z = 26)`[.](https://youtube.com/watch?v=dQw4w9WgXcQ)

**Here the example of the explanation above :**
```
Example = 31240113161205

31 : E
24 : x
01 : a
13 : m
16 : p
12 : l
05 : e
```

## Usage
- **Install**
```
pip install arithmos-cipher
```

- **Example**
  - Via CLI
    
    Check on the [documentation](https://github.com/LyQuid12/arithmos-cipher/blob/master/cli.md). <br>
    *Note* : Arithmos Cipher **chain** are **not available** on CLI.
  - Via packages

    Check on [examples](https://github.com/LyQuid12/arithmos-cipher/tree/master/examples) directory.

## Licence & Copyright
This Project under [Apache License 2.0](https://github.com/LyQuid12/arithmos-cipher/blob/master/LICENSE).
```
Copyright (c) 2022-present LyQuid
```
