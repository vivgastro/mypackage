from numpy import testing

def test_module_import():
    try:
        from src import sky_sim
    except Exception as E:
        raise ImportError("Could not import sky_sim from src due to \n\n"+ str(E))

def test_andromedas_coords():
    from src import sky_sim
    coords = sky_sim.get_coords()
    answer = (10.68479, 41.26906)
    testing.assert_allclose(coords, answer, atol=1./3600)

