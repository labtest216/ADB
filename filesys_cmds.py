class Fsys:

    # List dir.
    ls = 'ls'
    ls_l = 'ls-l'

    # Current dir.
    pwd = 'pwd'

    # Change file permission.
    @staticmethod
    def chmod(permission, file_path):
        return 'chmod '+permission+" "+file_path

    # Copy file.
    @staticmethod
    def cp(dev_src_file, dev_des_file):
        return 'cp ' + dev_src_file + " " + dev_des_file

    # Copy dir.
    @staticmethod
    def cp_r(dev_src_dir, dev_des_dir):
        return 'cp -r ' + dev_src_dir + " " + dev_des_dir

    # Change file name.
    @staticmethod
    def mv(file_path, file_path_new_name):
        return 'mv ' + file_path + " " + file_path_new_name

    # Delete file.
    @staticmethod
    def rm(file_path):
        return 'rm ' + " " + file_path

    # Delete dir.
    @staticmethod
    def rm_r(dir_path):
        return 'rm -r ' + dir_path

