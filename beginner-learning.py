#
#coding:utf-8  这里的coding:utf-8是为了让python解释器按照utf-8编码来读取源代码文件，避免中文乱码问题

num = 1 #整数
string = '1' #字符串
# print(num + string) #不同的类型不能直接相加，会报错

#如果你不知道变量的类型，可以使用type()函数来查看变量的类型
print(type(num))   #输出：<class 'int'>
print(type(string)) #输出：<class 'str'>

#转化数据类型
num = 1
string = '1'
num2 = int(string) #将字符串转换为整数
print(num + num2) #输出：2

#那么如果你想把整数转换为字符串呢？可以使用str()函数
num = 1
string = str(num) #将整数转换为字符串
print(string) #输出：1

#上面可以看到字符串可以和整数进行相加，但是如果你想把字符串重复多次呢？可以使用乘法运算符*来实现
words= "hello words" * 3
print(words)   #这里的'hello words'会被重复三次，输出结果为：hello words hello words hello words

#下面这个是复杂案例
word = 'a loooooong word' #字符串
num = 12 #整数
string = 'bang!' #字符串
total = string * (len(word) - num) # 这里string * 4 得到 'bang!bang!bang!bang!'
print(total) #'bang!bang!bang!bang!'

#下面我进行举一反三
# 1. 重复后拼接
a = 'Go'
b = 'al'
print(a + b * 3)   # 注意优先级：乘法高于加法
# 结果: Goa lalal? 不，是 'Go' + ('al'*3) = 'Goalalal'

# 2. 重复包含空格
sep = '-'
line = sep * 20
print(line)        # 输出: --------------------

# 3. 动态生成重复内容
emoji = '😊'
count = int(input('How many smiles? ')) #这里很重要，input()函数返回的是字符串类型，所以需要用int()函数将其转换为整数类型。
print(emoji * count) #这个很有趣，用户输入多少，就会输出多少个笑脸。

# 4. 字符串居中显示 用重复模拟文本对齐
word = 'center'
width = 20
# 左右填充 '=' 使 word 居中（近似）
left_pad = (width - len(word)) // 2
right_pad = width - len(word) - left_pad
result = '=' * left_pad + word + '=' * right_pad
print(result)
# 输出: =======center=======

#字符串重复的陷阱与注意事项：
# 1. 当重复次数为0时，结果是空字符串
# 小心：重复的是整个字符串，不是字符
s = 'ab'
print(s * 3)    # 'ababab'

# 重复 0 次或负数会怎样？
print('hi' * 0)  # 空字符串 ''
print('hi' * -1) # 空字符串 ''

# 重复一个空字符串
print('' * 100)  # 空字符串 

#上面都是字符串最基本用法，很简单的多看代码理解。

#字符串的分片与索引
#字符串的索引是从0开始的，负数索引表示从右往左数，-1表示最后一个字符，-2表示倒数第二个字符，以此类推。
#下面就以我的英文名字为例，来演示字符串的索引和分片。
name = "My name is bitter"
print(name[0])  # 输出: M
print(name[1])  # 输出: y
print(name[11:14]) # from 11th to 14th, 14th one is excluded
print(name[11:15]) # from 11th to 15th, 15th one is excluded
print(name[-1]) # 输出: r
print(name[-2]) # 输出: e
print(name[3:7]) # 输出: name
print(name[5:]) # 输出: me is bitter
print(name[:5]) # 这里省略了0，从0到5 输出： my na

#下面做个文字小游戏
word = 'friends'
find_the_evil_in_your_friends = word[0]+word[2:4]+word[-3:-1]
print(find_the_evil_in_your_friends) 

'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
'http://ww1.site.cn/85cc87jw1ex23yhwws5j20jg0szmzk.png'
'http://ww2.site.cn/185cc87jw1ex23ynr1naj20jg0t60wv.jpg'
'http://ww3.site.cn/185cc87jw1ex23yyvq29j20jg0t6gp4.gif'
# 用python编写爬虫，可以从图片中提取出这些网址，然后使用统一的方式进行png,jpg,gif格式的图片进行命名，通过字符串的索引和分片来实现图片的批量下载和命名。链接结尾倒数10个字符是图片的格式，通过索引和分片可以提取出来，然后进行命名。
url = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
file_name = url[-10:] #提取出图片的格式
print(file_name) #输出：ci0kuwex.jpg


#很多时候手机号码在网站注册信息中会被隐藏，显示为4的形式，这时候我们就可以使用字符串的索引和分片来提取出手机号码的前3位和后4位，然后进行拼接，得到完整的手机号码。
phone_number = '138****1234'
phone_number = phone_number[:3] + '****' + phone_number[-4:]
print(phone_number)
#还有只显示后四位的情况，这时候我们就可以使用字符串的索引和分片来提取出手机号码的前3位和后4位，然后进行拼接，得到完整的手机号码。
phone_number = '13866660006'  
phone_number = phone_number[:3] + '****' + phone_number[-4:]
print(phone_number)

phone_number = '1386-666-0006'
hiding_number = phone_number.replace(phone_number[:9],'*' * 9)
print(hiding_number) # *********0006
#这里使用replace()函数将前9位替换为9个*，实现隐藏手机号码的效果。也就是将前9位替换为9个*，'*'*9就是*乘以9，得到9个*.

#模拟手机通讯录中的电话号码联想功能
search = '168'
num_a = '1386-168-0006'
num_b = '1681-222-0006'
print(search + ' is at ' + str(num_a.find(search)) + ' to ' + str(num_a.find(search) + len(search)) +  ' of  num_a')
print(search + ' is at ' + str(num_b.find(search)) + ' to ' + str(num_b.find(search) + len(search)) +  ' of  num_b')
# 输出为168 is at 5 to 8 of num_a
# 输出为168 is at 0 to 3 of num_b

#下面是高级用法，查找所有匹配位置 — 使用 re.finditer() 可以找到字符串中所有匹配的位置：
import re
positions = [(m.start(), m.end()) for m in re.finditer(search, num_b)]
print(positions)  # 输出: [(0, 3)]

def highlight_match(full, search_str):
    idx = full.find(search_str)
    if idx >= 0:
        return full[:idx] + '[' + full[idx:idx+len(search_str)] + ']' + full[idx+len(search_str):]
    return full

print(highlight_match(num_a, search))  # 输出: 1386-[168]-0006
print(highlight_match(num_b, search))  # 输出: [168]-222-0006


