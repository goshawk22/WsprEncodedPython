# WsprEncodedPython

This is the python bindings for the [WsprEncoded](https://github.com/traquito/WsprEncoded) library.

[![Build DLL for Windows and Linux](https://github.com/traquito/WsprEncodedPython/actions/workflows/build-and-deploy.yml/badge.svg)](https://github.com/traquito/WsprEncodedPython/actions/workflows/build-and-deploy.yml)

To build the python extension yourself:

```
# Get a copy of the repo
git clone https://github.com/traquito/WsprEncodedPython.git

# Configure, Build, and Install
cd WsprEncodedPython
./configure.sh
./build.sh
./install.sh

# Test
./test_wspr_encode_user_defined.py
./test_wspr_decode_user_defined.py
./test_wspr_decode_common.py
```

Building yourself depends on [Python](https://www.python.org/downloads/), [CMake](https://cmake.org/download/), and [Ninja](https://ninja-build.org/) being installed.

See the website for more details on library use.

https://traquito.github.io/pro/telemetry/code