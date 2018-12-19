class Ui:

    press_home_button = 'am start -W -c android.intent.category.HOME -a android.intent.action.MAIN'
    reboot = 'reboot'
    poweroff = 'poweroff'

    ke_camera = 220
    ke_browser = 64
    ke_Brightness_down = 220
    ke_Brightness_up = 221
    ke_volume_down = 25
    volume_up = 24

    @staticmethod
    def print_screen(dev_save_path):
        return 'screencap -p '+str(dev_save_path)+'.png'

    @staticmethod
    def record_video(dev_save_path):
        return 'screenrecord '+str(dev_save_path)+'.mp4'

    @staticmethod
    def key_event(number):
        return 'input keyevent '+str(number)
