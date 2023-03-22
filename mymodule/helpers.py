from random import uniform
from astroquery.ipac.ned import Ned

def get_coords(galname: str="M31"):
    r'''
    Gets the coordinates (RA, DEC) from NED using astroquery

    Parameters
    ----------
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

def make_stars(gal_coord: tuple, NSRC: int=1_000_000):
    r'''
    Makes NSRC stars around the specified coords

    Parameters
    ----------
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
