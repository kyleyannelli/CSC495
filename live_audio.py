from pedalboard import Pedalboard, Chorus, Compressor, Delay, Gain, Reverb, Phaser
from pedalboard.io import AudioStream

import sounddevice as sd


def start():
    list_input_devices()

    selected_input_device = input("\nPlease select an input device (by number): ")

    list_output_devices()

    selected_output_device = input("\nPlease select an output device (by number): ")


def start_certain(input_device_number, output_device_number):
    print("start")



def list_output_devices():
    # list output devices
    print()
    for device in get_output_devices:
        print(device)


def list_input_devices():
    # list input devices
    print()
    for device in get_input_devices:
        print(device)


def get_output_devices():
    output_devices_array = []
    i = 0
    for device in query_devices_refresh():
        if device["max_output_channels"] > 0:
            output_devices_array.append("[" + str(i) + "] " + str(device["name"]))
            i += 1
    return output_devices_array


def get_input_devices():
    input_devices_array = []
    i = 0
    for device in query_devices_refresh():
        if device["max_input_channels"] > 0:
            input_devices_array.append("[" + str(i) + "] " + str(device["name"]))
            i += 1
    return input_devices_array


# taken from https://github.com/spatialaudio/python-sounddevice/issues/47#issuecomment-258461697
def query_devices_refresh(device=None):
        sd._terminate()
        sd._initialize()
        return sd.query_devices(device)
