#https://blog.csdn.net/qiqiyingse/article/details/83659396
init -10 python in eb_books:
    import store.eb_globals as eb_globals
    import os, json
    class Ebook(object):
        """docstring for Ebook"""
        def __init__(self, path):
            super(Ebook, self).__init__()
            self.path = path
            self.config = {
                # 名称
                'name':'',
                # 当前章节
                'curr_chapter':0,
                # 当前章节名称
                'curr_chapter_name':'',
                # 当前章节的页数
                'curr_c_page':0,
                # 总章节数
                'total_chapters':0,
                # 当前章节总页数
                'total_c_page':0,
                # 各章节信息list(章节，名称，页数)
                'chapter_data':[]
            }
    
        def create_config():
            with open(path+"/config.json", 'w') as config:
                pass