# dataverse_pooch

`dataverse_pooch` is a thin wrapper to manage data stored in a [DataVerse](https://github.com/IQSS/dataverse)
repository using the excellent [pooch](https://github.com/fatiando/pooch) library. Simply use
`dataverse_pooch.create` instead of `pooch.create` and you can access your dataset on-demand,
benefitting from `pooch`'s caching.

## Installation

You can install from PyPI or have your Python package depend on `dataverse_pooch`:

```
python -m pip install dataverse_pooch
```

## Usage

A typical use case looks like this:

```
import dataverse_pooch
import pooch

# Define your pooch
MYDATA = dataverse_pooch.create(
    server="https://heidata.uni-heidelberg.de",
    doi="10.11588/data/TJNQZG",
    path=pooch.os_cache("mypackage")
)

# Access data using fetch
filename = MYDATA.fetch("nkd_sgm.geojson")

# The 'filename' variable now contains the absolute path of the downloaded
# file. If you downloaded it before, it was taken from the cache.
```

Note that `dataverse_pooch.create` forwards all arguments to `pooch.create` except
for the `server` and `doi` ones which are used to access the data repository.
`dataverse_pooch` will automatically create a Pooch registry for you which itself
is cached with `pooch`.

## Known limitations

`dataverse_pooch` currently only handles the latest published version of a dataset,
as it does not perform any authentication.
