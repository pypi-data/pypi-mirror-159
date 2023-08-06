# Simple Calculator in Python

> Python class for basic math operations.

[![PyPI Version][pypi-image]][pypi-url]
[![Build Status][build-image]][build-url]
[![Code Coverage][coverage-image]][coverage-url]
[![License: MIT][license-image]][license-url]

Package `calculator` contains Python class `Calculator` that performs basic mathematical operations, including:

- addition;
- subtraction;
- scalar multiplication;
- division;
- exponentiation;
- taking square root and n-th root.


## Details

Class attributes:

- `.result` -- contains a numeric value of current result.
   Initial default value is 0.

Class methods:

- `.add()`, `.subtract()`, `.multiply_by()`, `.divide_by()`,  `.exponentiate()`, `.take_n_root()`, `.sqrt()` -- These methods perform mathematical operations (addition, subtraction, scalar multiplication, division, exponentiation, taking n-th root, and taking square root respectively) on numeric value of `.result` (attribute) and number provided by the user and saves the result as `.result`.
- `.reset()` -- This method resets the `.result` to 0 (default) or other user defined value.


## Installation

Install from PyPi:

```bash
pip install calculator_vg
``` 

<!--
Install from TestPyPi:

```bash
pip install --index-url https://test.pypi.org/simple/ calculator_vg
```
-->

Install from GitHub:

```bash
pip install git+https://github.com/GegznaV/calculator-py.git
```

Get Docker image from Docker Hub with this package installed:

```bash
docker pull gegznav/calculator-py
```

## Usage

```python
>>> from calculator.calculator import Calculator

>>> calculator = Calculator()
>>> calculator.reset(to=35)
>>> calculator.result
35.0
>>> calculator.reset()
>>> calculator.result
0.0
>>> calculator.subtract(10)
>>> calculator.result
-10.0
>>> calculator.add(46)
>>> calculator.take_n_root(n=2)
>>> calculator.result
6.0
>>> calculator.reset()
>>> calculator.result
0.0
```

## GitHub Repository

GitHub repo (with continuous integration) that hosts the project:

- https://github.com/GegznaV/calculator-py


## License

This project is licensed under the terms of the [MIT][license-url] license.


## Author

Vilmantas Gėgžna


<!-- Badges -->

[pypi-image]: https://img.shields.io/pypi/v/calculator_vg
[pypi-url]: https://pypi.org/project/calculator_vg/

[build-image]: https://github.com/GegznaV/calculator-py/actions/workflows/check.yml/badge.svg
[build-url]: https://github.com/GegznaV/calculator-py/actions/workflows/check.yml

[coverage-image]: https://codecov.io/gh/GegznaV/calculator-py/branch/main/graph/badge.svg
[coverage-url]: https://codecov.io/gh/GegznaV/calculator-py

[license-image]: https://img.shields.io/badge/License-MIT-blue.svg 
[license-url]: https://opensource.org/licenses/MIT