import os

program = 'sudo apt-get install android-tools-adb'

password = input("Enter your root password ro install ADB tool:")

os.system('echo %s|sudo -S %s' % (password, program))
