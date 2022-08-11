## Brief

You’re exiting a crowded subway nearby the office that you are about to visit. You are showing the guards your ID and answering a couple of routine questions. They are not impressed, but the gate opens up and you can enter the area despite their doubt. You are not allowed to stroll freely on the company grounds, but are shown around by a woman that stares at you with a crooked smile. At last you're able to talk to the manager, a short man with a white robe and shades: "Greetings, AGENT, You must be thirsty after your long journey? No? You don’t mind if I’ll have something for myself, do you? Good! We have heard about the device that you possess, can I have a look at it. Hmm, it seems that it is encrypted. Help me break this quickly so that we can continue with the analysis."

Challenge: To the moon (misc)
This one is a doozie. We found this weird file on a memory stick with a post-it note on it. It looks like someone was working on a very obscure encryption system. Maybe we can decode it? 

## Solve

We search for "higher than base64" in google and after a while we find base65536. Conveniently, we have a python library to decode it.

The result is hexadecimal, so we need another pass to recover the original bytes. We write the result in a file, which appears to be a jpeg image.

This is consistent with the encodings, as the next one is "named after a painter". We are talking about Piet here (from Piet Mondrian), which uses an image as source code

After trying 4 interpreters, the program seems to infinite loop.

We try to analyze it and come across a big string when stringing it

`strings -n 100 res.jpg > res2`

After searching for the "opposite of good", we find a language, Evil, composed uniquely of alphabet letter. 

We paste the string into the online interpreter at https://tio.run/#evil

and we get res3, which seems to be yet another hexdump. We convert it into bytes as res4 and file it, it seems to be a zlib file

`cat res4 | zlib-flate -uncompress > res5`

We file res5, it's a gzip file, we gzip -d it into res6

res6 is a netpbm image. I searched around before trying to use piet again

`npiet res6 > res7`

We have 912 bytes of hex then garbage, we keep only the hex

`head -c 912 res7 > res8`

`cat res9| zlib-flate -uncompress > res10`

The file is ascii reading "nyyyyya~" multiple times.

We are at the "rainbow cat" part of the encoding now. I first thought of LOLcode but it's transparent, an esolang called nya~ which is basically brainfuck without loops

We find an interpreter and run it

https://github.com/sech1p/nya

`./nya/build/nya res10 > res11`

We have this time a very big number. We now know that we deal with unary, so we convert our number into binary then replace the codes to get brainfuck

We use the module python-brainfuck to execute it and print the result and we finally get the flag

Flag is `CTF{pl34s3_n0_m04r}`
