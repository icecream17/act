#
# This is the first time trying python. Because js can't really edit files.
# Hopefully I can successfully update the text.
#

import random

f = open("act", "r")

moves = ["up", "down", "left", "right"]
text = f.read()

a = random.randrange(1, 1000) % 2

b = (moves.index(text) + 4) % 4

if a > b:
  c = moves[random.randrange(1, 4)]
else:
  c = moves[b]

f.write(c)
f.close()
