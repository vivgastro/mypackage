'''
Determine Andromeda location in ra/dec degrees
'''

from random import uniform
from math import cos, pi

# from wikipedia

ra = '00:42:44.3'
dec = '41:16:09'

# convert to decimal degrees

d, m, s = dec.split(':')
dec = int(d)+int(m)/60+float(s)/3600

h, m, s = ra.split(':')
ra = 15*(int(h)+int(m)/60+float(s)/3600)
ra = ra/cos(dec*pi/180)

NSRC = 1_000_000

# make 1000 stars within 1 degree of Andromeda
ras = []
decs = []
for i in range(NSRC):
    ras.append(ra + uniform(-1,1))
    decs.append(dec + uniform(-1,1))


# now write these to a csv file for use by my other program
with  open('catalog.csv','w', encoding='utf-8') as f:
    print("id,ra,dec", file=f)
    for i in range(NSRC):
        print(f"{0:07d}, {1:12f}, {2:12f}".format(i, ras[i], decs[i]), file=f)
