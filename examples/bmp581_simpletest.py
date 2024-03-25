# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
import bmp581

bmp = bmp581.BMP581()

# Oddly first pressure measure after power-on return wrong value.
# so we "burn" one measure
_ = bmp.pressure

while True:
    print(f"気圧: {bmp.pressure:.2f}hPa")
    print()
    time.sleep(0.5)
