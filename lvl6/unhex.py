#!/usr/bin/env python3

import sys

r = open(sys.argv[1], "r").read()
rr = bytes.fromhex(r.strip())
open(sys.argv[2], "wb").write(rr)
