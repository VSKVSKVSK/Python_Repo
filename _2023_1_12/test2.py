import test1  as general  # 导入模块并重命名
import platform         # 导入系统模块
import datetime         # 时间模块
import re               # 正则模块
import json             # json模块
import tornado
import requests
import random
# from test1 import MyNumbers # 部分导入，不允许在使用该函数时加上模块前缀

# dir列出模块中的所有函数和变量�?
print(platform.system())
print(dir(platform))
print(dir(general))

general.myfunction("shiki", 18)      # 使用导入的模块函�?

# 日期函数
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.timestamp())
print(x.weekday)

x = datetime.date(2023, 12, 15)
print(x)

# 将json转dict
jstr = '{"name":"shiki", "age":18, "sex":"male"}'       # 必须外单引，内双�?
res = json.loads(jstr)
print(type(res))
print(res)

# 任意python对象转json
js1 = json.dumps(res)
print(type(js1))
print(js1)

li = ["hello", 123, 3.0]        # complex无法序列化，除dict将转换为json串object�?
js2 = json.dumps(li)            # 其他python对象将对应转换为javascript等效项（如list，tuple转换为array�?
print(type(js2))
print(js2)

x = {
  "name": "Bill",
  "age": 63,
  "married": True,
  "divorced": False,
  "children": ("Jennifer","Rory","Phoebe"),
  "pets": None,
  "cars": [
    {"model": "Porsche", "mpg": 38.2},
    {"model": "BMW M5", "mpg": 26.9}
  ]
}

print(json.dumps(x, indent=4))  # 加上缩进格式更易阅读

# camel模块
header = "my emc corp"
trans = general.convert_camel(header)
print(trans)

# except示例
x = 1
y = 5
z = 10
try:
  if x < z: 
    raise Exception("wuhu!")
except:
  print("i was here")
finally:
  print("wait what")


# input命令行输�?
x = "input your name: "
print(x)
name = input()
print("your name is: " + name)

# 文件处理
file = open("info.txt", "r", encoding = "utf-8")    # 默认使用gbk解码，对utf-8文本读取将报�?
str = file.read()
print(file.readline())
print(file.read())    # 也可以直接全部读�?
for i in file:    # 遍历读取每行
  print(i)
file.close()

# 文件写入
file = open("info.txt", "w", encoding = "utf-8")
str = "this is a test sentence"
file.write(str)
file.close()

# random
x = random.random()
x = ["hihihi", 123, 3.3, 0.88]
x = random.choice(range(100))
x = random.choice(x)
print(x)

# 反转字符�?
str = "this is a test sentence"
print(str[::-1])

# 去重
mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)

list = [1,2,3,4,3,2,1,2,3,4,5,6,7]
list2 = list(dict.fromkeys(list))
print(list2)

# requests模块
# 设置请求头，告知服务器我们想要获取中文内�?
headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
}
response = requests.get("https://baidu.com", headers = headers)
print(response.text)
