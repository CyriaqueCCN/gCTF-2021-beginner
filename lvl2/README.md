## Solve

We must reverse some logic gates.

We just follow the stream (I did it by hand but I would've used Z3 for a more complex schema)

AND

G H I J


J & I 

!(G | H)

H ^ I 


((H ^ I) & !(G | H)) & (J & I)

needs to be true

G=0 H=0 I=1 J=1

&

!(A | !B) must be true
A | !B must be false

A=0 B=1

&

!((!C | D) | (E | !F)) must be true

(!C | D) | (E | !F) must be false

E | !F must be false ; E=0 F=1
!C | D must be false ; C=1 D=0

Flag is `CTF{BCFIJ}`
