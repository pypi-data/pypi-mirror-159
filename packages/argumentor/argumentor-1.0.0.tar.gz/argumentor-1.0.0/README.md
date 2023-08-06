# argumentor

## Description

A simple, copylefted, lightweight library to work with command-line arguments in Python

## Features

- No external dependency
- Easy to use
- Automatic help page generation
- Support for default values
- Published under LGPLv3, a copyleft license that still lets you use the library in a project that is not under the same license

## Installation

```shell
$ pip install argumentor
```

## Usage

```python
from argumentor import Arguments

parser = Arguments()
parser.add_operation(
    operation="--help",
    value_type=bool,
    description="Print help page"
)

operations, options = parser.parse()

if operations["--help"]:
    print(parser.help_page)
```

More usage can be found [in the documentation](https://twann.codeberg.page/python-argumentor/)

## License

[![LGPLv3 badge](https://www.gnu.org/graphics/lgplv3-147x51.png)](https://codeberg.org/twann/python-argumentor/src/branch/main/LICENSE)

This repository and its content (unless specified otherwise) are released under the terms of the [GNU Lesser General Public License version 3](https://codeberg.org/twann/python-argumentor/src/branch/main/LICENSE).