# ____a word she can get what she ____ for.
# A.With
# B.came 这样的题目让我们印象深刻，当字符串很多空需要填充时，我们可以使用.format()进行批处理。
print('{} a word she can get what she {} for.'.format('With','came'))
print('{preposition} a word she can get what she {verb} for'.format(preposition = 'With',verb = 'came'))
print('{0} a word she can get what she {1} for.'.format('With','came'))
# 这种用法很广泛，例如下面的例子：可以填充网址中空缺的城市数据:
city = input("write down the name of city:")
url = "http://apistore.baidu.com/microservice/weather?citypinyin={}".format(city)
print(url)
# 这是利用百度天气API接口，输入城市拼音，就可以获取该城市的天气信息。

#学习一下py常用的函数
#print()函数：用于输出信息到控制台。一个是放入对象就可以将结果打印的函数。
#input()函数：用于从控制台获取用户输入。一个是可以让用户输入数据的函数。
#type()函数：用于获取对象的类型。一个是可以查看变量类型的函数。
#len()函数：用于获取对象的长度。一个是可以查看字符串长度的函数。
#int()函数：用于将对象转换为整数类型。一个是可以将字符串转换。
#str()函数：用于将对象转换为字符串类型。一个是可以将整数转换为字符串。
#通过规律其实不难发现，python中有很多内置函数，都是以函数名()的形式调用的。就是把你要处理的对象放入函数的括号中，就可以得到你想要的结果。还有很多函数就不举例了。
#以python内置函数为例，python内置函数有很多，常用的有：abs()、all()、any()、bin()、bool()、bytearray()、bytes()、callable()、chr()、classmethod()、compile()、complex()、delattr()、dict()、dir()、divmod()、enumerate()、eval()、exec()、filter()、float()、format()、frozenset()、getattr()、globals()、hasattr()、hash()、help()、hex()、id()、input()等等。 
#以python3.50版本为例，一共存在68个内置函数，它们都叫做内置函数，都是python自带的函数，使用起来非常方便。不要搞混了，python内置函数和python模块中的函数是不同的，模块中的函数需要导入模块才能使用，而内置函数不需要导入模块就可以直接使用。 
#但是还有一些不常用，比如涉及字符编码的函数，涉及数学运算的函数，涉及文件操作的函数，涉及网络操作的函数ascii()、bin()、bytes()、bytearray()、callable()、chr()、classmethod()、compile()、complex()、delattr()、dict()、dir()、divmod()、enumerate()、eval()、exec()、filter()、float()、format()、frozenset()、getattr()、globals()、hasattr()、hash()、help()、hex()等等。
#大家可以去python官方文档中查看python内置函数的详细介绍和使用方法。

#开始创建函数
#def关键字用于定义函数，define函数名后面跟着括号，括号中可以包含参数列表，参数之间用逗号分隔。函数体以冒号开始，并缩进编写代码。函数可以通过return语句返回值，也可以不返回值。
#argument是函数的参数，parameter是函数的形参，argument是函数的实参。函数的参数可以有默认值，也可以没有默认值。函数的参数可以是位置参数，也可以是关键字参数。函数的参数可以是可变参数，也可以是不可变参数。函数的参数可以是必选参数，也可以是可选参数。函数的参数可以是命名关键字参数，也可以是位置关键字参数。函数的参数可以是可变关键字参数，也可以是不可变关键字参数。
#return语句用于从函数中返回值，return语句可以返回任意类型的值，也可以不返回值。函数的返回值可以是单个值，也可以是多个值，也可以是None。函数的返回值可以通过变量接收，也可以直接使用。函数的返回值可以通过print()函数输出，也可以通过其他函数使用。
#Example:
def greet(name):
    print(f"Hello, {name}!") 
    print('小明')

# Define a function called 'function' which has two arguments : arg1 and arg2. The function should return the sum of arg1 and arg2. returns the result——'Something'
def function():
    return'Something'
    def function():
        return'Something'
#下面是摄氏度转化公式，定义函数为fahrenheit_Converter()    
def fahrenheit_converter(C):
  fahrenheit = C * 9/5 + 32
  return str(fahrenheit) + '˚F' #计算的结果是int类型，不能与字符串"F"相合并所以需要使用str()函数进行转换
lyric_length = len('I Cry Out for Magic!') 
print(lyric_length) #输出：21 

C2F = fahrenheit_converter(35)
print(C2F) 

#我们把刚刚的函数进行以下修改
def fahrenheit_converter(C):
  fahrenheit = C * 9/5 + 32
  print(str(fahrenheit) + '˚F')
C2F = fahrenheit_converter(35)
print(C2F) #95.0˚F None

#练习题 
#1初级难度:设计一个重量转换器函数，输入以g为单位的重量，输出以kg为单位的重量。1kg=1000g。
def weight_converter(g):
    kg = g / 1000
    return str(kg) + 'kg'

# Example usage:
weight_in_g = 5000
weight_in_kg = weight_converter(weight_in_g)
print(weight_in_kg)  # Output: 5.0kg

#2中级难度:设计一个求直角三角形斜边长的函数(两条直角边的长度作为参数，求最长边的长度)，如果直角边长分别为3和4。那么返回的结果应该想这样The right triangle third side's length is 5.0。

import math
def hypotenuse_length(a, b):
    return math.hypot(a, b)

# Example usage:
side_a = 3
side_b = 4
hypotenuse = hypotenuse_length(side_a, side_b)
print(f"The right triangle third side's length is {hypotenuse}.")  # Output: The right triangle third side's length is 5.0.
#修改建议
def weight_converter(grams):
    """将克转换为千克（返回浮点数）"""
    return grams / 1000

# 使用
weight_in_kg = weight_converter(5000)
print(f"{weight_in_kg}kg")  # 5.0kg

#传递参数与参数类型
fahrenheit_converter(35)
fahrenheit_converter(15)
fahrenheit_converter(0)
fahrenheit_converter(-3)
#位置参数(position argument) 关键词参数(keyword argument)
#构造梯形面积函数
def trapezoid_area(base_up, base_down, height):
    """计算梯形的面积"""
    return 1/2 * (base_up + base_down) * height
trapezoid_area(1,2,3) #位置参数
trapezoid_area(base_up=1, base_down=2, height=3) #位置参数
#第二种传入方式
trapezoid_area(base_up=1, base_down=2, height=3)#关键词参数
trapezoid_area(height=3, base_down=2, base_up=1)#关键词参数
# trapezoid_area(height=3, base_down=2, base_up=1) # RIGHT!
# trapezoid_area(height=3, base_down=2, 1) # wrong!
# trapezoid_area(base_up=1, base_down=2, 3) # RIGHT!
trapezoid_area(1, 2, height=3) # RIGHT!
#理解函数的参数传递方式
base_up = 1
base_down = 2
height = 3
trapezoid_area(height, base_down, base_up)
#定义一个函数，模拟手电筒的开关功能，它需要两个电池参数battery1, battery2意为电池，这时候你去商店买电池的时候，你需要买两节电池才能使用手电筒。这个函数的功能是当你传入两个电池参数时，返回一个字符串'Light!'，表示手电筒亮了。
def flashlight (battery1, battery2):
  return 'Light!'
