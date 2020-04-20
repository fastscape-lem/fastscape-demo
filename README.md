[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/fastscape-lem/fastscape-demo/master?urlpath=lab)

# FastScape Demo

Some [Jupyter](http://jupyter.org/) notebooks showing how to build,
customize and run landscape evolution models using the
[xarray-simlab](https://github.com/benbovy/xarray-simlab) modelling
framework and the model components available in
[fastscape](https://github.com/fastscape-lem/fastscape).

## How to run the notebooks?

You can try running the notebooks from your browser without installing
anything thanks to [binder](https://mybinder.org/). Just click on the
"launch binder" badge above and it will launch remotely a new notebook
server for you. This service is for demo purpose only, do not rely on
it for doing more serious work.

Alternatively, you can run the notebook server on your own
machine. Assuming that you have `git` and
[conda](https://conda.io/docs/index.html) installed, you just need to
run the following commands to install and activate the environment:

```
   $ git clone https://github.com/fastscape-lem/fastscape-demo
   $ cd fastscape-demo
   $ conda env create -f environment.yml
   $ source activate fastscape-demo
```

Note that on windows platforms, the last command is simply `activate
fastscape-demo`. For recent conda versions (4.4+), you can use
`conda activate fastscape-demo`.

Then run the command below to start the notebook server. It should open
a new tab in your browser.

```
    $ jupyter notebook
```
