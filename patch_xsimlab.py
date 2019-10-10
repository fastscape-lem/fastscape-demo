import xsimlab as xs
from xsimlab.xr_accessor import _maybe_get_model_from_context

import xarray as xr

import dask.array as da
from dask import delayed


def _run_model_batch(self, dim, model=None, client=None):
    model = _maybe_get_model_from_context(model)

    out_ds_list = []

    for _, in_ds in self._ds.groupby(dim):
        out_ds = delayed(in_ds.xsimlab.run)(model=model)
        out_ds_list.append(out_ds)

    out_ds = delayed(xr.concat)(out_ds_list, dim, data_vars='different')

    return out_ds.compute().chunk({dim: 1})


xs.SimlabAccessor.run_model_batch = _run_model_batch
