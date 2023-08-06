import dataverse_pooch
import os


def test_heidata():
    nakadake = dataverse_pooch.create(
        server="https://heidata.uni-heidelberg.de", doi="10.11588/data/TJNQZG"
    )

    assert os.path.exists(nakadake.fetch("nkd_fpl_slope_LT.json"))
