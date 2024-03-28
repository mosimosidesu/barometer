from python_bmp581 import bmp581
from scd30_i2c import SCD30
#import calculate_etc
from calculate_etc import absolute_humidity_dew_point
from calculate_etc import discomfort_index
from calculate_etc import print_discomfort_index
import logging
import time


# BMP581
bmp = bmp581.BMP581()

# Oddly first pressure measure after power-on return wrong value.
# so we "burn" one measure
_ = bmp.pressure

scd30 = SCD30()

logging.basicConfig(level=logging.INFO)

retries = 30
logging.info("Probing sensor...")
ready = None
while ready is None and retries:
    try:
        ready = scd30.get_data_ready()
    except OSError:
        # The sensor may need a couple of seconds to boot up after power-on
        # and may not be ready to respond, raising I2C errors during this time.
        pass
    time.sleep(1)
    retries -= 1
if not retries:
    logging.error("Timed out waiting for SCD30.")
    exit(1)

logging.info("Link to sensor established.")
logging.info("Getting firmware version...")

logging.info(f"Sensor firmware version: {scd30.get_firmware_version()}")

# 2 seconds is the minimum supported interval.
measurement_interval = 4

logging.info("Setting measurement interval to 2s...")
scd30.set_measurement_interval(measurement_interval)
logging.info("Enabling automatic self-calibration...")
scd30.set_auto_self_calibration(active=True)
logging.info("Starting periodic measurement...")
scd30.start_periodic_measurement(int(bmp.pressure))

time.sleep(measurement_interval)

logging.info(f"ASC status: {scd30.get_auto_self_calibration_active()}")
logging.info(f"Measurement interval: {scd30.get_measurement_interval()}s")
logging.info(f"Temperature offset: {scd30.get_temperature_offset()}'C")

try:
    while True:
        if scd30.get_data_ready():
            measurement = scd30.read_measurement()
            if measurement is not None:
                humidity_dew = absolute_humidity_dew_point(bmp.temperature, measurement[2], bmp.pressure)
                print(f"気温: {bmp.temperature:.2f}°C")
                print(f"相対湿度: {measurement[2]:.2f}%")
                print(f"絶対湿度: {humidity_dew[0]:.2f}g/m^3")
                print(f"露点温度: {humidity_dew[3]:.2f}°C")
                print(f"気圧: {bmp.pressure:.2f}hPa")
                print(f"CO2: {measurement[0]:.2f}ppm")
                time.sleep(measurement_interval)
        else:
            time.sleep(0.2)

except KeyboardInterrupt:
    logging.info("Stopping periodic measurement...")
    scd30.stop_periodic_measurement()
