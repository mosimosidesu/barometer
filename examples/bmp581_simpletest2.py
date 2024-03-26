# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import python_bmp581.bmp581 as bmp581

bmp = bmp581.BMP581()

# Oddly first pressure measure after power-on return wrong value.
# so we "burn" one measure
_ = bmp.pressure


print(f"気温: {bmp.temperature:.2f}°C")
print(f"気圧: {bmp.pressure:.2f}hPa")
print(f"高度: {bmp.altitude:.1f}m")