s= raw_input()
fst = s[1]
snd = s[27]
no1 = int(s[4:7])
no2 = int(s[30:33])


c =  ord(fst) + ord(snd)
print fst*no1 + snd*no2 + str(c)