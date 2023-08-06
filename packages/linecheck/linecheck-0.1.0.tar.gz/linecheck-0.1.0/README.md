# linecheck

This package runs a check that files end with newlines.

```bash
usage: linecheck [-h] [--fix] [-v] [--match [MATCH [MATCH ...]]]
                 [--ignore [IGNORE [IGNORE ...]]]
                 path

Check if files end in newlines.

positional arguments:
  path                  File to check or folder to recurse into.

optional arguments:
  -h, --help            show this help message and exit
  --fix                 Fix files that don't end in newlines.
  -v, --verbose         Print file names.
  --match [MATCH [MATCH ...]]
                        Only check files matching this pattern.
  --ignore [IGNORE [IGNORE ...]]
                        Ignore filepaths containing these.
```
