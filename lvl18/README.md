## Brief

You press a button and enter through a tinted glass door. There is a vast oil painting on the wall that depicts a bold man with a scar under his left eye, under his arms rests a white chubby cat. Below the painting is the very same man, and he’s addressing you: "Well, well, well. Isn’t it the trouble maker? Huh, how did you get past the guards? Well, I have a final offer for you. I’ll let you live only on one condition: START WORKING FOR ME! BWAHAHAHAHA-" While he goes on with his monologue about conquering the world and some twisted philosophy about how he is actually the good guy and so on you start discretely fiddling with a control panel labeled "Self destruction". You need to quickly figure out the activation code while he’s distracted.

Challenge: Strange Virtual Machine (reversing)
Everyone is coming up with their own programming language these days, so I came up with my own architecture. You can use it to run the attached program that will print the flag for you.

## Solve

We have a Rust VM

Launching it

`./target/release/vm-cli ../vm.rom`

`CTF{ThisIsAVeryLongFlagAndYouMigh^C`

It's very long and I don't wanna fry my CPU. Let's reverse that.

[...]
