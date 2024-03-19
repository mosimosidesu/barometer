# SPDX-FileCopyrightText: Copyright (c) 2023 Jose D. Montoya
#
# SPDX-License-Identifier: MIT

import time
from smbus2 import SMBus
#from gpiozero import I2CDevice
from python_bmp581 import bmp581

# I2Cバス1を開く
bus = SMBus(1)

# SDAとSCLに対応するGPIOピンを設定
SDA = 5
SCL = 3

# I2Cデバイスを作成
i2c = I2CDevice(bus, SDA, SCL)

bmp = bmp581.BMP581(i2c)

bmp.pressure_oversample_rate = bmp581.OSR16

while True:
    for pressure_oversample_rate in bmp581.pressure_oversample_rate_values:
        print(
            "Current Pressure oversample rate setting: ", bmp.pressure_oversample_rate
        )
        for _ in range(10):
            print(f"Pressure: {bmp.pressure:.2f}kPa")
            print()
            time.sleep(0.5)
        bmp.pressure_oversample_rate = pressure_oversample_rate
