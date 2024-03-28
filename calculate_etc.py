import math

def absolute_humidity_dew_point(T, HR, P):
    """
    Calculate absolute humidity and dew point from temperature, relative humidity, and atmospheric pressure.

    :param float T: Temperature in degrees Celsius
    :param float HR: Relative humidity in percent
    :param float P: Atmospheric pressure in hPa
    :return: Absolute humidity in g/m^3 and g/kg, and dew point in degrees Celsius
    :rtype: tuple
    """

    # Convert temperature to Kelvin
    T_K = T + 273.15

    # Calculate saturation vapor pressure (Ps) in Pa
    if T >= 0:
        ln_Ps = -6096.9385 / T_K + 21.2409642 - 2.711193e-2 * T_K + 1.673952e-5 * T_K**2 + 2.433502 * math.log(T_K)
    else:
        ln_Ps = -6024.5282 / T_K + 29.32707 + 1.0613868e-2 * T_K - 1.3198825e-5 * T_K**2 - 0.49382577 * math.log(T_K)
    Ps = math.exp(ln_Ps)

    # Calculate actual vapor pressure (e) in Pa
    e = HR / 100 * Ps

    # Calculate absolute humidity (D) in g/m^3
    D = 0.794e-2 * e / (1 + 0.00366 * T)

    # Calculate absolute humidity (HW) in g/kg
    HW = 0.622 * e / (P * 100 - e) * 1000

    # Calculate dew point temperature (td) in degrees Celsius
    y = math.log(e / 611.213)
    if y >= 0:
        td = 13.715 * y + 8.4262e-1 * y**2 + 1.9048e-2 * y**3 + 7.8158e-3 * y**4
    else:
        td = 13.7204 * y + 7.36631e-1 * y**2 + 3.32136e-2 * y**3 + 7.78591e-4 * y**4

    return D, HW, td

def discomfort_index(T, H):
    DI = 0.81 * T + 0.01 * H * (0.99 * T - 14.3) + 46.3
    return DI

def get_discomfort_index(DI):
    discomfort_levels = [
        (55, '\033[34m', '寒い'),
        (60, '\033[36m', '肌寒い'),
        (65, '\033[37m', '何も感じない'),
        (70, '\033[32m', '快い'),
        (75, '\033[33m', '暑くない'),
        (80, '\033[93m', 'やや暑い'),
        (85, '\033[91m', '暑い'),
        (float('inf'), '\033[31m', 'とても暑い')
    ]
    
    for level in discomfort_levels:
        if DI < level[0]:
            return f"{level[1]}{DI:.1f} - {level[2]}\033[0m"