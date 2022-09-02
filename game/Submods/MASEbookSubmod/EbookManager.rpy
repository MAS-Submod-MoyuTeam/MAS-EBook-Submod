#https://blog.csdn.net/qiqiyingse/article/details/83659396
init -10 python in eb_books:
    import store.eb_globals as eb_globals
    import store.eb_utils as eb_utils
    from store.eb_exception import *
    import os, json, re
    # py2
    import io
    def load_ebooks():
        """
        加载所有的电子书
        return:
            一个由Ebook类组成的list
        """
        list = []
        dirs = os.listdir(eb_globals.ebook_path)
        for book in dirs:
            list.append(Ebook(eb_globals.ebook_path + "/" + book))
        return list
    
    class Ebook(object):
        # 章节名匹配格式
        _chapter_pattern = re.compile(r"\S*[第]\S*[章, 节]")
        """
        一个电子书类，表示一本电子书
        IN：
            path 电子书根目录
        """
        def __init__(self, path, name = '一本新书'):
            super(Ebook, self).__init__()
            self.path = path
            if not os.path.exists(self.path + "/original_text.txt"):
                raise EB_BookPathNotExist(self.path)
            eb_utils.mkdir(self.path + "/chapters")
            self.config = {
                # 名称
                'name':'',
                # 当前阅读到的章节
                'curr_chapter':0,
                # 当前章节名称
                'curr_chapter_name':'',
                # 当前阅读到的章节的页数
                'curr_c_page':0,
                # 总章节数
                'total_chapters':0,
                # 当前阅读到的章节总页数
                'total_c_page':0,
                # 各章节信息list(名称，页数)
                'chapter_data':[],
                # 是否进行过分章
                'chapter_splited':False
            }
            if not self.config['chapter_splited']:
                self.split_txt()
            self.rename(name)

        def load_config(self):
            with open(self.page+"/config.json", 'r') as config:
                json.load(config, self.config)

        def get_config(self, a):
            return self.config[a]
        
        def rename(self, str1):
            self.config['name'] = str1

        def create_config(self):
            """
            创建/保存本地数据
            """
            with open(self.path+"/config.json", 'w') as config:
                json.dump(self.config, config)
        
        def chapter_data_append(self, name):
            self.config['chapter_data'].append(name)

        def split_txt(self):
            """
            初始化图书，进行分章节切割
            """
            _ch = 0
            self.chapter_data_append(("序", 0))
            ori = io.open(self.path + "/original_text.txt", 'r', encoding='utf-8')
            out = io.open(self.path + "/chapters/{}.txt".format(_ch), 'w', encoding='utf-8')
            out_cache = []
            for line in ori:
                eb_utils.log_debug(line)
                if line.strip() == '':
                    continue
                a = re.search(self._chapter_pattern, line)
                eb_utils.log_debug(a)
                if a is not None:
                    eb_utils.log_debug("分割新章节：{} - {}".format(_ch, line))
                    self.chapter_data_append((line, 0))
                    _ch = _ch + 1
                    out.writelines(out_cache)
                    out.flush()
                    out.close()
                    out = io.open(self.path + "/chapters/{}.txt".format(_ch), 'w', encoding='utf-8')
                    out_cache = []
                else:
                    out_cache.append(line)
            out.writelines(out_cache)
            out.flush()
            out.close()
            eb_utils.log_debug("分割完成：{}".format(self.config['name']))
            out_cache = []
            ori.close()
            self.config['chapter_splited'] = True

        def split_page(self, chapter,pnum=0):
            """
            根据页数输出要显示的内容，每次显示24行
            """
            if pnum < 0:
                raise EB_PageNotLegal()
            ebook = io.open(self.path + "/chapters/{}.txt".format(chapter), 'r', encoding='utf-8')
            reads = []
            startline = 24*pnum if pnum==0 else 24*pnum+1
            endline = 24*(pnum+1)
            for text in ebook.readlines()[startline:endline]:
                reads.append(text)
            return reads