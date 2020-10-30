import sys
import pygrib
import os
command=sys.argv[1]
currentDIR = os.getcwd()
filename = sys.argv[2]
# read the file
grbs=pygrib.open(currentDIR + '/' + filename)
commandlist= ['showvar']
if command=='showvar':
    grb = grbs.select()[:]
    print(grb)
else:
    print('%s is not a valid command, try %s' %(command, commandlist))
