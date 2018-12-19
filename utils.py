import os
from device import Device


class Utils:

    list = 'adb devices | tail -n +2'

    # One line get version command for all connected devices
    ver = 'adb devices | tail -n +2 | cut -sf -1 | xargs -I X adb -s X shell getprop ro.build.version.release '

    def get_devices(self):

        answer = os.popen(self.list).read()
        list_split = str(answer).splitlines()

        # Make devices list adresses and status.
        dev_list = []
        for i in range(0, len(list_split)):
            dev_list.append(list_split[i].split("\t"))

        # Initial devices objects.
        dev_init_list = [Device(dev_list[dev][0], dev_list[dev][1]) for dev in range(0, len(dev_list)-1)]
        return dev_init_list