nanfu1 = 600
nanfu2 = 600
flashlight(nanfu1, nanfu2)

def trapezoid_area(base_up, base_down, height=3): # 梯形面积公式 面积 = (上底 + 下底) × 高 ÷ 2,1/2 * (base_up + base_down) * height，等价于 (base_up + base_down) * height / 2，数学上正确,1/2=0.5
  return 1/2 * (base_up + base_down) * height  
trapezoid_area(1, 2) #计算结果：1/2 × (1+2) × 3 = 4.5
trapezoid_area(1, 2, height=15) #计算结果：1/2 × (1+2) × 15 = 22.5

# 推荐这样写 默认参数 height=3，调用时可以不传该参数
# 关键字参数	height=15，明确指定传给哪个参数
# 缩进 函数体必须缩进，这是Python 的语法规则
# 函数返回值return返回结果，但需要接收或打印才能看到
def trapezoid_area(base_up, base_down, height=3):
    """计算梯形的面积"""
    return (base_up + base_down) * height / 2
#使用沉默高
result = trapezoid_area(1, 2)  # 使用默认高度3
print(result)  # 输出: 4.5
#指定高度为15
result2= trapezoid_area(1, 2, height=15)
print(result2)  # 输出: 22.5


#下面是一个爬虫案例，使用requests库进行网络请求，获取图片并保存到本地。
# 1. 先定义 url（你要下载的图片地址）
import requests
import urllib3

urllib3.disable_warnings()
url = 'https://www.baidu.com/img/flexible/logo/pc/result.png'  # ← 请换成真实的图片网址
# header = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
# }

# ★ 在这里可以添加代理配置
# proxies = {
#   'http': 'http://127.0.0.1:7890',
#    'https': None,          # HTTPS 不走代理，直接连接
# }
# import requests # 这是 Python 第三方库 requests 中用于发送 HTTP GET 请求 的方法。HTTP GET	从服务器获取资源（网页、图片、API数据等），就像在浏览器中输入网址访问页面。requests 库	Python 最流行的 HTTP 请求库，需要先安装 pip install requests
# response = requests.get(url, headers=header,verify=False,proxies={'http': None, 'https': None}) # 要访问的网址，必须是字符串。例如：'https://www.baidu.com'、'https://api.github.com/users/octocat'
# requests.get(url, headers=header,verify=False, proxies={'http': None, 'https': None}) # headers（可选，但很常用）是一个字典，用于设置 HTTP 请求头，让服务器识别请求的来源、类型等信息。1模拟浏览器访问（绕开反爬虫）2设置认证信息3指定内容类型

# 模拟 Chrome 浏览器的请求头
# ★ header 必须在这里定义（在 requests.get 之前）
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
} # 为什么要加 headers？ 很多网站会检查请求的来源，如果发现是 Python 请求（没有浏览器标识），可能会拒绝访问或返回错误数据。
# 返回值：Response 对象；requests.get() 返回一个 Response 对象，包含服务器的响应内容。常用属性和方法：

response = requests.get(url, headers=header,verify=False,proxies={'http': None, 'https': None})

# 状态码（200 表示成功，404 页面不存在，500 服务器错误）
print(response.status_code)     # 200
# 响应内容（二进制形式，适用于图片、文件等字节形式）
print(response.content)         # b'...' # bytes 类型
# 响应内容（文本形式，自动解码）
print(response.text)            # '<!DOCTYPE html>...' # HTML 源码或 JSON 字符串
# 将响应内容解析为 JSON（API 接口常用）
# data = response.json()          # 自动解析为 Python 字典/列表

# 判断请求是否成功
if response.ok:                 # status_code < 400 时为 True
    print("请求成功")
else:
    print("请求失败")

# 不走代理直接连接
import requests, urllib3
urllib3.disable_warnings()
r = requests.get(
    'https://www.baidu.com',
    headers={'User-Agent': 'Mozilla/5.0'},
    verify=False,
    proxies={'http': None, 'https': None}  # 完全禁用代理
)
print(r.status_code)

# 完整的示例：下载一张图片
import requests

# 1. 准备请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# 2. 发送 GET 请求获取图片
url = 'https://www.example.com/image.jpg'
response = requests.get(url, headers=header,verify=False, proxies={'http': None, 'https': None}
)

# 3. 检查是否成功
if response.status_code == 200:
    # 4. content 返回二进制数据，写入文件保存
    with open('image.jpg', 'wb') as f:
        f.write(response.content)
    print("图片下载成功")
else:
    print(f"下载失败，状态码: {response.status_code}")

from PIL import Image # 注意这里需要安装库 pip install pillow
img = Image.open('input.jpg')
img.save(img_new, img_format, quality=100) # 这是 PIL/Pillow 库中用于保存图像文件的方法。img 是 Pillow 的 Image 对象。给图片加水印的时候默认是100。
# Pillow	Python 图像处理库，安装：pip install pillow
# Image 对象	用 Image.open() 打开图片后得到的对象
# save()	将图像对象保存到文件
#img_new	保存的文件路径和名称，例如 'output.jpg'、'result.png'。也可以是一个文件对象（如 BytesIO）。
#img_format	保存的图片格式，例如 'JPEG'、'PNG'、'GIF' 如果不指定，Pillow 会根据文件扩展名自动判断：
# .jpg / .jpeg → JPEG
# .png → PNG
# .gif → GIF
# 显式指定格式（即使文件扩展名不同）
img.save('output.png', 'JPEG')   # 保存为 JPEG 格式但扩展名为 .png（不推荐）

# 不指定格式，根据扩展名自动判断
img.save('output.jpg')            # 自动用 JPEG 格式保存
quality=100  # JPEG 格式专用）图片质量，取值范围：1（最差）~ 95（最好）。默认值：75。quality=100 表示最高质量，但文件最大。仅对 JPEG 格式有效，PNG 等无损格式忽略此参数。
# 高质量（文件较大）
img.save('high_quality.jpg', quality=95)
# 中等质量（文件较小）
img.save('medium_quality.jpg', quality=50)
# 最低质量（文件最小）
img.save('low_quality.jpg', quality=10)
#完整的示例：下载并保存图片
import requests
from PIL import Image
from io import BytesIO

