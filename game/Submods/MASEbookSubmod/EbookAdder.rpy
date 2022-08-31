init -900 python in eb_function:
    import store.eb_globals as eb_globals
    import store.eb_utils as eb_utils
    import os
    def check_txt():
        files = os.listdir(eb_globals.check_path)
        for f in files:
            if eb_utils.find_str(f, '.txt'):
                eb_globals.new_txt.append(f)
    def move_txt():
        for i in eb_globals.new_txt:
            _file = eb_globals.check_path + "/" + i
            _filedir = eb_globals.ebook_path + "/{}".format(eb_utils.get_file_md5(_file))
            eb_utils.mkdir(_filedir)
            eb_utils.move_file(_file, _filedir)
