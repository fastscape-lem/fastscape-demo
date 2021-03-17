import xarray as xr
from datashader import geo


def map_xr_func(func, da, time_dim=None, batch_dim=None, **kwargs):
    """Map a DataArray compatible function, maybe brodcasting it over
    the time and/or batch dimension(s).

    Parameters
    ----------
    func : callable
        Any function accepting a :class:`xarray.DataArray` as first and
        only positional argument and returning another DataArray.
    da : :class:`xarray.DataArray`
        The DataArray object used to map ``func``.
    time_dim : str, optional
        Time dimension label.
    batch_dim : str
        Batch dimension label.
    **kwargs
        Keyword arguments passed to ``func``.

    Returns
    -------
    result : :class:`xarray.DataArray`
        The resulting DataArray.

    """
    if batch_dim is not None:
        res_t = []
        for _, da_t in da.groupby(batch_dim):
            res_t.append(map_xr_func(func, da, time_dim=time_dim, **kwargs))

        result = xr.concat(res_t, batch_dim)

    elif time_dim is not None:
        result = da.groupby(time_dim).map(func, shortcut=False, **kwargs)

    else:
        result = func(da, **kwargs)

    return result


def hillshade(ds, groupby=None, elev_var='topography__elevation', **kwargs):
    elev = ds[elev_var]

    return map_xr_func(geo.hillshade, elev, time_dim=groupby)
