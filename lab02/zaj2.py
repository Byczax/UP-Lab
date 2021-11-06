#!/usr/bin/env python2
import time
import math
from pyModbusTCP.client import ModbusClient

REGISTERS_PHASE_VOLTAGE_L1_TO_N = 4098
REGISTERS_LINE_CURRENT_L1 = 4112
REGISTERS_APPARENT_POWER = 4136
REGISTERS_REACTIVE_POWER = 4152
REGISTERS_PHASE_COS_PHI = 4128
REGISTERS_POWER_FACTOR = 4120
REGISTERS_REACTIVE_POWER = 4152
REGISTERS_PHASE_TANGENT_PHI = 4184
REGISTERS_ACTIVE_POWER = 4144


def get_fourbyte_value(connection, address):
    # ms2b - most significant two bytes
    # ls2b - least significant two bytes
    ms2b, ls2b = connection.read_holding_registers(address, 2)
    return ms2b * (2 ** 16) + ls2b


# system uzupelnieniowy
def get_u2(num):
    if num & (1 << 31) == 0:
        return num
    else:
        return num - 2 ** 32


def main():
    c = ModbusClient(
        host="156.17.41.18", port=502, unit_id=1, auto_open=True, auto_close=True
    )

    while True:
        voltage = get_fourbyte_value(c, REGISTERS_PHASE_VOLTAGE_L1_TO_N) / 1000.0
        current = get_fourbyte_value(c, REGISTERS_LINE_CURRENT_L1) / 1000.0
        apparent_power = get_fourbyte_value(c, REGISTERS_APPARENT_POWER)
        phase_cosinus = get_u2(get_fourbyte_value(c, REGISTERS_PHASE_COS_PHI)) / 1000.0
        power_factor = get_u2(get_fourbyte_value(c, REGISTERS_POWER_FACTOR)) / 1000.0
        reactive_power = get_u2(get_fourbyte_value(c, REGISTERS_REACTIVE_POWER))
        reactive_power = get_u2(get_fourbyte_value(c, REGISTERS_REACTIVE_POWER))
        tang = get_u2(get_fourbyte_value(c, REGISTERS_PHASE_TANGENT_PHI)) / 100000.0
        active_power = get_u2(get_fourbyte_value(c, REGISTERS_ACTIVE_POWER))

        sinus = tang * phase_cosinus

        calculated_apparent_power = voltage * current
        calculated_real_power = math.fabs(voltage * current * phase_cosinus)
        calculated_reactive_power = -100 * current * voltage * sinus

        print("")
        print("Voltage: {} V".format(voltage))
        print("Current: {} A".format(current))
        print("Power factor: {}".format(power_factor))
        print("Cos: {}".format(phase_cosinus))
        print(
            "Real/active power: read = {} W, calculated = {} W".format(
                active_power, calculated_real_power
            )
        )
        print(
            "Reactive power: read = {}var, calculated = {} var".format(
                reactive_power, calculated_reactive_power
            )
        )
        print(
            "Apparent power: read = {} VA, calculated = {} VA".format(
                apparent_power, calculated_apparent_power
            )
        )

        time.sleep(0.1)


if __name__ == "__main__":
    main()
