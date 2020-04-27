#
# This is the first time trying python. Because js can't really edit files.
# Hopefully I can successfully update the text.
#

import os, requests, time, random

move = "up"

# Mostly stolen from https://github.com/programical/gitland/blob/master/server.py
# Since I don't know anything
  
def update():
  moves = ["up", "down", "left", "right"]
  
  a = random.randrange(1, 1000) % 2
  b = (moves.index(move) + 4) % 4
  
  if a > b:
    c = moves[random.randrange(1, 4)]
  else:
    c = moves[b]
   
  move = c
  
  open("map", "w").write(c)


while True:
  update()
  time.sleep(420)
