def t(c,d):return c+len(d).to_bytes(4,"big")+d
n=[];r=range
for i in r(2,8000):
 if all(i%p for p in n):n+=[i]
def encode(b):q=bytes;a=q(r(97,123));return q([z^(x&255) for z,x in zip(t(b"BEGN",a)+t(b"DATA",b)+t(b"END.",a.upper()),n)])
