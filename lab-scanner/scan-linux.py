#!/usr/bin/env python3
import sane
import sys
import os
import datetime

device_address = 'escl:http://192.168.1.6:443'
sane.init()
device = sane.open(device_address)

supported_resolutions = next(
    filter(lambda opt: opt[1] == 'resolution', device.get_options()))[8]
supported_modes = next(
    filter(lambda opt: opt[1] == 'mode', device.get_options()))[8]


def usage():
    print(f"Usage: {sys.argv[0]} [mode] [resolution]")
    print("    supported modes: ", ", ".join(supported_modes))
    print("    supported resolutions: ", ", ".join(
        map(str, supported_resolutions)))
    sys.exit(1)


def main():
    if len(sys.argv) != 3:
        usage()

    mode = sys.argv[1]
    resolution = int(sys.argv[2])

    if mode not in supported_modes or resolution not in supported_resolutions:
        usage()

    print("All scanner options:")
    for opt in device.get_options():
        print(opt)

    device.mode = mode
    device.resolution = resolution

    device.start()
    image = device.snap()

    filename = f"Skan {datetime.datetime.now()}.png"
    image.save(filename)

    # Eye of Gnome, domyślna przeglądarka obrazów w Gnomie
    os.execv("/usr/bin/eog", ["/usr/bin/eog", filename])


if __name__ == "__main__":
    main()
