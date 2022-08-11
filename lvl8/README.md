## Brief

You arrive at the location through the coordinates that you got from the assassin, a luxurious yacht. A fat, bald man lies on a puma couch. He sips on a dry martini, smokes the biggest cigar you've ever seen and when he smiles, a golden tooth is revealed. You can’t help but smile back at him, although you think the place seems shady. "Welcome to my yacht, Johnson, finally you show us your face. Have you killed the AGENT now? Good! You’re here to collect your reward I presume? I’ll have my guy finalize the transaction but before you leave I need a small favour from you." It seems that he is mistaking you for the assassin but you don’t mind.

Challenge: Hide and seek (misc)
The man hands you a pendrive which you reluctantly connect to your laptop. He says he got it from a partner, and the partner claims that he hid valuable information in that PNG there. The problem is, it looks empty. See if you can find anything

## Solve

A PNG file. pngcheck says "Unkown chunks eDIH after each IDAT chunk"

Using the excellent https://www.nayuki.io/page/png-file-chunk-inspector, we find many of those eDIH chunks.

eDIH spells hide backwards

48 of them with a length of 1 byte each time

Let's write a simple script that gets that byte and logs it's ascii encoding

We get a string looking like base64, we decode it and get the flag

`echo "Q1RGe0RpZFlvdUtub3dQTkdpc1Byb25vdW5jZWRQSU5HP30=" | base64 -d`

Flag is `CTF{DidYouKnowPNGisPronouncedPING?}`
