init -999 python in eb_exception:
    class EB_PageNotLegal(object):
        def __init__(self):
            self.arg = arg
        def __str__(self):
            return "[Ebook] 页数参数不合法"
    class EB_BookPathNotExist(object):
        def __init__(self):
            self.arg = arg
        def __str__(self):
            return "[Ebook] 电子书目录不存在: '{}'".format(self.arg)