# 1. 下载图片
url = 'https://www.example.com/image.jpg'
header = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=header)

# 2. 用 Pillow 打开图像（从内存中读取）
img = Image.open(BytesIO(response.content))

# 3. 对图片做一些处理（可选）
# img = img.resize((800, 600))   # 调整大小
# img = img.rotate(90)           # 旋转

# 4. 保存图片（最高质量）
img.save('saved_image.jpg', 'JPEG', quality=100)
print("图片保存成功")

# requests.get() + img.save() 的完整工作流程;把两个方法串联起来，就是从网络下载图片并保存到本地的完整流程：
import requests
from PIL import Image
from io import BytesIO

# 准备请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}

# 发送 GET 请求获取图片数据
response = requests.get('https://example.com/photo.jpg', headers=headers)

# 检查状态码
if response.status_code == 200:
    # 将二进制数据转换为 Image 对象
    img = Image.open(BytesIO(response.content))
    
    # 保存图片
    img.save('downloaded_photo.jpg', 'JPEG', quality=95)
    
    # 也可以保存为其他格式
    img.save('downloaded_photo.png', 'PNG')
    
    print("下载并保存成功！")
else:
    print(f"请求失败，状态码: {response.status_code}")

from PIL import Image
# 先确认你有一张图片可以打开
# 比如你之前下载了 baidu_logo.png
img = Image.open('baidu_logo.png')
# 定义正确的变量
img_new = 'my_saved_image.jpg'   # 要保存的文件名
img_format = 'JPEG'              # 图片格式
img.save(img_new, img_format, quality=100)
print(f"✅ 图片已保存为 {img_new}")

#下面我们设置自己的函数，来实现敏感词过滤器，先认识一个函数open。我们先在本地创建一个文件夹，命名为test.txt的文件。
# open()函数是Python内置函数，用于打开文件并返回文件对象。它的基本语法如下：
open('/Users/username/Desktop/test.txt', 'r', encoding='utf-8')   # 注意Windows系统，路径应该是 D:\Desktop\... 格式。
open('C://Users//username//Desktop//test.txt', 'r', encoding='utf-8')
#认识一个新函数write()，照抄我之前的代码replace()函数，来学着使用write的方法：
file = open('/Users/username/Desktop/test.txt', 'w', encoding='utf-8') #打开文件
file.write('Hello, World!') #写入数据
file.close() #关闭文件

# 掌握了open()和write()函数后，我们就可以实现设计函数了，传入参数name和msg就可以控制在桌面写入的文件名称和内容的函数text_create，如果桌面没有这个文件我们可以创建一个之后在写入内容，如果桌面有这个文件我们可以直接写入内容。
def text_create(name,msg):
    desktop_path = '/Users/username/Desktop/'  # 替换为你的桌面路径
    full_path = desktop_path + name + '.txt'  # 文件完整路径
    file = open(full_path, 'w', encoding='utf-8')
    file.write(msg)
    file.close()
    print("done")
    print(f"文件 {full_path} 已创建并写入内容。")
text_create('hello','hello world') # 调用函数，创建hello.txt文件，并写入内容hello world
# 敏感词过滤器的实现思路是：先定义一个敏感词列表，然后读取文本内容，检查文本中是否包含敏感词，如果包含就进行替换或删除。下面是一个简单的实现示例：
def text_filter(word,censored_word = 'lame',changed_word = 'Awesome'): # word: 必填参数，代表要处理的原始文本。censored_word='lame': 默认参数，指定要被替换的敏感词，默认值为 'lame'。changed_word='Awesome': 默认参数，指定替换后的词，默认值为 'Awesome'。函数的作用：将 word 中的所有 censored_word 替换为 changed_word，并返回新字符串。
  return word.replace(censored_word,changed_word) # 调用字符串的 replace() 方法，返回替换后的结果。
text_filter('python is lame！') #调用函数

def text_filter(word, censored_word='lame', changed_word='Awesome'):
    """将 word 中的敏感词替换为指定的词"""
    return word.replace(censored_word, changed_word)
# 调用并打印结果
result = text_filter('python is lame！')
print(result)  # 输出: python is Awesome！

def censored_text_create(name, msg):
  clean_msg = text_filter(msg)
  text_create(name,clean_msg)
censored_text_create('Try','lame!lame!lame!') # 调用函数

# 完整可运行示例（包含所有定义）
def text_filter(word, censored_word='lame', changed_word='Awesome'):
    """将 word 中的敏感词替换为指定词"""
    return word.replace(censored_word, changed_word)

def text_create(name, msg):
    """打印格式化的消息"""
    print(f"[{name}] says: {msg}")

def censored_text_create(name, msg):
    """过滤敏感词并创建消息"""
    clean_msg = text_filter(msg)
    text_create(name, clean_msg)

# 运行
censored_text_create('Try', 'lame!lame!lame!') # 输出: [Try] says: Awesome!Awesome!Awesome!

#运用函数的运作方式，假设a=10,b=20,运算符如下:
# + a+b 输出等于30 加
# - a-b 输出等于-10 减
# / b/a 输出等于2 除- x除以y
# % b%a 输出等于0 取模-返回除法的余数
# ** a**b 为10的20次方，输出结果100000000000000000000  冥-返回x的y次冥
#// 9//2 输出等于4，9.0//2.0输出等于4.0  取整除-返回商的整数部分

# 循环与判断 true&false
1>2    # False  1 不大于 2
1<2<3    # True  链式比较，等价于 1<2 and 2<3
42 != '42'  # True 整数和字符串类型不同，不相等
'Name' == 'name'  # False  字符串区分大小写
'M' in 'Magic'  # True  字符串包含子串
number = 12
number is 12  # True  小整数被缓存，是同一个对象
# 验证比较运算符
print(42 != '42')       # True
print('Name' == 'name') # False
print('M' in 'Magic')   # True

number = 12
number is 12    # True

# 多条件比较
middle=5
1<middle<10
# 变量的比较
two=1+1
three=1+3
two<three
# 字符串的比较
'Eddie Van Helen' == 'eddie van helen' #
#两个函数产生的结果进行比较
abs(-10)>len('length of this word')

# 不同类型的对象不能使用“<，>，<：，>："进行比较，却可以使用'：：'和'！：'，例如字符串和数字
42 > 'the answer'  #无法比较
42 == 'the answer' #False
42 != 'the answer' #True
# 要注意的是，浮点和整数虽是不同类型，但是不影响到比较运算：
5.0 == 5 #True
3.0 > 1 #True
# 布尔类型
True > False # 1>0 
True + False > False + False # 1+0>0+0

