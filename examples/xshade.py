import datashader.geo as dgeo


def hillshade(ds, groupby=None, elev_var='topography__elevation', **kwargs):
    elev = ds[elev_var]
    
    if groupby is not None:
        hshade = elev.groupby(groupby).apply(dgeo.hillshade, shortcut=True,
                                             **kwargs)
    else:
        hshade = dgeo.hillshade(elev, shortcut=True, **kwargs)
    
    return (hshade
            .rename(dim_0='y', dim_1='x')
            .assign_coords(x=ds.x, y=ds.y))
