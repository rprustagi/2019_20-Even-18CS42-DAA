#!/usr/bin/env python3
"""
# the original program sorting_animate.py has been edited
# to display only selection sort with number of items
# to sorted can be defined at run time.
# RPRustagi

         sorting_animation.py

A minimal sorting algorithm animation:
Sorts a shelf of 10 blocks using insertion
sort, selection sort and quicksort.

Shelfs are implemented using builtin lists.

Blocks are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press space button
 ---------------------------------------
"""
from turtle import *
import random
import sys


class Block(Turtle):

    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False)
        self.penup()
        self.shapesize(size * 1.0, 1.5, 2) # square-->rectangle
        self.fillcolor("yellow")
        self.showturtle()

    def glow(self):
        self.fillcolor("red")

    def unglow(self):
        self.fillcolor("yellow")

    def __repr__(self):
        return "Block size: {0}".format(self.size)


class Shelf(list):

    def __init__(self, y):
        "create a shelf. y is y-position of first block"
        self.y = y
        self.x = -250

    def push(self, d):
        width, _, _ = d.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        d.sety(self.y + y_offset)
        d.setx(self.x + 34 * len(self))
        self.append(d)

    def _close_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)

    def _open_gap_from_i(self, i):
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)

    def pop(self, key):
        b = list.pop(self, key)
        b.glow()
        b.sety(200)
        self._close_gap_from_i(key)
        return b

    def insert(self, key, b):
        self._open_gap_from_i(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        width, _, _ = b.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()

def ssort(shelf):
    length = len(shelf)
    for j in range(0, length - 1):
        imin = j
        for i in range(j + 1, length):
            if shelf[i].size < shelf[imin].size:
                imin = i
        if imin != j:
            shelf.insert(j, shelf.pop(imin))
        textinput("Sort Progress", "Press any keoy to continue")

def randomize():
    disable_keys()
    clear()
    target = list(range(sort_nums))
    random.shuffle(target)
    for i, t in enumerate(target):
        for j in range(i, len(s)):
            if s[j].size == t + 1:
                s.insert(i, s.pop(j))
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def show_text(text, line=0):
    line = 20 * line
    goto(0,-250 - line)
    write(text, align="center", font=("Courier", 16, "bold"))

def start_ssort():
    disable_keys()
    clear()
    show_text("Selection Sort")
    ssort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()

def init_shelf():
    global s

    s = Shelf(-200)
    vals = list(range(1, sort_nums + 1))
    random.shuffle(vals)
    for i in vals:
        s.push(Block(i))

def disable_keys():
    onkey(None, "s")
    onkey(None, "r")

def enable_keys():
    onkey(start_ssort, "s")
    onkey(randomize, "r")
    onkey(bye, "space")

def main():
    getscreen().clearscreen()
    hideturtle(); penup()
    init_shelf()
    show_text(instructions1)
    show_text(instructions2, line=1)
    enable_keys()
    listen()
    return "EVENTLOOP"

instructions1 = "press s for selection sort, r to randomize"
instructions2 = "spacebar to quit"

if __name__=="__main__":
    global sort_nums
    sort_nums = 10
    if (len(sys.argv) > 1):
        sort_nums = int(sys.argv[1])
    msg = main()
    mainloop()
