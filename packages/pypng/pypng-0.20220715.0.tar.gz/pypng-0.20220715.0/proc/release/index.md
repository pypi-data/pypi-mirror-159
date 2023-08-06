# PyPNG Release Procedure

## Overview

These modified instructions have not yet been tested.

With `pip`, we build a _wheel_ file and a source distribution
`.tar.gz`.
With `twine` we upload those to PyPI and the GitLab project
repository.

## Tool Prerequisites

You'll need `pip` and `twine`.

This document cannot describe any detailed method for installing `pip`,
but I recommend using `conda` or `brew` to get Python and pip
together.

`twine` can be installed with `python -m pip install twine`.

## Release procedure

At top-level...

Choose the next version number.
As of 2022 this of the form: 0.CCYYMMDD.z

Thus in x.y.z notation: x is 0; y is the 8-digit ISO 8601 data;
z is the patch number (typically 0, unless you make more than
one release a day).

Edit ``code/png.py`` and ``setup.cfg`` for new version number.
Then ``git commit`` this.

Get release notes into ``README.md`` somehow.

Get the latest git change hash::

    git log -n1 | sed q

Set the `PYPNG_VERSION` variable (extracted from `code/png.py`):

    . ./pypng-version

Add a tag for this release (the tags have this format so that
the automatically generated tarballs from github.com have the
right URL).

    git tag -a pypng-$PYPNG_VERSION -m "PyPNG release $PYPNG_VERSION"

and push:

    git push --tags origin HEAD

Make a clean clone:

    cd ${PWD%pypng*}
    git clone pypng pypng-$PYPNG_VERSION
    cd pypng-$PYPNG_VERSION

Build a wheel file:

    pip wheel .

It's possible at this point that you might want to smoke-test the actual
release binary.  Let's assume that the release binary is good to go.

cd back into your main development directory::

    cd ${PWD%pypng*}pypng

Check that the `sh dock.sh` command populated
the `dist/` directory in the original `pypng` directory.

    ls dist

(which it won't have done)

Documentation magically appears on ReadTheDocs.
In some previous versions, docker was used to build the
documentation which was bundled into an `sdist`.

    sphinx-build -N -d sphinx-crud -a man html

Upload to PyPI:

    pip -m twine upload *.whl

(If it complains about "you must be identified" then use
"python setup.py register" first; unlikely to work since i
deleted setup.py)

## Record Release

Make a record in ``release/index.txt``

Consider adding dist artefacts to `dist` branch


# END
