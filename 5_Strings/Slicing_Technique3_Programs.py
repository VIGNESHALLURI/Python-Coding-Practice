#Write a program to access alternate characters,reverse and reverse alternate characters
proverb = "Prevention is better"

#Print peet 0
print(proverb[:11:2])
print(proverb[-20:-9:2])

#Print ibt
print(proverb[11:18:3])
print(proverb[-9:-2:3])

#Print alternate characters
print(proverb[::2])

#Print reverse the entire string
print(proverb[19::-1])
print(proverb[-1::-1])

#Print reverse alternate characters
print(proverb[::-2])