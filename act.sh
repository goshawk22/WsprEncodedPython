#!/usr/bin/env -S bash

# act push --artifact-server-path .act/artifacts --matrix os:ubuntu-latest --matrix compiler:gcc

act push --artifact-server-path .act/artifacts --matrix os:ubuntu-latest --matrix compiler:mingw