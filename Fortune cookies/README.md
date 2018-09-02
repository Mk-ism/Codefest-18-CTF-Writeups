#  Fortune Cookie 
### Difficulty : Easy
### Points : 75

# Description
H4k3r has heard that there is a secret hidden behind this website(http://34.216.132.109:8084/), but he is confused as to how to get access to it. Can you help him.

# Solution
After visiting page it shows :

![alt text](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Fortune%20cookies/first.jpg)

Intercepting through burp, cookies shows: Cookie: who are you?=Me

![alt text](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Fortune%20cookies/before.jpg)

Then add Cookie: who are you?=admin

After changing we got the flag:

![alt text](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Fortune%20cookies/after.jpg)


Flag : CodefestCTF{f0r7Un4B1sC0TtO}