# 成员运算符与身份运算符(Membership&ldentifyOperators)
# 成员运算符和身份运算符的关键词是in与iso把in放在两个对象中间的含义
# 是，测试前者是否存在于in后面的集合中。说到集合，我们先在这里介绍一个简单易
# 懂的集合类型一列表(List)
# 字符串、浮点、整数、布尔类型、变量甚至是另一个列表都可以储存在列表中，
# 列表是非常实用的数据结构，在后面会花更多篇幅来讲解列表的用法，这里先简单了解一下
# 创建一个列表
album = [] #空的列表
album = ['Black Star','David Bowie',25,True] #非空列表
# 想要添加一个内容,需要使用append方法向列表添加新的元素
album.append('new song')
# 下面是列表的索引,前面我们有学习字符串的索引,相信下面的知识也不难理解,
print(album[0],album[-1]) #打印第一个元素,和最后一个元素.
# 接下来使用in来测试字符串甘ackStar'是否在列表album中。如果存在则会显示True，不存在就会显示FaIse了：
'Black Star' in album
# 接下来讲解is和is not,接下来再来讲解is和isnot，它们是表示身份鉴别(ldentify Operator)的布尔运算符，in和not in则是表示归属关系的布尔运算符号(Membership Operator)
# 在Python中任何一个对象都要满足身份(ldentity)丶类型(Type)丶值(value)这三个占缺一不可。is操作符号就是来进行身份的对比的。试试输入这段代码：
the_Eddie = 'Eddie'
name = 'Eddie'
the_Eddie == name
the_Eddie is name  # is对比最后返回了true

# 其实在Python中任何对象都可判断其布尔值，除了0、None和所有空的序列与集合（列表，字典，集合）布尔值为FaIse之外，其它的都为True，使用函数bool()进行判别：
bool(0) #False
bool([]) #False
bool('') #False
bool(False) #False
bool(None) #False
a_thing = None # 当你想设定一个变量，但又没想好它应该等于什么值时，你就可以这样写

# 布尔运算符(BooleanOperators)
# and、or用于布尔值的之间的运算，具体规则如下：
# not X 如果是True，则返回FaIse,否则返回True
# X and Y   and表示“并且"，如果x和Y都是True,则返回True；如果x和Y有一个是FaIse,则返回FaIse
# X or Y  or表示“或者"，如果x或y有其中一个是True，则返回True；如果x和Y都是FaIse,则返回FaIse

# and和or经常用于处理复合条件，类似于1<n<3，也就是两个条件同时满足。
1 < 3 and 2 < 5 #True
1 < 3 and 2 > 5 #False
1 < 3 or 2 > 5 #True
1 > 3 or 2 > 5 #False

# 条件控制 条件控制其实就是if...else的使用。先来看下条件控制的基本结构
# 用一句话概括if...else结构的作用：如果···条件是成立的，就做····；反之，就做...
# 所谓条件(condition)指的是成立的条件，即正返回值为True的布尔表达式,知道了这点后使用起来应该不难。
# 我们结合函数的概念来创建这样一个函数，逐行分析它的原理：

def account_login():  # 第1行：定义函数，并不需要参数；
    password = input('Password:') # 第2行：使用input获得用户输入的字符串并储存在变量password中；
    if password == 'bitter':  # 第3、4行：设置条件，如果用户输入的字符串和预设的密码12345相等时，
        print('Login success!') # 就执行打印文本'Loginsuccess!'
    else: # 第5、6行：反之，一切不等于预设密码的输入结果，全部会执行打印错误提示，
        print('Wrong password contact bitter or invalid input!') # 并且再次调用函数，让用户再次输入密码；
        account_login() # 第7行：运行函数。
account_login() # 第8行：调用函数

# 如果if后面的布尔表达式过长或者难于理解，可以采取给变量赋值的办法来储存布尔表达式返回的布尔值True或FaIseo因此上面的代码可以写成:
def account_login():
    password = input('Password:')
    password_correct = password == 'bitter' #here!
    if password_correct:
        print('Login success!')
    else:
        print('Wrong password contact bitter or invalid input!')
        account_login()
account_login()

# 多条件的判断,只需要在if和else之间加入elif,用法和if一样,所有的代码都是从上往下运行,
# 首先需要看条件是否成立,如果成立那么就运行下面的代码,如果不成立就先运行下面的代码是否成立,如果都不成立就会运行else对应的语句.

#下面使用elif语句做一个重置密码的功能:  下面的代码很简单,之前学了前面的内容,一眼就能理解下面的代码
password_list = ['*#*#','bitter']
def account_login():
    password = input('Password:')
    password_correct = password == password_list[-1]
    password_reset = password == password_list[0]
    if password_correct:
        print('Login success!')
    elif password_reset:
        new_password = input('Enter a new password:')
        password_list.append(new_password)
        print('Your password has changed successfully!')
        account_login()
    else:
        print('Wrong password contact bitter or invalid input!')
        account_login()
account_login()

#循环(Loop) for循环  下面做个例子
for every_letter in 'Hello world':
    print(every_letter)
# 这两行代码展示的是：使用for循环打印出'Hello world'这段字符串中的每一个
# 字符。for循环作为编程语言中最强力的特性之一，能够帮助我们做很多重复性的事
# 情，比如批量命名、批量操作等等。
# 把for循环所做的事情概括成一句话就是：于···其中的每一个元素，做···事情
# 下面怎么使用for循环做到打印做这种效果呢
# 1 + 1 = 2
# 2 + 1 = 3
# ...
# ...
# 10 + 1 = 11

# 需要用到一个内置函数一range。只需要在range函数后面的括号中填上数字，就可以得一个具有连续整数的序列，输入代码：
for num in range(1,11): # 这里不包含11,范围是1-10
    print(str(num) + ' + 1 =',num + 1)
# 下面可以这样写,
num = 1
print(str(num) + ' + 1 =',num + 1)
num = 2
print(str(num) + ' + 1 =',num + 1)
...
...
num = 10
print(str(num) + ' + 1 =',num + 1)

#歌曲程序循环播放案例
songslist = ['Holy Diver', 'Thunderstruck', 'Rebel Rebel']
for song in songslist:
    if song == 'Holy Diver':
        print(song,' - Dio')
    elif song == 'Thunderstruck':
        print(song,' - AC/DC')
    elif song == 'Rebel Rebel':
        print(song,' - David Bowie')

# 嵌套循环 被称之为嵌套循环(NestedLoop)，其实这种循环并不复杂而且还非常实用。都学过乘法囗诀表，又称“九九表"，接下来就用嵌套循环实现它
for i in range(1,10):
    for j in range(1,10):
        print('{} X {} = {}'.format(i,j,i*j))
