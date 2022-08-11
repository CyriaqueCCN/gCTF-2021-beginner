def t(c,d):return c+len(d).to_bytes(4,"big")+d
r=range
n=[i for i in r(2,8000) if all(i%p for p in r(2,i))]
def e(b):return [b[i]^(n[i]&255) for i in r(len(b))]
def encode(i):a=bytes(r(97,123));return e(t(b"BEGN",a)+t(b"DATA",i)+t(b"END.",a.upper()))
