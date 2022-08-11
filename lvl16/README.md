## Brief

Well, okay, you’re back in the cell again, and they changed the lock to something quite heavier. This one cannot be picked with a paperclip… So, is this where the mission ends? PLING, another message from the boss. Another GIF… No wait, not only a GIF, also text: "Hi AGENT, I was just contacting you to say that we’re running out of time, if you fail to reach the office and pull the self destruction lever in under 30 minutes, they will already have executed their evil plan. I’m counting on you!." Well, that wasn’t too helpful... What to do, what to do?

Challenge: Hash-meee (misc)
I heard BotBot, the resident Discord bot, is experimenting with hashing. He specifically wants to see 2 different strings, both starting with `gctf`, that have the same md5 hash. He will reward this with a flag. You can access our Discord with the following invite link: https://discord.gg/nt6JFkk3mu To solve this challenge DM BotBot on discord using the command `!hashme` followed by the two strings, encoded in hex. E.g. if your strings are "gctfhello" and "gctfhola" you would send `!hashme 6763746668656c6c6f 67637466686f6c61`
We need to create a md5 collision of 2 strings starting with  gctf

## Solve

We use hashclash and launch it with a prefix.txt with gctf

We wait for 30 min
```
Block 1: ./data/coll1_1661686904
c1 50 80 11 54 44 37 97 8d bf 56 2f 20 40 54 6f 
e2 c3 60 97 0a e9 66 2f 47 96 8d b4 51 8e 4c 5f 
76 e7 68 13 80 23 38 a1 0e 86 96 39 e6 69 17 b0 
b8 ad f7 43 00 2a df 6d 02 c6 91 6f 33 9a 88 df 
Block 2: ./data/coll2_1661686904
c1 50 80 11 54 44 37 97 8d c0 56 2f 20 40 54 6f 
e2 c3 60 97 0a e9 66 2f 47 96 8d b4 51 8e 4c 5f 
76 e7 68 13 80 23 38 a1 0e 86 96 39 e6 69 17 b0 
b8 ad f7 43 00 2a df 6d 02 c6 91 6f 33 9a 88 df 
Found collision!
md5_diffpathhelper: /home/user42/google_ctf_2022/beginnerquest/lvl16/hashclash/boost-1.57.0/include/boost/thread/pthread/mutex.hpp:111: boost::mutex::~mutex(): Assertion `!res' failed.
9d4303312a0e9df4e30bd757b82a76ea  collision1.bin
9d4303312a0e9df4e30bd757b82a76ea  collision2.bin
0376fdab002c187347fe9d9c31753ebfe3abbd01  collision1.bin
b1cfcd3152d285095a2062e1c65a8eb6d25c705f  collision2.bin
4 -rw-rw-r-- 1 user42 user42 128 juil.  4 23:38 collision1.bin
4 -rw-rw-r-- 1 user42 user42 128 juil.  4 23:38 collision2.bin
```

We get the hex values of those last 2 files :

`xxd -p collision2.bin | tr -d '\n'`

`xxd -p collision1.bin | tr -d '\n'`

We c/p the hex strings and send a message to the bot

`!hashme 676374664029925d2bd58adbe0abc227a2e2965a2b1832166f16187e407be6ebd7578e53e722f72d96c3bdfb141f9ae0d57da01bd90ff563ee746bdafdde73b1c1508011544437978dc0562f2040546fe2c360970ae9662f47968db4518e4c5f76e76813802338a10e869639e66917b0b8adf743002adf6d02c6916f339a88df 676374664029925d2bd68adbe0abc227a2e2965a2b1832166f16187e407be6ebd7578e53e722f72d96c3bdfb141f9ae0d57da01bd90ff563ee746bdafdde73b1c1508011544437978dbf562f2040546fe2c360970ae9662f47968db4518e4c5f76e76813802338a10e869639e66917b0b8adf743002adf6d02c6916f339a88df`

He responds :

Good job! Here is a flag for you!

`CTF{h4sh_m3_tw1c3}`
