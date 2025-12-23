"""Some functions related to finite volume."""


def generate_grid(x_size, x_num):
    """generate_grid Generate a 1D grid with `x_num` elements of size `x_size`.

    Parameters
    ----------
    x_size : float
    x_num : int

    Returns
    -------
    list
        Mesh
    """
    x_grid = []  # the grid of spcae discretization
    for i in range(0, x_size):
        x_grid.append((i + 0.5) * (1.0 / x_num))
    return x_grid