# 正如代码所示，这就是嵌套循环。通过观察，我们不难发现这个嵌套循环的原理：最外层的循环依次将数值1、9存储到变量i中，变量i每取一次值，内层循环就要依次将1、9中存储在变量j中，最后展示当前的i、j与i*j的结果。

# while循环 Python中有两种循环，第一种for循环，躬二种则是while循环。它们的相同点在于都能循环做一件重复的事情，不同点在于for循环把列表里的每一个元素都处理一遍完成的时候停止，while则是在条件不成立的时候停止，因此while的作用概括成一句话就是：只要···条件成立，就一直做···
# 下面的小例子
while 1 < 3:
    print('bitter is dizzy or 1 is smaller than 3') #在这里先行提醒一下，一定要记得及时停止运行代码！
# 注：在终端或者命令行中按CtrI+C停止运行，在PyCharm中则点击红色的x停止
# 因为在while后面的表达式是永远成立的，所以print会一直进行下去直至你的
# cpu过热。条件永远为True的循环，我们称之为死循环(lnfiniteLoop)

#在循环过程中制造某种可以使循环停下来的条件,例如:
count = 0
while True:
    print('bitter is brave or Repeat this line !')
    count = count + 1
    if count == 5:
        break
    
# 在上面代码中，有两个重要的地方，首先是给count的变量赋值
# 为0，我们希望在循环次数为5的时候停下来。接下来的是break，
# 这个count=count+1！其实我已经不止一次强调过编程代码和数学公式在某些地方很相似，但又不完全相同，首先在Python中“=”并非是我们熟知的“等于'的含义，所以我们不必按照数学公式一样把重复的变量划掉。其次count被赋值为0，count=count+1意味着count被重新赋值！等价于count=0+1，随着每次循环往复，count都会在上一次的基础上重新赋值，都会增加+1，直至count等于5的时候break,跳出最近的一层循环，从而停下来。利用循环增加变量还是一个挺常见的技巧，随着循环不仅可以增加，还可以随着循环减少(n=n一1），甚至是成倍数增加（n=n*3)0

# 除此之外，让while循环停下来的另外一种方法是：改变使循环成立的条件。为了解释这个例子，我们在前面登录函数的基础上来实现，给登录函数增加一个新功能：输入密码错误超过3次就禁止再次输入密码。

password_list = ['******','bitter']
def account_login():
    tries = 3
    while tries > 0:
        password = input('Password:')
        password_correct = password == password_list[-1]
        password_reset = password == password_list[0]

        if password_correct:
            print('Login success!')

        elif password_reset:
            new_password = input('Enter a new password :')
            password_list.append(new_password)
            print('Password has changed successfully!')
            account_login()
        else:
            print('Wrong password contact bitter or invalid input!')
            tries = tries - 1
            print( tries, 'times left')
    else:
        print('Your account has been suspended or contact admin bitter')

account_login()

# 第4、5行：增加了while循环，如果tries>0这个条件成立，那么便可输入密码，从而执行辨别密码是否正确的逻辑判断；第20、21行：当密码输入错误时，可尝试的次数tries减少1；第23、24行：while循环的条件不成立时，就意味着尝试次数用光，通告用户账户被锁。在这里while可以理解成是if循环版，可以使用while-else结构，而在while代码块中又存在着第二层的逻辑判断，这其实构成了嵌套逻辑（Nested Condition)

# 下面布置小练习、

# 1.设计这样一个函数，在桌面的文件夹上创建10个文本，以数字给它们命名。
# 答案
import os
import platform

def create_numbered_text_files_on_desktop(count: int = 10) -> None:
    """
    在桌面文件夹上创建指定数量的数字命名文本文件，例如 1.txt, 2.txt, ...

    参数:
        count: 要创建的文件数量，默认为 10
    """
    # 确定桌面路径
    system = platform.system()
    if system == "Windows":
        desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
    elif system == "Darwin":  # macOS
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    else:  # Linux 及其他类 Unix
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")

    # 确保桌面路径存在
    if not os.path.isdir(desktop):
        raise FileNotFoundError(f"桌面目录不存在: {desktop}")

    created_files = []

    for i in range(1, count + 1):
        filename = f"{i}.txt"
        filepath = os.path.join(desktop, filename)

        # 避免覆盖已有文件，可以选择追加内容或跳过
        # 此处选择跳过（不覆盖）
        if os.path.exists(filepath):
            print(f"⚠️ 跳过已存在的文件: {filepath}")
            continue

        try:
            # 创建一个空文本文件（也可以写入一些内容）
            with open(filepath, "w", encoding="utf-8") as f:
                # 写入简单的欢迎内容（可选）
                f.write(f"这是文件 {filename}\n创建时间: 自动生成\n")
            created_files.append(filepath)
            print(f"✅ 已创建: {filepath}")
        except Exception as e:
            print(f"❌ 创建文件失败 {filepath}: {e}")

    print(f"\n完成！共创建 {len(created_files)} 个文件。")


# 如果需要立即运行，取消下面的注释：
# if __name__ == "__main__":
#     create_numbered_text_files_on_desktop()


# 2.设计一个复利计算函数invest(),它包含三个参数：amount（资金）rate（利率），time（投资时间）。输入每个参数后调用函数，应该返回每一年的资金总额。（假设利率为5％）

# 答案
# 设计一个复利计算函数 invest()
# 复利公式：A = P(1 + r)^t
# A = 最终金额，P = 本金，r = 年利率，t = 投资年数

def invest(amount, rate, time):
    """
    计算复利投资，返回每一年的资金总额
    
    参数:
        amount: 初始投资金额（本金）
        rate:   年利率（百分比形式，如 5 表示 5%）
        time:   投资年限
    
    返回:
        每一年末的资金总额列表
    """
    print(f"初始投资金额: ¥{amount}")
    print(f"年利率: {rate}%")
    print(f"投资年限: {time}年")
    print("=" * 40)
    
    yearly_results = []
    current_amount = amount
    
    for year in range(1, time + 1):
        # 计算该年的复利增长
        # rate/100 将百分比转换为小数，例如 5% → 0.05
        current_amount = current_amount * (1 + rate / 100)
        print(f"第{year:2d}年末: ¥{current_amount:,.2f}")
        yearly_results.append(round(current_amount, 2))
    
    print("=" * 40)
    total_return = current_amount - amount
    print(f"总投资回报: ¥{total_return:,.2f}")
    print(f"总回报率: {total_return / amount * 100:.2f}%")
    
    return yearly_results


