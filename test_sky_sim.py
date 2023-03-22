from numpy import testing
from src.sky_sim import get_coords

def test_module_import():
    try:
        from src import sky_sim
    except Exception as E:
        raise ImportError("Could not import sky_sim from src due to \n\n"+ str(E))



def test_andromedas_coords():
    coords = get_coords()
    answer = (10.68479, 41.26906)
    testing.assert_allclose(coords, answer, atol=1./3600)

