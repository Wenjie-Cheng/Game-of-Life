## Badges

| Badges | |
| :-- | :--  |
| (1/2) code repository              | [![github repo badge](https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue)](https://github.com/Wenjie-Cheng/Game-of-Life) |
| (2/2) license                      | [![github license badge](https://img.shields.io/github/license/Wenjie-Cheng/Game-of-Life)](https://github.com/Wenjie-Cheng/Game-of-Life/blob/master/LICENSE) |


## Description

A Conway's Game of Life code. Part of Big Geodata Processing course

## Installation

To install Game-of-Life from GitHub repository, do:

```console
git clone https://github.com/Wenjie-Cheng/Game-of-Life.git
cd Game-of-Life
python -m pip install .
```

Pypi package install 

```console
pip install lifebgp==0.1.0
```

## Functions

Import library

```console
from life import Life
```

Input data

```console
Life.(filename)
```

tick grid

```console
Life.tick_grid(n)
```

Input data

```console
Life.write_grid("filename.txt")
```


## Credits

This package was created with [Copier](https://github.com/copier-org/copier) and the [NLeSC/python-template](https://github.com/NLeSC/python-template).