# 调用函数：假设利率为 5%
print("\n▶ 示例 1：投资 1000 元，利率 5%，投资 5 年\n")
result1 = invest(amount=1000, rate=5, time=5)

print("\n" + "★" * 50)

print("\n▶ 示例 2：投资 10000 元，利率 5%，投资 10 年\n")
result2 = invest(amount=10000, rate=5, time=10)

print("\n" + "★" * 50)

# 你也可以让用户自己输入参数
print("\n▶ 示例 3：用户自定义输入\n")
user_amount = float(input("请输入投资金额: "))
user_rate = float(input("请输入年利率（%）："))
user_time = int(input("请输入投资年限: "))
user_result = invest(amount=user_amount, rate=user_rate, time=user_time)

# 3、打印1、100内的偶数
# 答案

# 1.num % 2 == 0	取模运算符 %，余数为 0 说明能被 2 整除 → 偶数， 打印 1 到 100 内的全部偶数
print("1 到 100 内的偶数：")

for num in range(1, 101):
    if num % 2 == 0:        # 能被 2 整除 → 偶数
        print(num, end=' ')  # end=' ' 让输出在一行，用空格分隔


# 2.range(2, 101, 2) 的含义：从 2 开始，到 100 结束，步长为 2;range(2, 101, 2)	第三个参数"步长"，跳过奇数直接生成偶数
# 这样直接就能得到所有偶数，不需要 if 判断
print("1 到 100 内的偶数（range 步长法）：")

for num in range(2, 101, 2):
    print(num, end=' ')

# 3.封装成函数 end=' '	print() 默认换行，设置 end=' ' 改为空格分隔
def print_even_numbers(start=1, end=100):
    """
    打印指定范围内的所有偶数
    
    参数:
        start: 起始值（包含），默认为 1
        end:   结束值（包含），默认为 100
    """
    print(f"打印 {start} ~ {end} 内的偶数：")
    
    # 收集偶数到列表中 
    evens = []
    for num in range(start, end + 1):
        if num % 2 == 0:
            evens.append(num)
    
    # 每行显示 10 个，更整齐
    for i in range(0, len(evens), 10):
        print(' '.join(f"{x:3d}" for x in evens[i:i+10]))
    
    print(f"\n共找到 {len(evens)} 个偶数")


# 调用函数
print_even_numbers(1, 100)

print("\n" + "=" * 40)

# 也可以灵活指定范围
print_even_numbers(50, 80)


# 4.列表推导式 [x for x in iterable if condition]一行代码搞定，适合展示 Python 的简洁特性
evens = [num for num in range(1, 101) if num % 2 == 0]
print(evens)

# 已经基本学完了逻辑判断和循环的用法，首先创建一个列表，放入数字，再使用sum()函数对列表中的所有整数求和，打印
a_list = [1,2,3]
print(sum(a_list)) # 结果是6

# 接着认识一个内置库random，可以生成随机数
import random
point1 = random.randrange(1,7)
point2 = random.randrange(1,7)
point3 = random.randrange(1,7)
print(point1,point2,point3) # 每次打印的数都会不一样

# 设计一个小游戏猜大小;我们摇出来的结果是3个骰子分别的点数，需要把点数转换为“大"或者“小"，其中“大"的点数范围是11<=总值<：18，“小"的点数范围是3<=总值<=10。最后，让用户猜大小，如果猜对了就告诉用户赢的结果，如果猜错了就告诉用户输的结果。
# 下面参考
# <<<<< GAME STARTS! >>>>>
# Big or Small:Big
# <<<<< ROLE THE DICE!>>>>>
# The points are [2, 6, 3] You Lose!

import random
def roll_dice(numbers=3, points=None):  # 第2行：创建函数，设定两个默认参数作为可选，numbers——骰子数量，points三个筛子的点数的列表；
    print('<<<<< ROLL THE DICE! >>>>>') # 第3行：告知用户开始摇骰子；
    if points is None:   # 第4、5行：如果参数中并未指定points,那么为points创建空的列表；
        points = []
    while numbers > 0:
        point = random.randrange(1,7)  #第6、9行：摇三次骰子，每摇一次numbers就减1，直至小于等于0时，循环停止
        points.append(point)
        numbers = numbers - 1
    return points  # 第10行：返回结果的列表。
# 接着，再用一个函数来将点数转化成大小，并使用if语句来定义什么是“大"，什么是“小"
def roll_result(total):  # 第1行：创建函数，其中必要的参数是骰子的总点数；
    isBig = 11 <= total <=18  # 第2、3行：设定“大"与“小"的判断标准；
    isSmall = 3 <= total <=10  
    if isBig: 
        return 'Big'
    elif isSmall:
        return 'Small'   # 第4、7行：在不同的条件下返回不同的结果。


# 最后，创建一个开始游戏的函数，让用户输入猜大小，并且定义什么是猜对，什么是猜错，并输出对应的输赢结果。
def start_game():  # 第1行·创建函数，并不需要什么特殊参数；
    print('<<<<< GAME STARTS! >>>>>')  # 第2行告知用户游戏开始；
    choices = ['Big','Small'] # 第3行规定什么是正确的输入；
    your_choice = input('Big or Small :')  # 第4行将用户输入的字符串储存在your-choice中；
    if your_choice in choices: # 第5、13、15行：如果符合输入规范则往下进行，不符合则告知用户并重新开始；
        points = roll_dice()  # 第6行：调用roll-dice函数，将返回的列表命名为points；
        total = sum(points)   # 第7行：点数求和；
        youWin = your_choice == roll_result(total)   # 第8行：设定胜利的条件一你所选的结果和计算机生成的结果是一致的；
        if youWin:
            print('The points are',points,'You win !')  # 第9、12行：成立则告知胜利，反之，告知失败；
        else:
            print('The points are',points,'You lose !')
    else:
        print('Invalid Words')
        start_game()
start_game() # 第16行：调用函数，使程序运行。

# 练习题
# 1、在最后一个项目的基础上增加这样的功能，下注金额和赔率。具体规则如下：
# 2、初始金额为1000元；
# 3、金额为0时游戏结束；
# 4、默认赔率为1倍，也就是说押对了能得相应金额，押错了会输掉相应金额。

# 答案如下
import random

