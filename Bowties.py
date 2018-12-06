"""
file: Bowties.py
author: Sam Dzialo
Email: sad8333@rit.edu
language: python3.7
description: Lab03 solution
"""
import turtle as tt


def bowtie(size):
    """"The purpose of the bowtie function is to create a bowtie
    shape with a colored circle in the center"""
    tt.pencolor("purple")
    tt.down()
    tt.speed(0)
    tt.left(30)
    tt.forward(size)
    tt.right(120)
    tt.forward(size)
    tt.right(120)
    tt.forward(size*2)
    tt.left(120)
    tt.forward(size)
    tt.left(120)
    tt.forward(size)
    tt.right(30)
    tt.fillcolor("red")
    tt.forward(size/4)
    tt.left(90)
    tt.begin_fill()
    tt.circle(size/4)
    tt.end_fill()
    tt.up()
    tt.right(90)
    tt.forward(-size/4)
    """Turtle starts and end in the center, facing east"""


def main():
    """The purpose of the ask function is to
    ask the user for the necessary variables."""
    tt.setup()
    size = int(input("Enter the Size: "))
    depth = int(input("Enter the amount of levels: "))
    bowtie_rec(size, depth)
    tt.done()


def bowtie_rec(size, levels):
    """takes the variables from ask()
    and then recursively calls bowtie."""
    if levels == 0:
        pass
    elif levels == 1:
        bowtie(size)
    else:
        bowtie(size)
        tt.left(30)
        tt.forward(2*size)
        bowtie_rec(size/3, levels-1)
        tt.forward(-2*size)
        tt.left(120)
        tt.forward(2*size)
        bowtie_rec(size/3, levels-1)
        tt.forward(-2*size)
        tt.left(60)
        tt.forward(2*size)
        bowtie_rec(size/3, levels-1)
        tt.forward(-2*size)
        tt.left(120)
        tt.forward(2*size)
        bowtie_rec(size/3, levels-1)
        tt.forward(-2*size)
        tt.left(30)
    """The turtle ends at the same sport that it started facing east."""


main()
