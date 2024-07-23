# TFIDF (term frequency * inverse document frequency) is a weighting scheme
# for terms in documents, or in our case, tags for songs.

# TF for tag t in song s is defined as:
# number of times t appears in s / total number of tags in s

# However, in our case, each tag can appear only once per song, so:
# 1 / total number of tags in s

# IDF for tag t is defined as:
# log ( total number of songs / number of songs containing t )

# Finally, TFIDF = TF * IDF

# Given a file of song IDs and their tags, like:

# 1 electronic house
# 2 rock metal spanish
# 3 jungle drum&bass
# 4 pop r&b soul
# ...

# write a short program that prints out the TFIDF weighted tags, like:

# 1 electronic:0.66 house:0.82
# 2 rock:0.51 metal:0.49 spanish:1.35
# 3 jungle:1.06 drum&bass:0.72
# 4 pop:0.15 r&b:0.21 soul:0.36
# ...

# The file is called /home/coderpad/data/song_tag_assignments
import math

with open('/home/coderpad/data/song_tag_assignments') as f:
    lines = [line for line in f]

d = {}
# n = number of lines m number of words O(n*m)
for line in lines:
    words = set(line.split()[1:])
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1

# n = number of lines m number of words O(n*m)
for line in lines:
    words = line.split()[1:]
    TF = {}
    for word in words:
        if word in TF:
            TF[word] = TF[word] + 1/len(words)
        else:
            TF[word] = 1/len(words)
    

TFIDF = {}
for word in d:
    TFIDF[word] = math.log(len(lines) / d[word]) * TF[word]

print(TFIDF)
