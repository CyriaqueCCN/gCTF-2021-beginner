## Brief

It’s a hot day, and your skin is cracking and dry. It’s difficult to make your way through the crowded bazaar. A high pitch voice pierces through the soundscape from a salesman that’s trying to sell colorful fabrics and then from another corner comes delicious smells. You spot a hand waving - it’s your contact that you’ve been waiting to meet. "Take a seat, my friend, I’m Gökhan, have you been to Istanbul before? No, really? I’m sure that you will have a great time, I’ve ordered tea for the two of us. Show me the amulet, will you?. Wow, this is really something from my younger days, this is as mysterious as it is beautiful and belongs to “The cloaked brotherhood”. They are very dangerous, and eventhough your quest is urgent, I would advise you to not continue looking for the owner of this. Go home, and forget about it." In the blink of an eye, four tough guys show up, and you start to run together with Gökhan through the crowded marketplace and then up on a rooftop. The tough guys are closing in, but the two of you climb down from the rooftop, run around a corner and are able to hide in two crates.

Challenge: Twisted robot (misc)
We found this old robo caller. It basically generates random phone numbers to spam. We found the last list of numbers in generated and also some weird file... Maybe it's got to do with these new beta features they were testing? 

## Solve

From the brief, we know that it's "old"

Luckily for us, Python's old implementation of random was using Mersenne's Twister, which is reversible if you have enough samples.

Funny enough, Mersenne Twister is invertible after 624 outputs, and we have a list doing exactly that.

We postulate that the encrypted file was generated right after running the spam list generator, otherwise we're screwed.

Downloading a Mersenne reverser online, we hack it together with a little script and run it.

Flag is `CTF{n3v3r_3ver_ev3r_use_r4nd0m}`
