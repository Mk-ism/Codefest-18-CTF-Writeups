# Prodigy
### Difficulty : Easy
### Points : 100

# Description
Self proclaimed prodigy Gourav, has just learnt about binaries and compiler. He believes he can hide anything in the [binary](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Web%20Book/prodigy) unless he doesn't print it. Show him that he is wrong.

# Solution
After searching **flag** in stings of binary i found a function **getFlag()**

After applying breakpoint at main(), jumping to getFlag(), and checking stack gives the flag.

![image](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Web%20Book/binary.jpg)

Flag : CodefestCTF{`cZNjbcipTKZgHL}
