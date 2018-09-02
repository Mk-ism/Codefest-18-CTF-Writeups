# Web Book
### Type : Web
### Difficulty : Easy
### Points : 75

# Description
It is expected to complete reading a book/novel to pass the course, but the students being clever avoid reading the whole book by going through the summary only.
Santosh(their course teacher) comes up with a new idea, he creates a magic book (you can only go to next page, that is: you can't go to next page without reading the previous one and so on, and you can only start from the beginning).
It is know that the flag is hidden somewhere in the book, so the only way to pass the course is to read the whole book, find the flag. The book has 1000 pages so better be fast. And if you are lucky, you may even find the key on the very first page itself.
![link to Web_BooK](http://34.216.132.109:8083/fp/)

# Solution
After opening web book it shows:

![alt text](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Web%20Book/page1.jpg)

In next page:

![alt text](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Web%20Book/page2.jpg)

and further on.
In every new page Session Cookie is changing. and tampering that it says not allowed.
In this i automate the webpage through python script which uses previous session and next page is opened and in every page it searches for flag. 

![Script](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Web%20Book/auto.py)

After running ![Script](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Web%20Book/auto.py) it gives the flag which was in the 998th page.

![alt text](https://github.com/Mk-ism/Codefest-18-CTF-Writeups/blob/master/Web%20Book/webflag.jpg)

Flag : CodefestCTF{bAs!c_ScripTing&isn!t(it)}