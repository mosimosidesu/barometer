# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import bmp581

bmp = bmp581.BMP581()

bmp.pressure_oversample_rate = bmp581.OSR16

while True:
    for pressure_oversample_rate in bmp581.pressure_oversample_rate_values:
        print(
            "Current Pressure oversample rate setting: ", bmp.pressure_oversample_rate
        )
        for _ in range(10):
            print(f"気圧: {bmp.pressure:.2f}hPa")
            print()
            time.sleep(0.5)
        bmp.pressure_oversample_rate = pressure_oversample_rate
