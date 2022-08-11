We have a C file that sends data to a hardware device, probably a 7-segment display. It seems to send ASCII-encoded characters. 

A little bit of research shows that the controller must send a mask either up or down to put up or down the corresponding bits.

We write a little python script for each state of the masks sent and we get back the characters from the flag, one by one.

Flag is `CTF{be65dfa2355e5309808a7720a615bca8c82a13d7}`
