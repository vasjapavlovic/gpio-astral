#!/user/bin/env python3
# -*- coding:utf-8 -*-

# from CameraLED import CameraLED
import time
import datetime

# čas sončnega vzhoda in zahoda
from sonce import pozicija_sonca

# Podatki o soncu
sonce = pozicija_sonca()
soncni_zahod = sonce['zahod'].time()
soncni_vzhod = sonce['vzhod'].time()

# Kalkulacija trenutnega časa
trenutni_cas = datetime.datetime.now().time()
offset_ur = 5

# Led modul
# led = CameraLED()


while True:
    if soncni_zahod > trenutni_cas > soncni_vzhod:
        # led = off, od sončnega vzhoda do zahoda
        # led.off()
        print('led=off')
        time.sleep(1)
    else:
        # led = on, do sončnega zahoda do vzhoda
        # led.on()
        print('led=on')
        time.sleep(1)
