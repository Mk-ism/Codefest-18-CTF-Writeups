# Prodigy
### Difficulty : Easy
### Points : 100

# Description
Self proclaimed prodigy Gourav, has just learnt about binaries and compiler. He believes he can hide anything in the [binary](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Prodigy/prodigy) unless he doesn't print it. Show him that he is wrong.

# Solution
After searching **flag** in strings of binary i found a function **getFlag()**

After applying breakpoint at main(), jumping to getFlag(), and checking stack gives the flag.

![alt text](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Prodigy/binary.jpg)

Flag : CodefestCTF{`cZNjbcipTKZgHL}
