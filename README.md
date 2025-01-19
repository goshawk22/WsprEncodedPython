# WsprEncodedPython

This is the python bindings for the [WsprEncoded](https://github.com/traquito/WsprEncoded) library.

Pre-built libraries available in the prebuilt folder.

If you don't find a pre-built library suitable for your system, raise an [issue](https://github.com/traquito/WsprEncodedPython/issues) and an attempt will be made to make one available.

Install directory -- put in the directory printed when running this command:
```
python -m site --user-site
```

Note -- The pre-built binaries have not been tested across all systems and are provided as a best-effort attempt to avoid you needing to build the library yourself.


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
./test_wspr_encode.py
./test_wspr_decode.py
```

Building yourself depends on [Python](https://www.python.org/downloads/), [CMake](https://cmake.org/download/), and [Ninja](https://ninja-build.org/) being installed.

See the website for more details on library use.

https://traquito.github.io/pro/telemetry/code