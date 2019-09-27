# t-gen
Template directory generator for competitive coding

```console
$ ./t-gen ABC001 # Only for atcoder contests
.
└── ABC001
    ├── build/
    ├── A.cc
    ├── B.cc
    ├── C.cc
    ├── D.cc
    ├── E.cc
    ├── F.cc
    ├── CMakeLists.txt
    ├── Makefile
    └── test.py
or
$ ./t-gen ABC001 ABCD
.
└── ABC001
    ├── build/
    ├── A.cc
    ├── B.cc
    ├── C.cc
    ├── D.cc
    ├── CMakeLists.txt
    ├── Makefile
    └── test.py
```
To make use `make all`, and to run the test use `make test`.
Tests can be specified using `make test ABC` where only the tests for `ABC` would execute.

To add tests, modify `test.py`
```
'A': [
  ['Input1', 'Expected Output1'],
  ['Input2', 'Expected Output2']
  .
  .
  .
]
```

Root directory for the templates are configurable in `settings.json`
