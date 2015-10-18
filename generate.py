import random
import textwrap


b = open('./data/buzzfeed.txt', 'r')
t = open('./data/tractatus.txt', 'r')

buzzfeed = list()
tractatus = list()

# will / that will

for line in t:
    offset = line.find(" will ")
    if offset != -1 and line.find(" the will ") == -1 and line.find(" there will ") == -1 and line.find("(") == -1:
        tractatus.append(line[:offset+1])

for line in b:
    offset = line.find(" That Will ")
    if offset != -1:
        buzzfeed.append(line[offset+6:])

for i in range(1):
    tractatus_ch = random.choice(tractatus)
    buzzfeed_ch = random.choice(buzzfeed)#.lower()
    combined = tractatus_ch + buzzfeed_ch
    print("\n" + textwrap.fill(combined, 60) + "\n")

# can 
b = open('./data/buzzfeed.txt', 'r')
t = open('./data/tractatus.txt', 'r')

buzzfeed = list()
tractatus = list()

for line in t:
    offset = line.lower().find(" can ")
    if offset != -1 and line.find(" there can ") == -1:
        tractatus.append(line[:offset+1])

for line in b:
    offset = line.lower().find(" can ")
    if offset != -1:
        buzzfeed.append(line[offset+1:])

for i in range(1):
    tractatus_ch = random.choice(tractatus)
    buzzfeed_ch = random.choice(buzzfeed)#.lower()
    combined = tractatus_ch + buzzfeed_ch[:-1] + "."
    print("\n" + textwrap.fill(combined, 60) + "\n")
