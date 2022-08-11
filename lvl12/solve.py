#!/usr/bin/env python3

import requests
import itertools

TARGET = "https://old-lock-web.2021.ctfcompetition.com/"

def main():
    perms = list(itertools.permutations(["3", "5", "7", "8", "0"]))
    for p in perms:
        r = requests.post(TARGET, data={"v" : "".join(p)})
        if not "that's not it" in r.text:
            print(r.text)
            break

main()
