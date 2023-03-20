'''
Determine Andromeda location in ra/dec degrees

Author: Vivek Gupta (vivek.gupta@csiro.au)
'''

from random import uniform
from math import cos, pi
from astroquery.ned import Ned


def get_coords(galname="M31"):
    '''
    Gets the coordinates (RA, DEC) from NED using astroquery

    Params
    ------
    galname: str
            Name of the galaxy

    Returns
    -------
    coords: tuple
            A tuple containing the RA and Dec in degrees as floats
    '''

    result_table = Ned.query_object(galname)
    RA = result_table['RA'].value[0]
    DEC = result_table['DEC'].value[0]

    return (RA, DEC)

def make_stars(gal_coord, NSRC=1_000_000):
    '''
    Makes NSRC stars around the specified coords

    Params
    ------
    gal_coord: tuple
            A tuple containing the RA and DEC as floats
    NSRC:   int
            An integer specifying the number of stars to generate

    Returns
    -------
    coords: list
            A list of tuples which contains the coords of each star
    '''
    ras = []
    decs = []

    RA, DEC = gal_coord
    for i in range(NSRC):
        ras.append(RA + uniform(-1, 1))
        decs.append(DEC + uniform(-1, 1))

    return [(ras[i], decs[i]) for i in range(NSRC)]

def write_catalog(fname, coords):
    '''
    Writes the Star coords to a file in csv format

    Params
    ------
    fname: str
            Name of the output csv file
    coords: list
            List of tuples which contains the coords (RA, DEC) of each star
    '''
    nsrc = len(coords)
    # now write these to a csv file for use by my other program
    with  open(fname,'w', encoding='utf-8') as f:
        print("id,ra,dec", file=f)
        for i in range(nsrc):
            print(f"{i:07d}, {coords[i][0]:12f}, {coords[i][1]:12f}", file=f)

def main():
    '''
    The main function
    '''
    galcoord = get_coords("M31")
    star_coords = make_stars(galcoord)
    write_catalog(fname="catalog.csv", coords = star_coords)

if __name__ == '__main__':
    main()
