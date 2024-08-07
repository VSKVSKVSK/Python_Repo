import camelcase

# 定义父类
class person:
    def __init__(this, name = "老马", age = 18):
        this.name = name
        this.age = age

    def fun(this):
        print("name is " + this.name + ", the age is " + str(this.age))
        print(this.dept, this.year)

    dept = "sc"
    year = 2020

# 定义子类
class student(person):
    # 通过super获取父类方法和属性（临时对象）
    def __init__(this, name, age, id, sex, job):
        super().__init__(name, age)
        this.id = id
        this.sex = sex
        this.job = job

    def print_stu(this):
        # f-string的变量嵌入方式，可读性更高，操作更方便
        super().fun()
        print(f"id:{this.id} name:{this.name} age:{this.age} sex:{this.sex} job:{this.job} dept:{this.dept} year:{this.year}")



# test
p1 = person("alan", 48)
p1.fun()

p2 = student("velvet shiki", 20, 10001, "male", "student")
p2.fun()
p2.print_stu()

# 修改类属性
p1.name = "bill"
p1.age = 88
p1.fun()

s = "this is a test sentence"
res = s.split(" ")
for i in res: 
    print(i)

x = student("elon musk", 48, 10010, "male", "programmer")
x.print_stu()

# 迭代
mytuple = ("apple", "banana", "cherry")
# 返回一个迭代对象tuple_iterator
myit = iter(mytuple)
# 返回数据对象
# print(type(next(myit)))
print(next(myit))
print(next(myit))
print(next(myit))

s = "this is a test"
sit = iter(s)
try:
    while(True):
        print(next(sit))
except StopIteration:
    # 循环正常或异常终止，该语句必定被触发
    # while(True): print(next(sit)) 会不断调用 next(sit) 直到触发 StopIteration 异常
    # print("exception has been triggered in loop")
    pass


# 自定义迭代器
class MyNumbers:
  # __iter__为类创建迭代器返回，使类型可以使用iter构造
  def __iter__(self):
    self.a = 1
    return self

  # __next__为类返回迭代器的下一个
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      # 迭代至末尾，自动触发迭代异常以终止循环
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


def myfunction(name, age):
   print(f"my name is {name} and the age of mine is {age}")

# 驼峰命名转换
def convert_camel(input):
   camel = camelcase.CamelCase()
   ret = input.replace(" ", "")
   print(ret)
   ret = camel.hump(ret)
   return ret

header = "my emc corp"
camel = camelcase.CamelCase()
ret = camel.hump(header)
print(ret)
trans = convert_camel(header)
print(trans)