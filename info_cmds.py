class Info:

    android_ver = 'getprop ro.build.version.release'
    kernel_ver = 'uname -a'
    sdk_ver = 'getprop ro.build.version.sdk'
    cpu_use = 'dumpsys cpuinfo'
    mem_use = 'dumpsys meminfo'
    net_status = 'netcfg'
    ip_cfg = 'ifconfig'

