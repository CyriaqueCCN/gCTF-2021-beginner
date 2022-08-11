## Brief

That was close! The armed guard didn’t notice you. The floor shakes, the boat is leaving the harbor. You are trying to stay hidden. You see two guards coming your way, you sneak into a small scrubber, they pass it, but then one of the guards takes out his phone and says “OK Google” and your phone suddenly makes a noise: PLING! The guards heard it: Guard 1: "Did you hear that?" Guard 2: "It must have come from the scrubber" Guard 1: "Let's have a look!" The guards close in, you are trapped! Suddenly a bell rings in the distance, and a voice talks through speakers: "Every man to their positions, the ship is about to debark, I repeat, every man to their positions." The guards change their course and head for their positions. Pheww, that was close! You find a better place to hide and settle in for the journey. Then you notice an ethernet socket in the wall. Might as well sniff some traffic while you're here.

Challenge: Noise on the wire (net)
You connect your laptop to the ethernet socket and start wireshark. It taks a while before something interesting pops up - perhaps the crew as busy with whatever is that they normally do. You look through the packets, and hey, these look pretty interesting...

## Solve

We have a pcap file

Using wireshark, we see that a zip file containing the flag is transmitted but it's password protected

We can recover the file using wireshark > follow TCP stream > save packet data as raw (in flag.zip.bin)

or use tcpick

`tcpick -r httponly.pcap -S -T1  -wR`

`cat flag.zip.bin | tail -c 209 > flag.zip`

A conversation is also intercepted, talking about "military grade encryption"

We infer the zip password is transmitted using this encryption so we get back the HTML page to see what is going on

We have a function to decrypt the message in the HTML so we juste c/p it into a webpage's console and call it with the message

`decryptWithMilitaryGradeEncryption("717f510b44623d391016bd6464450c5e316d1a0c16b95f794d487a2719373000be4a54445843273f080216b97c795348642d19300a169d627a4d645634280c0c21a53a241218")`

"zip's password is BossToldMeToSetABetterPasswordSoThisWillHaveToDo1234" 

(last message says "yeah")

We unzip with the password

Flag is `CTF{PleaseAssumeThisIsSomeSecretStuffThankYou}`