def start_game():
    # 1. 初始化游戏数据
    balance = 1000  # 初始金额
    default_odds = 1.0  # 默认赔率
    
    print("====== 欢迎来到数字博弈游戏 ======")
    print(f"初始本金：{balance} 元 | 默认赔率：{default_odds} 倍")
    print("规则：每轮你可以自由下注，猜对硬币正反面（1为正面，0为反面）。")
    print("==================================")
    
    # 2. 游戏主循环（金额为0时结束）
    while balance > 0:
        print(f"\n当前余额: {balance} 元")
        
        # --- 下注阶段 ---
        try:
            bet = int(input("请输入下注金额 (输入0退出游戏): "))
        except ValueError:
            print("请输入有效的整数金额！")
            continue
            
        # 退出条件
        if bet == 0:
            print("你选择退出了游戏。")
            break
            
        # 边界检查：下注不能超过持有金额，也不能是负数
        if bet > balance:
            print("余额不足，无法下注这么多！")
            continue
        if bet < 0:
            print("下注金额不能为负数！")
            continue
            
        # --- 游戏互动阶段 ---
        guess = input("请预测硬币正反面 (输入 1 表示正面，0 表示反面): ")
        if guess not in ['0', '1']:
            print("输入错误，请输入 0 或 1！")
            continue
            
        # 模拟掷硬币 (0或1)
        result = str(random.randint(0, 1))
        print(f"开奖结果是: {'正面' if result == '1' else '反面'}")
        
        # --- 结算阶段 ---
        if guess == result:
            # 猜对了：赢得 下注金额 * 赔率
            win_amount = int(bet * default_odds)
            balance += win_amount
            print(f"🎉 恭喜你猜对了！赢得了 {win_amount} 元。")
        else:
            # 猜错了：输掉相应金额
            balance -= bet
            print(f"❌ 遗憾猜错了！输掉了 {bet} 元。")
            
    # 3. 游戏结束
    print("\n==================================")
    print("游戏结束！")
    if balance <= 0:
        print("你的金额已归零，胜败乃兵家常事，请重新来过！")
    else:
        print(f"最终带着 {balance} 元离开了游戏。")
    print("==================================")

# 运行游戏
if __name__ == "__main__":
    start_game()


#  2、我们在注册应用的时候，常常使用手机号作为账户名，在短信验证之前一般都会
# 检验号码的真实性，如果是不存在的号码就不会发送验证码。检验规则如下：
# 长度不少于11位，
# 是移动、联通、电信号段中的一个电话号码；
# 因为是输入号码界面，输入除号码外其他字符的可能性可以勿田攵
# 移动号段，联通号段，电信号段如下：
# CN_mobile = \
[134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
CN_union = [130,131,132,155,156,185,186,145,176,1709]
CN_telecom = [133,153,180,181,189,177,1700] 

# 程序效果如下
# Enter Your number：123
# Invalid length, your number should be in 11 digits
# Enter Your number：12345
# Invalid length, your number should be in 11 digits
# Enter Your number：11121123123
# No such a operator
# Enter Your number：13162221340
# Operator：China Union
# We are sending verification code via text to your phone：13162221340 

# 答案如下
def start_phone_verification():
    # 题目给出的运营商号段数据
    CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
    CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
    CN_telecom = [133, 153, 180, 181, 189, 177, 1700]

    while True:
        # 1. 获取输入并剔除两端空格
        phone_num = input("Enter Your number：").strip()
        
        if not phone_num:
            break

        # 2. 长度检查：不等于 11 位则报错并继续循环
        if len(phone_num) != 11:
            print("Invalid length, your number should be in 11 digits")
            continue

        # 3. 提取前缀（转为数字用于和列表中的 int 进行比对）
        try:
            prefix_3 = int(phone_num[:3])
            prefix_4 = int(phone_num[:4])
        except ValueError:
            print("No such a operator")
            continue

        # 4. 运营商匹配
        operator = None
        if prefix_4 in CN_mobile or prefix_3 in CN_mobile:
            operator = "ChinaMobile"
        elif prefix_4 in CN_union or prefix_3 in CN_union:
            operator = "ChinaUnion"
        elif prefix_4 in CN_telecom or prefix_3 in CN_telecom:
            operator = "ChinaTelecom"

        # 5. 严格按照你的最新示例输出
        if operator:
            print(f"Operator：{operator}")
            print(f"We are sending verification code via text to your phone：{phone_num}")
            break  # 验证成功，发送后跳出循环结束程序
        else:
            print("No such a operator")

if __name__ == "__main__":
    start_phone_verification()

# python有四种数据结构，分别是列表，字典，元组，合集
list = [val1,val2,val3,val4]
dict = {key1:val1,key2:val2}
tuple = (val1,val2,val3,val4)
set = {val1,val2,val3,val4}
# 从最容易识别的特征上来说，列表中的元素使用方括号扩起来，字典和集合是花括号，而元组则是圆括号。其中字典中的元素是均带有苤'的key与value的对应关系组。

# 首先我们从列表开始，深入地讲解每一种数据结构。列表具有的最显著的特征
# 1·列表中的每一个元素都是可变的；
# 2·列表中的元素是有序的，也就是说每一个元素都有一个位置；
# 3·列表可以容纳Python中的任何对象。
# 列表中的每一个元素都对应着一个位置，输入位置查询该位置所对应的值，试着输入：
Weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
print(Weekday[0])

# 第三个特征是列表可以装入Python中所有的对象，看下面的例子就知道了：
all_in_list = [
1,  # 整数
1.0, # 整数
'a word', # 字符串
print(1), # 函数
True  # 布尔值
[1,2], # 列表中套列表
(1,2),  # 元组 
{'key':'value'} # 字典
]

# 列表的增删改查 对于数据的操作，最常见的是增删改查这四类。从列表的插入方法开始，输入：
fruit = ['pineapple','pear']
fruit.insert(1,'grape')
print(fruit)
# 或者这样
fruit[0:0] = ['Orange']
print(fruit)

# 删除列表中元素的方法是使用remove()：
fruit = ['pinapple','pear','grape']
fruit.remove('grape')
print(fruit)
# 或者这样直接替换
fruit[0] = 'Grapefruit'

# 删除还可以使用del关键字来声明
del fruit[0:2]
print(fruit)

# 列表的索引与字符串的分片十分相似，同样是分正反两种索引方式，只要输入对应的位置就会返回给你在这个位置上的值：接下来用元素周期表来试验一下：
periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[-10:])
print(periodic_table[:9])

# 你会发现列表的索引和字符串是一样的，但是如果要是反过来，想要查看某个具体的值所在的位置，就需要用别的方法了，否则就会报错：
print(periodic_table['H'])
# Traceback(most recent call Last)：
# tinianianuntittt乙
# print(periodic—tabte['H're.I])
# TypeError：list indices must be integers or stices，not str
# 报错是因为列表只接受用位置进行索引，但如果数据量很大的话，肯定会记不住什么元素在什么位置，那么有没有一种数据类型可以用人类的方式来进行索引呢？其实这就是字典，继续学习。