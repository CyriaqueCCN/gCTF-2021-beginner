#!/usr/bin/env python3

import base65536

b = open('chall.txt', 'rb').read().decode("utf-8")

r = base65536.decode(b)

# we seem to only get the hex so we need to reencode into bytes
rr = bytes.fromhex(r.decode("utf-8"))

open("res1", "wb").write(rr)

