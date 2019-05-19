#!/user/bin/env python3
# -*- coding:utf-8 -*-

import time
import datetime
from astral import Location


def pozicija_sonca():
    """
    Pridobitev podatkov o času sončnega vzhoda in sončnega zahoda

    Astral modul:
    https://astral.readthedocs.io/en/stable/index.html
    """

    # Določitev lokacije
    l = Location()
    l.name = 'Grgar, Breg'
    l.region = 'Goriška'
    l.latitude = 45.999142
    l.longitude = 13.682394
    l.timezone = 'CET'
    l.elevation = 297 # 297m, 974.41feet
    sonce = l.sun()

    # Sončni vzhod
    soncni_vzhod = sonce['sunrise'].time()

    # Sončni zahod
    soncni_zahod = sonce['sunset'].time()

    return {
        'vzhod': soncni_vzhod,
        'zahod': soncni_zahod
        }