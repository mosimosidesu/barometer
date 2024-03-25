# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import bmp581

bmp = bmp581.BMP581()

while True:
    print(f"気温: {bmp.temperature:.2f}°C")
    print()
    time.sleep(0.5)
