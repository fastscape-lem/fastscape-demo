#!/usr/bin/env python3
from pathlib import Path
import shutil
import sys
import time
import warnings

import papermill as pm


if __name__ == "__main__":

    for pn in sorted(Path.cwd().rglob("*.ipynb")):
        # skip notebook checkpoints
        if pn.match(".ipynb_checkpoints/*.ipynb"):
            continue

        # remove zarr datasets (if any)
        for pzarr in pn.parent.rglob("*.zarr"):
            shutil.rmtree(pzarr)

        # execute notebook
        print(f"executing {pn}")
        sys.stdout.flush()
        time.sleep(1)

        with warnings.catch_warnings():
            # ignore papermill warning due to no notebook file output.
            warnings.filterwarnings("ignore", category=UserWarning)
            pm.execute_notebook(pn, "/dev/null", kernel_name="python3", cwd=pn.parent)

        sys.stdout.flush()
        time.sleep(1)
