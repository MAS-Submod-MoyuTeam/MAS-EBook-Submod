init -900 python in eb_utils:
    import shutil, os
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
            os.mkdir(path)
        except IOError:
            pass
    def move_file(src, dst):
        try:
            shutil.move(src, dst)
        except Exception as e:
            log_error(e)
            raise e