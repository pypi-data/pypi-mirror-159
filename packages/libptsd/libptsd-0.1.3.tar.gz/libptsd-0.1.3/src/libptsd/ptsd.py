#!/usr/bin/env python3

import os
import sys
import subprocess

""" PTSD: Post Traumatic StanDard """
""" A new standard library for programmers that has PTSD with their projects. """

argv = sys.argv


# File Manipulation
def fileOpen(file, mode):
    open(file, mode)    
def fileRead(file):
    f = open(file, 'r')
    printf("%s" % f.read())

# String Outputs
def printf(string):
    sys.stdout.write(f"{string}")
def eprintf(string):
    sys.stderr.write(f"{string}")

# OS System Commands 
def system(command):
    subprocess.run(command, shell=True)
