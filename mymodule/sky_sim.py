'''
Determine Andromeda location in ra/dec degrees

Author: Vivek Gupta (vivek.gupta@csiro.au)
Date: 20/03/2023
'''

import argparse
from helpers import make_stars, get_coords

def write_catalog(fname :str , coords: list):
    r'''
    Writes the Star coords to a file in csv format

    Parameters
    ----------
    fname: str
            Name of the output csv file
    coords: list
            List of tuples which contains the coords (RA, DEC) of each star

    Raises
    ------
    ValueError: If len(coords) < 1
    '''
    nsrc = len(coords)
    if nsrc < 1:
        raise ValueError(f"The number of start to write need to be > 0, given {nsrc}")

    # now write these to a csv file for use by my other program
    with  open(fname,'w', encoding='utf-8') as f:
        print("id,ra,dec", file=f)
        for i in range(nsrc):
            print(f"{i:07d}, {coords[i][0]:12f}, {coords[i][1]:12f}", file=f)

def main():
    r'''
    The main function.
    Don't import it!
    '''
    galcoord = get_coords(args.gal)
    star_coords = make_stars(galcoord, args.nstars)
    write_catalog(fname=args.outname, coords = star_coords)

if __name__ == '__main__':
    a = argparse.ArgumentParser(prog='sky_sim')
    a.add_argument('-gal', type=str,
                   help="Name of the Galaxy (def = M31)", default="M31")
    a.add_argument('-nstars', type=int,
                   help="No. of stars to simulate (def = 1 mil)", default="1_000_000")
    a.add_argument('-o', type=str, dest='outname',
                   help="Name of the output catalog (def = catalog.csv)", default="catalog.csv")

    args = a.parse_args()
    main()
