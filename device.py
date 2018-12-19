import os
from time import sleep
from filesys_cmds import Fsys
from info_cmds import Info
from ui_cmds import Ui
import utils

class Device:

    # Shell command type classes.
    fs = Fsys()
    info = Info()
    ui = Ui()

    # Init device with address and  connected status (usb/ip:port offline/device).
    # Define preamble with -s for multiple devices.
    def __init__(self, address, status):
        self._address = address
        self._status = status
        self._shell_preamble = "adb -s "+self._address+" shell "
        self._preamble = "adb -s "+self._address+" "

    # Send shell bash command if device connected.
    # If you know any of the bash commands, you can send it direct by string.
    def send(self, cmd, preamble=None):
        if preamble is None:
            preamble = self._shell_preamble
        if self._status == 'device':
            print('Device ' + self._address + ' connected')
            full_cmd = preamble + str(cmd)
            print(full_cmd)
            answer = os.popen(full_cmd).read()
            print(answer)
            sleep(1)
            return answer
        else:
            print('Device '+self._address+' not connected')
            sleep(2)
            return -1

    # If not connected by usb.
    def connect(self, dev_ip):
        return self.send('connect '+str(dev_ip), self._preamble)

    # Copy file from pc to device.
    def push(self, pc_src, dev_des):
        return self.send('push ' + pc_src+" "+dev_des, self._preamble)

    # Copy file from device to pc.
    def pull(self, dev_src, pc_des):
        return self.send('pull ' + dev_src + " " + pc_des)

    def get_sn(self):
        return self._address

    def kill_server(self):
        return self.send('kill-server', self._preamble)

    def start_server(self):
        return self.send('start-server', self._preamble)

