init -900 python in eb_utils:
    import shutil, os, hashlib
    from store.mas_submod_utils import submod_log as submod_log
    def log_debug(str):
        submod_log.debug("[ebook] {}".format(str))
    def log_info(str):
        submod_log.info("[ebook] {}".format(str))
    def log_warn(str):
        submod_log.warning("[ebook] {}".format(str))
    def log_error(str):
        submod_log.error("[ebook] {}".format(str))

    def find_str(str1, str2):
        if str1.find(str2) != -1:
            return True
        else:
            return False 
    def mkdir(path):
        try:
            if not os.path.exists(path):
                os.makedirs(path)
        except IOError:
            raise
    def move_file(src, dst):
        try:
            shutil.move(src, dst)
        except Exception as e:
            log_error(e)
            raise e
    def get_file_md5(path):
        """
        获取文件内容的MD5值
        :param path: 文件所在路径
        :return:
        """
        with open(path, 'rb') as file:
            data = file.read()

        diff_check = hashlib.md5()
        diff_check.update(data)
        md5_code = diff_check.hexdigest()
        return md5_code