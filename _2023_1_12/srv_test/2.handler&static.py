from tornado import ioloop, web
from tornado.web import StaticFileHandler
# from tornado.options import define, options, parse_command_line, parse_config_file
# parse_config_file('server.conf')
import os

# 获取当前文件绝对路径
def print_path():
    print(os.path.abspath(__file__))                        # 打印文件绝对路径
    print(os.path.dirname(os.path.abspath(__file__)))       # 打印文件目录的绝对路径

# 拼接静态路径
def path_merge():
    static_url = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    return static_url

print_path()
print("当前文件绝对路径: " + path_merge())

class DefaultHandler(web.RequestHandler):
    def initialize(self):
        print("init handler")
    
    def on_finish(self):
        print("handler has finished")

    async def get(self):
        # get_query_argument接收url显式传参，一般用于get
        name = self.get_query_argument("username")
        pwd = self.get_query_arguments("pwd")       # 返回一个列表
        self.write(f"user {name}, pwd {pwd} access success")        # 打印user shiki, pwd ['123', '234', '345'] access success

    async def post(self):
        self.write("post request has been sent")
        # 接收body中的参数，一般用于post
        # name = self.get_body_argument("username")
        # dept = self.get_body_arguments("dept")
        # print(name)
        # print(dept)

        # self.request.body用于获取原生raw数据
        print(self.request.body.decode('utf-8'))
        self.finish({"msg":"access finish"})        # 访问成功传回响应体，并于该语句结束

# 注意：self.get_argument既能当做get_query_argument，也能当做get_body_argument使用
        
settings={
    'static_path':'./static/',
    'statuc_url_prefix':'/image/'
}

if __name__ == '__main__':
    app = web.Application([('/', DefaultHandler),
                            # 法三：通过静态文件方式访问
                            ('/image/(.*)', StaticFileHandler, {'path': path_merge()})
                           ] 
                            # 法一：通过传静态路由的方式访问静态资源（图片，视频，css等）
                            # static_path='./static/',
                            # statuc_url_prefix='/image/'
                            #
                            # 法二：通过配置访问：**settings是Python的字典解包操作符，将字典settings中的所有键值对作为参数传递给web.Application
                            # **settings,
                            #
                            
    )       
    app.listen(8080)
    print("server listening 8080...")
    ioloop.IOLoop.current().start()