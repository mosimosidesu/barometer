# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import bmp581

bmp = bmp581.BMP581()

# Oddly first pressure measure after power-on return wrong value.
# so we "burn" one measure
_ = bmp.pressure

print(f"Pressure: {bmp.pressure:.2f}hPa")
print(f"Current altitude: {bmp.altitude:.1f}mts")
# aaa