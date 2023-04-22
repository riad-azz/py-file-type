# Py File Type

A wrapper for [python-magic](https://pypi.org/project/python-magic/) that includes python-magic-bin files.

## Description

This was made duo to a file conflict problem happening when trying to
install [python-magic](https://github.com/ahupp/python-magic)
and [python-magic-bin](https://pypi.org/project/python-magic-bin/).

## Installing

```bash
pip install py-file-type
```

## Usage

Works exactly like [python-magic](https://github.com/ahupp/python-magic)

```python
import py_file_type as magic

file_type = magic.from_file('video.mp4', mime=True)
print(file_type)  # -> video/mp4
```

## Authors

Riadh Azzoun - [@riad-azz](https://github.com/riad-azz)

## License

This project is licensed under the [MIT] License - see the LICENSE.md file for details