# Coronavirus Michigan Readings

[![Build Status](https://travis-ci.com/debsahu/CoronaVirus.svg?branch=master)](https://travis-ci.com/debsahu/CoronaVirus) [![License: MIT](https://img.shields.io/github/license/debsahu/CoronaVirus.svg)](https://opensource.org/licenses/MIT) [![version](https://img.shields.io/github/release/debsahu/CoronaVirus.svg)](https://github.com/debsahu/CoronaVirus/releases/tag/1.0.0) [![LastCommit](https://img.shields.io/github/last-commit/debsahu/CoronaVirus.svg?style=social)](https://github.com/debsahu/CoronaVirus/commits/master)

Python based webscraper to get live readings from [Michigan Coronavirus COVID-19 page](https://www.michigan.gov/coronavirus)

## Python3 (recommended: use virtual environment)

Install required Python3 libraries

```
pip install --no-cache-dir -r requirements.txt
```

Run Python3 script

```
python coronavirus.py
```
## Docker

Build and Run

```
docker build -t debsahu/coronavirus .
docker run --rm debsahu/coronavirus
```