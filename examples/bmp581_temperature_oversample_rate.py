# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import python_bmp581.bmp581 as bmp581

bmp = bmp581.BMP581()

bmp.temperature_oversample_rate = bmp581.OSR4

while True:
    for temperature_oversample_rate in bmp581.temperature_oversample_rate_values:
        print(
            "Current Temperature oversample rate setting: ",
            bmp.temperature_oversample_rate,
        )
        for _ in range(10):
            temp = bmp.temperature
            print(f"気温: {bmp.temperature:.2f}°C")
            print()
            time.sleep(0.5)
        bmp.temperature_oversample_rate = temperature_oversample_rate
