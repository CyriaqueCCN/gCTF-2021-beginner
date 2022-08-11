#!/usr/bin/env python3

x = open("hideandseek.png", "rb").read()

r = []
i = 0
for _ in range(48):
    try:
        a = x.find(b"\x65\x44\x49\x48") + 4
        r.append(x[a])#print(x[a])
        x = x[a:]
    except:
        break

print("".join([chr(z) for z in r]))
