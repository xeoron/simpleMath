#!/usr/bin/env python
# Name: simpleMath.pl
# License: Released under GPL v2 or higher. Details here http://www.gnu.org/licenses/gpl.html
# Author: Jason Campisi
# Date: 6/3/2022
# Purpose: Send some math to the program at the command line to do and format it with commas.
# Usage: simpleMath.py "insert equation here"
#  So I don't have to do this: echo "50.2*8*260" | bc | xargs /usr/bin/printf "%'d\n" 2>/dev/null

import sys

def addCommas(number):
    return ("{:,}".format(number))

numbers = sys.argv[1]
print ("This %s yields" % numbers)
print ("     %s" % addCommas(eval(numbers)))