from tornado import web
from tornado.web import RedirectHandler
from tornado import ioloop
from tornado.options import define, options, parse_command_line, parse_config_file

# 从命令行读取参数port，参数名为port，默认端口为8000，值类型为int
define('port', default=8000, help='port to listen on', type=int)
define("debug", default=False, help="enable debug mode", type=bool)

# 解析配置文件
parse_config_file('server.conf')    # 上面两个声明也不能少，否则参数无法解析并传递

# 命令行配置信息需要解析参数
parse_command_line()

# requestHandler
# 1. initialize：初始化，一般不设置异步，一般用于日志，属性初始化等
# 2. prepare：请求前先调用，再post
# 3. on_finish：post结束后调用，用于资源清理

class DefaultHandler(web.RequestHandler):
    # 带上async表示建立异步连接
    async def get(self):
        self.write("default request")

class IndexHandler(web.RequestHandler):
    async def get(self):
        self.write("this is a get request")

class UserHandler(web.RequestHandler):
    async def get(self, id):
        self.write(f"user login num: {id}")

class UserHandler2(web.RequestHandler):
    async def get(self, name):
        self.write(f"user login name: {name}")

class DirectHandler(web.RequestHandler):
    async def get(self):
        self.redirect(self.reverse_url('index'))        # index这个name关联到了localhost:8000/index/这个url
        # 等价写法:传回的是名为index的url地址：/index/（使用如上写法维护性更好）
        # self.redirect('/index/')        
        # 补充：url重定向301为永久跳转，302为临时跳转

class UserShow(web.RequestHandler):
    def initialize(self, name, pwd):
        self.name = name
        self.pwd = pwd
        print(f"name is {self.name}, pwd is {self.pwd}")

    async def get(self):
        self.write(f"name is {self.name}, pwd is {self.pwd}")

# 可以通过参数包将信息传入到事件处理中
args = {
    "name":"shiki",
    "pwd":12345
}

# 命令行运行程序需要在当前程序路径前加上python以请求解释
if __name__ == '__main__':
    # 列表里的元祖为路由url地址，接收事件请求，为同步IO
    app = web.Application([('/', DefaultHandler), 
                           web.URLSpec('/index/?', IndexHandler, name='index'),     # 正则匹配以自动补全url路径
                           ('/user/(\d+)/?', UserHandler),          # \d返回字符串包含数字的匹配项（数字 0-9），+为一次或多次出现
                           ('/user/(\w+)/?', UserHandler2),         # \w返回一个匹配项，其中字符串包含任何单词字符（从 a 到 Z 的字符，从 0 到 9 的数字和下划线 _ 字符）
                           web.URLSpec('/redirect/?', DirectHandler),    # web.URLSpec用于路由的配置，即将URL与特定的处理函数或类关联起来
                           web.URLSpec('/info/?', UserShow, args, name="info"),       # 参数传入
                           web.URLSpec('/redirect2/?', RedirectHandler, {"url":"/"})    # 模块也提供跳转功能到指定url
                           ],            
                           debug=options.debug) 
    print(options.port)       
    app.listen(options.port)        # port和debug参数由命令行/配置文件传入
    ioloop.IOLoop.current().start()