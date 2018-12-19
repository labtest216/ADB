from time import sleep
from utils import Utils

# SYNC PC WITHE DEVICES
# Before run the main.py script, sync pc with the devices:
# Enable developer mode on all devices by pushing on settings->about phone->model number 8 times.
# (depend on your phone)
# Go to developer options->enable USB debugging


# Initial devices objects.
dev_init_list = Utils().get_devices()

# Do actions for all connected devices.
for dev in dev_init_list:
    # get device version cpu use and memory use.
    dev.send(dev.info.android_ver)
    dev.send(dev.info.kernel_ver)
    dev.send(dev.info.sdk_ver)
    #dev.send((dev.info.net_status))
    #dev.send((dev.info.ip_cfg))
    #dev.get_sn()
    #dev.send((dev.info.cpu_use))
    #dev.send((dev.info.mem_use))

    # take screen shot.
    dev.send(dev.ui.print_screen('/sdcard/screenshot'))

    # list screen shot file.
    dev.send(dev.fs.ls + " /sdcard/screenshot.png")

    # copy screen shot file to pc.
    dev.pull('/sdcard/screenshot.png', './')

    # delete screen shot file from device.
    dev.send(dev.fs.rm('/sdcard/screenshot.png'))

    # list screen shot file to see it deleted.
    dev.send(dev.fs.ls + " /sdcard/screenshot.png")

    # press device home button.
    dev.send(dev.ui.press_home_button)

    # record video.
    #dev.send(dev.ui.record_video('/sdcard/movie'))

    # reduce brightness.
    dev.send(dev.ui.key_event(dev.ui.ke_Brightness_down))


    sleep(3)







