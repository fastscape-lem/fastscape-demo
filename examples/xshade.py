import datashader.geo as dgeo


def hillshade(ds, groupby=None, elev_var='topography__elevation', **kwargs):
    elev = ds[elev_var]
    
    if groupby is not None:
        # TODO: use shortcut=True
        # https://github.com/holoviz/datashader/issues/871
        hshade = elev.groupby(groupby).apply(dgeo.hillshade, shortcut=False,
                                             **kwargs)
    else:
        hshade = dgeo.hillshade(elev, **kwargs)
    
    return hshade

    # TODO: related to todo above
    #return (hshade
    #        .rename(dim_0='y', dim_1='x')
    #        .assign_coords(x=ds.x, y=ds.y))
