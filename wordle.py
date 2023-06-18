#wordle solver program

import linecache

text = open("validWords.txt", "r")
words = text.read()
words = words.split(" ")
text.close()

yellow = []
yellowpos = []

green = []
greenpos = []

gray = []

decisions = linecache.getline("mem.txt", 1).replace('\n', '')

if decisions[0] == 'y':
    gray = linecache.getline("mem.txt", 2).replace('\n', '')
    gray = gray.split(" ")
if decisions[1] == 'y':
    yellow = linecache.getline("mem.txt", 3).replace('\n', '')
    yellow = yellow.split(" ")
    yellowpos = linecache.getline("mem.txt", 4).replace('\n', '')
    yellowpos = yellowpos.split(" ")
    for k in range(len(yellowpos)):
        yellowpos[k] = int(yellowpos[k])
if decisions[2] == 'y':
    green = linecache.getline("mem.txt", 5).replace('\n', '')
    green = green.split(" ")
    greenpos = linecache.getline("mem.txt", 6).replace('\n', '')
    greenpos = greenpos.split(" ")
    for k in range(len(greenpos)):
        greenpos[k] = int(greenpos[k])

j = 0

while j < len(gray):
    i = 0
    while i < len(words):
        if gray[j] in words[i]:
            words.remove(words[i])
        else:
            i += 1
    j += 1

j = 0

while j < len(green):
    i = 0
    while i < len(words):
        if green[j] not in words[i][greenpos[j]]:
            words.remove(words[i])
        else:
            i += 1
    j += 1

j = 0

while j < len(yellow):
    i = 0
    while i < len(words):
        if yellow[j] in words[i][yellowpos[j]] or yellow[j] not in words[i]:
            words.remove(words[i])
        else:
            i += 1
    j += 1

output_text = ' '.join(words)

text = open("output.txt", "w")
text.writelines(output_text)
text.close()

import random

text = open("output.txt", "r")
stuff = text.read()
stuff = stuff.split(" ")
text.close()

num = random.randrange(len(stuff))
print(stuff[num])