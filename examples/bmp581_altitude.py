# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

from smbus2 import SMBus
from gpiozero import I2CDevice
from python_bmp581 import bmp581

# I2Cバス1を開く
bus = SMBus(1)

# SDAとSCLに対応するGPIOピンを設定
SDA = 2
SCL = 3

# I2Cデバイスを作成
i2c = I2CDevice(bus, SDA, SCL)

bmp = bmp581.BMP581(i2c)

# Oddly first pressure measure after power-on return wrong value.
# so we "burn" one measure
_ = bmp.pressure

print(f"Pressure: {bmp.pressure:.2f}kPa")
print(f"Current altitude: {bmp.altitude:.1f}mts")
