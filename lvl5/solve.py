#!/usr/bin/env python3

import random

from mt_recover import MT19937Recover

def get_samples():
    rr = open("robo_numbers_list.txt", "r").read().replace("-", "").split("\n")
    return [int(x.strip()) - (1<<31) for x in rr]


def mersenne_invert():
    r = get_samples()
    rcv = MT19937Recover()
    r2 = rcv.go(r, forward=False)
    print(decodesec(r2))

def decodesec(r2):
    s = open("secret.enc", "rb").read()
    key = [r2.getrandbits(8) for i in range(len(s))]
    return "".join([chr(a^b) for a,b in zip(list(s), key)])

#print(decodesec())
mersenne_invert()
