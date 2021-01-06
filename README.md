[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fastscape-lem/fastscape-demo/master?urlpath=lab)
[![Test notebooks](https://github.com/fastscape-lem/fastscape-demo/workflows/Test%20notebooks/badge.svg)](https://github.com/fastscape-lem/fastscape-demo/actions)

# FastScape Demo

This repository contains a collection of [Jupyter](http://jupyter.org/)
notebooks with examples of using the Fastscape software stack for landscape
evolution modeling and topographic analysis.

More information on this website: https://fastscape.org

- [How to run the notebooks?](#how-to-run-the-notebooks)
    - [Run in the cloud (Binder)](#run-in-the-cloud-binder)
    - [Install and run locally (Docker)](#install-and-run-locally-docker)
    - [Install and run locally (Conda)](#install-and-run-locally-conda)
- [How to contribute?](#how-to-contribute)

## How to run the notebooks?

### Run in the cloud (Binder)

You can run the notebooks in your browser without installing anything thanks to
[binder](https://mybinder.org/). Just follow the link below or click on the
"launch binder" badge above and it will launch remotely a new notebook server
for you:

- [Run on binder](https://mybinder.org/v2/gh/fastscape-lem/fastscape-demo/master?urlpath=lab)

This service is for demo purpose only, do not rely on it for doing more serious
work.

### Install and run locally (Docker)

[Docker](https://www.docker.com/) images are built automatically for this
repository. Those images provide the whole computing environment, pre-installed
and pre-configured for running the notebooks. The only requirement is to
have Docker installed on your machine. It is available on all platforms
Linux/Windows/Mac and it can be installed from the Docker website or using one
of your platform's package managers.

Run the command below to first pull the latest image:

```bash
$ docker pull fastscape/fastscape-demo:latest
```

Then run the command below to start the Jupyterlab application from the Docker
container (replace `test-fastscape` by any other name you want to give to your
local container):

```bash
$ docker run -it --name test-fastscape -p 8888:8888 fastscape/fastscape-demo jupyter lab --ip 0.0.0.0
```

You can then enter in your browser the url and token provided to start using the
application.

Check [Docker's documentation](https://docs.docker.com/) for additional run
options, e.g., if you want to use the Jupyterlab application with notebooks or
files on your local filesystem (i.e., not in the container).

When you are done you need to stop (and optionally remove) the container:

``` bash
$ docker stop test-fastscape
$ docker rm test-fastscape
```

### Install and run locally (Conda)

Assuming that you have `git` and [conda](https://conda.io/docs/index.html)
installed, you can install all the packages required to run the notebooks in a
new conda environment using the following commands:

```bash
$ git clone https://github.com/fastscape-lem/fastscape-demo
$ cd fastscape-demo
$ conda env create -f environment.yml
$ conda activate fastscape-demo
```

You also need to install a few Jupyterlab extensions with the following command
(this step won't be required anymore with Jupyterlab >= 3.x):

```bash
$ jupyter labextension install \
    @jupyter-widgets/jupyterlab-manager \
    @pyviz/jupyterlab_pyviz \
    dask-labextension \
    ipygany
```

Finally run the command below to start the Jupyterlab application. It should
open a new tab in your browser.

```bash
$ jupyter lab
```

## How to contribute?

Your contribution is welcome! Your can do so by reporting issues, suggesting new
notebook examples or improvements to the current examples.

A few extra steps are required to prepare your contributions. You can first
update the conda environment using the following command:

```bash
$ conda env update -n fastscape-demo --file environment-dev.yml 
```

This installs a few additional packages like
[pre-commit](https://pre-commit.com/), which is used to ensure that all notebook
cell outputs are cleared before adding or updating notebooks in this git
repository. Run the command below to enable pre-commit (you only need to do this
once):

```bash
$ pre-commit install
```

The script below is useful if you want to ensure that all notebooks are running
without error:

```bash
$ python execute_all_notebooks.py
```

This script (as well as a script to build the Docker image) is run each time you
open or update a pull-request on GitHub.
