#!/usr/bin/env python3

r = open("res11", "r").read().strip()

b = bin(int(r))[3:]

# binary unary repr (shhhhh.)
print(b)

# after https://esolangs.org/wiki/Unary

dico = {"000":">",
        "001":"<",
        "010":"+",
        "011":"-",
        "100":".",
        "101":",",
        "110":"[",
        "111":"]"}

res = ""

for i in range(0, len(b), 3):
    res += dico[b[i:i+3]]

# unary brainfuck repr
print(res)

import brainfuck as bf

braaaaain = bf.to_function(res)

x = braaaaain()

print(x)

