# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import python_bmp581.bmp581 as bmp581

bmp = bmp581.BMP581()

while True:
    for output_data_rate in range(0, 32, 1):
        print("Current Output data rate setting: ", bmp.output_data_rate)
        for _ in range(10):
            print(f"気圧: {bmp.pressure:.2f}hPa")
            print()
            time.sleep(0.5)
        bmp.output_data_rate = output_data_rate
