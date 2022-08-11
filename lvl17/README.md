## Brief

You are walking through a corridor, but hey, what was that?! Changing room, you enter and find a uniform, you put it on, wow, you’re hot in uniform! You peek outside, and notice a sign on the wall that says "Master office, 100m". You close the door and plan your next steps. You're pretty close to completing your mission, but if anything goes wrong everything you've learnt will be lost. So you pull out your laptop, write down everything you know, encrypt it, hit send, and in horror watch an error appearing on the screen! You start investigating and quickly find out that a few blocks on your SSD chose this moment to die. But it gets worse - one of these blocks contained an encoding routine you needed for the data! No matter, you can implement it yourself in a few minutes, right?

Challenge: Playing golf (misc)
What luck! You found the official documentation of the protocol with an example implementation! Uh, but that's that? You can't write to the disk anymore? What?! OK, slowly now. You find a partially writable block with 235 bytes of free space. How are you going to squeeze in the encoder.py's functionality in just 235 bytes?! Well, you guess you have to try

## Link

https://capturetheflag.withgoogle.com/playing-golf.2021.ctfcompetition.com port 1337

## Solve

We need to write a golfed version of encoder.py

First, we need to eliminate the huge list of numbers
Fortunately, they are all primes, so they should be easy to generate

We have 5 seconds to execute the code right

We need to find the first 1000 primes

We list version and modules

Python 3.8.10 (default, Jun  2 2021, 10:49:15) 
[GCC 9.4.0]

We list all the modules we have server side to not get a nasty surprise after working locally

We have math, cmath and numbers. Or re, but it's too slow

I think we'd better look into the codegolfs rather than the modules

We find a good one, using only list comprehensions and the built-in "all"

Looking at the tester, it appears we can generate only the first 800 primes (scanning numbers until 8000)

We write our script, pruning it over and over again

And finally... netcat'ing the code yields :

Verifying tests...
All tests passed!

Flag is `CTF{EncodingSuccessfulIntelReceivedCorrectly}`
