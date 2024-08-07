from tornado import web, ioloop, template

class DefaultHandler(web.RequestHandler):
    def initialize(self):
        pass

    def get(self):
        self.write("<h1>hi there!</h1>")
        # template渲染写法1
        words = "this is a template test"
        # t = template.Template("<h2>hihihi, {{arg}} </h2>")
        # self.finish(t.generate(arg = words))

        # 法2:
        self.render("index.html", arg=words)

if __name__ == '__main__':
    app = web.Application([('/', DefaultHandler)], 
                          debug=True, 
                          template_path="./templates")
    app.listen(8080)
    print("server listening 8080...")
    ioloop.IOLoop.current().start()