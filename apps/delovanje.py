#!/user/bin/env python3
# -*- coding:utf-8 -*-

# from CameraLED import CameraLED
import time
from datetime import datetime, timedelta


# čas sončnega vzhoda in zahoda
from sonce import pozicija_sonca

# Podatki o soncu
sonce = pozicija_sonca()
soncni_zahod = sonce['zahod']
soncni_vzhod = sonce['vzhod']

# Kalkulacija trenutnega časa
offset_ur = 0  # pozitivno število
trenutni_cas = datetime.now()
trenutni_cas = trenutni_cas + timedelta(hours=offset_ur)
trenutni_cas = trenutni_cas.time()

# Led modul
led = CameraLED()

# Delovanje
while True:
    if soncni_zahod > trenutni_cas > soncni_vzhod:
        # led = off, od sončnega vzhoda do zahoda
        led.off()
        # print('led=off')
        # time.sleep(1)
    else:
        # led = on, do sončnega zahoda do vzhoda
        led.on()
        # print('led=on')
        # time.sleep(1)
