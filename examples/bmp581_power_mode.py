# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import bmp581

bmp = bmp581.BMP581()

bmp.power_mode = bmp581.NORMAL

while True:
    for power_mode in bmp581.power_mode_values:
        print("Current Power mode setting: ", bmp.power_mode)
        for _ in range(10):
            print(f"気圧: {bmp.pressure:.2f}hPa")
            print()
            time.sleep(0.5)
        bmp.power_mode = power_mode
