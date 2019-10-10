import os

import numpy as np
import pyvista as pv


# enable panel display on headless servers
os.system('/usr/bin/Xvfb :99 -screen 0 1024x768x24 &')
os.environ['DISPLAY'] = ':99'


def create_pyvista_grid(dataset, warp_by_scalar=True, scale_factor=1.,
                        var_names=None):
    x = dataset.x.values
    y = dataset.y.values
    z = [0]

    grid = pv.StructuredGrid(*np.meshgrid(y, x, z))

    vnames = ['topography__elevation']

    if var_names is not None:
        vnames += var_names

    for k in vnames:
        grid.point_arrays[k] = dataset[k].values.ravel()

    if warp_by_scalar:
        return grid.warp_by_scalar(scalars='topography__elevation',
                                   factor=scale_factor)

    else:
        return grid
