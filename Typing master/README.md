#  Typing Master
### Difficulty : Easy
### Points : 50

# Description
If you think you have it in you, connect now to 34.216.132.109 9093 and prove your mettle.

You will be presented with a simple typing task which is meant to check your typing speed.

For example, Can you type 'Z' 10 times followed by 'u' 6 times, followed by the sum of their ASCII values?
				 **ZZZZZZZZZZuuuuuu207**

## Input Format

**Regarding input to the server** - The question was designed keeping netcat in mind. Some users who are using other tools/language (eg, Python, PuTTY, TELNET) to connect to the server please note that they do not terminate the strings like netcat does. If you choose not to use netcat, the message you send to our server should terminate with a trailing newline ('\n') and nothing else.

# Solution

After Connecting it through **nc 34.216.132.109 9093** it shows:

I want 'F' 274 times followed by 'p' 279 times, along with the sum of their ASCII values.
This connection will close in 10 secs ;) You gotta be fassssssssst :D 

And after 10 sec, it terminates connection showing:

Take help from your typewriter friend :) You seem too slow

It is impossible to type this soo much in 10 sec.
so,i used this script to solve problem. although it can be done through automation.

Copy from **'** to end and run program and paste result to get the flag

![alt text](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Typing%20master/first.jpg)

![alt text](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Typing%20master/second.jpg)


Flag : CodefestCTF{1_s33_y0u_4r3_a_m4n_0f_sp33d}
