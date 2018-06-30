'''
@author   : zhang
@time     : 2018-6-24 16:29
@file     :pagenation.py  
@software :PyCharm
'''


#页码专用模块
class Page:

    def __init__(self,current_page, data_count, per_page_count=10, page_num=7):
        #current_page    当前页面页码
        #data_count      后台数据总条数
        #per_page_count  每页显示数据条数
        #page_num        一次显示页码数量
        self.current_page = current_page
        self.data_count = data_count
        self.per_page_count = per_page_count
        self.page_num = page_num

    #每页显示的数据起始位置
    def start(self):
        return ((self.current_page-1)*self.per_page_count)

    # 每页显示的数据终止位置
    def end(self):
        return (self.current_page*self.per_page_count)

    # 返回html数据，显示页码模块
    @property
    def all_count(self):
        v,y = divmod(self.data_count,self.per_page_count)
        if y:
            v = v+1
        return v

    def page_str(self,base_url):
        page_list = []
        if self.all_count < self.page_num:
            start_page = 1
            end_page = self.all_count + 1
        else:
            if self.current_page <= (self.page_num + 1) / 2:
                start_page = 1
                end_page = self.page_num + 1
            else:
                start_page = self.current_page - (self.page_num - 1) / 2
                end_page = self.current_page + (self.page_num + 1) / 2
                if (self.all_count - self.current_page) < (self.page_num + 1) / 2:
                    start_page = self.all_count - self.page_num
                    end_page = self.all_count + 1
        #上一页标签
        prev = '<a class="page" href="?p=%s">上一页</a>' % (self.current_page - 1)
        if self.current_page == 1:
            prev = '<a class="page" href="javascript:void(0)">上一页</a>'
        page_list.append(prev)

        #页码标签
        for i in range(int(start_page), int(end_page)):
            if i == self.current_page:
                page = '<a class="page active" href="?p=%s">%s</a>' % (i, i)
            else:
                page = '<a class="page" href="?p=%s">%s</a>' % (i, i)
            page_list.append(page)

        #下一页标签
        next = '<a class="page" href="?p=%s">下一页</a>' % (self.current_page + 1)
        if self.current_page == self.all_count:
            next = '<a class="page" href="javascript:void(0)">下一页</a>'
        page_list.append(next)

        #跳转框标签
        index = '''
            <input type='text' id='i1'><input type='button' value='跳转' onclick='jumpTo(this,"%s?p=");'>
            <script>
                function jumpTo(ths,base) {
                    var p = ths.previousSibling.value;
                    console.log(p,base);
                    location.href = base+p;

                }
            </script>'''%base_url
        page_list.append(index)
        page_str = ''.join(page_list)
        return page_str
