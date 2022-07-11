#!/usr/bin/env python
# Name: simpleMath.pl
# License: Released under GPL v2 or higher. Details here http://www.gnu.org/licenses/gpl.html
# Author: Jason Campisi
# Version 1.1.0
# Date: 7/10/2022
# Purpose: Send some math to the program at the command line to calulate & format it with commas.
# Usage: simpleMath.py "insert equation here"
#  So I don't have to do this: echo "50.2*8*260" | bc | xargs /usr/bin/printf "%'d\n" 2>/dev/null

import sys

def addFormatting(number):
    return ("{:,.2F}".format(number))

numbers = sys.argv[1]
print ("This %s yields" % numbers)
print ("     %s" % addFormatting((eval(numbers)) ))