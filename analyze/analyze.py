
from tkinter import messagebox
import time
import numpy as np
import win32ui
import os
import json
from wordcloud import WordCloud
from collections import Counter
import jieba

from PIL import ImageTk, Image
import codecs
import jieba.posseg as pseg
import matplotlib.pyplot as plt

from pylab import mpl
import jieba.posseg as pseg

from pymongo import MongoClient
from pandas import Series,DataFrame
import pandas as pd
from collections import Counter
import pygal
import thulac
import numpy as np

from gensim.models import word2vec
import re
import json
import request
import tkinter
from tkinter import *

import matplotlib.pyplot as plt
import matplotlib
from PIL import ImageTk, Image
from pymongo import MongoClient
from pandas import Series,DataFrame
import pandas as pd
from collections import Counter
import pygal
import thulac
import numpy as np
#from gensim.models import word2vec
from gensim.models import word2vec
import re
import json
import request
import tkinter
from tkinter import *

import matplotlib.pyplot as plt
import matplotlib
from PIL import ImageTk, Image

import requests
from bs4 import BeautifulSoup
import webbrowser

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


# #增加背景图片
# back_photo = root.PhotoImage(file="back.png")
# theLabeback = root.Label(root,
#     text="我是内容,\n请你阅读",#内容
#     ustify=root.LEFT,#对齐方式
#     image=back_photo,#加入图片
#     compound = root.CENTER,#关键:设置为背景图片
#     font=("华文行楷",20),#字体和字号
#     fg = "white")#前景色
# theLabeback.pack()
#Label2=Label(root,image=photo).pack(side=RIGHT)



class Application(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        #作品选择可以更改
        self.file_path = 'data\西游记.txt'
        self.character_path = 'data\西游记人物.txt'
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['runoobdb']
        mycol = self.db['sites']
        plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签

        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号



    def createWidgets(self):
        #self.nameInput = Entry(self)
        #self.nameInput.pack()
        self.alertButton1 = Button(self, text='作品原文', command=self.open_file)
        #self.alertButton1.pack(side=tkinter.LEFT)
        self.alertButton1.pack()
        self.alertButton2 = Button(self, text='作品人物', command=self.open_character)
        # self.alertButton2.pack(side=tkinter.LEFT)
        self.alertButton2.pack()
        self.alertButton3 = Button(self, text='分析词频', command=self.draw_frequency)
        self.alertButton3.pack()
        # self.alertButton3.pack()
        self.alertButton4 = Button(self, text='绘制词云', command=self.word_cloud)
        self.alertButton4.pack()
        self.alertButton5 = Button(self, text='人物关系', command=self.name_name)
        self.alertButton5.pack()
        self.alertButton6 = Button(self, text='词条搜索', command=self.word_search)
        self.alertButton6.pack()
        self.alertButton7 = Button(self, text='诗歌最常见十大地点',command=self.draw_max_posion)
        self.alertButton7.pack()
        self.alertButton8 = Button(self, text='十大作者频次图', command=self.draw_max_author)
        self.alertButton8.pack()
        self.alertButton9 = Button(self, text='季节饼图', command=self.draw_season_times)
        self.alertButton9.pack()





    def word_search(self):
        # 测试搜索功能
        # def baidu_search():
        #     searching_word = new_name.get()
        #     print(searching_word)

        def OnButtonCheck():
            # self.result.SetLabel('')
            # try:
            num = new_name.get()  # 获取用户输入的词语

            class Baidu_baike():

                def request(self, url):
                    return self.session.get(url)

                # 必须有一个query方法，用户执行查询的时候会自动调用query方法
                def query(self, key):
                    self.description = []  # 自己添加的，用来保存文档中的subtitle作为当前需要的搜索结果
                    self.key = key
                    self.results = []
                    self.session = requests.session()
                    self.session.headers[
                        'User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (' \
                                        'KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36 '
                    if not key:
                        self.appendResult('请输入关键字', '百度一下，你就知道')
                    else:
                        url = 'https://baike.baidu.com/search/word?word=' + key
                        res = self.request(url)
                        res.encoding = 'utf-8'
                        content_encoding = res.headers['Content-Encoding']
                        soup = BeautifulSoup(res.text)
                        if content_encoding == 'deflate':
                            # headers中的Content Encoding的值为deflate，则证明query中的关键字直接匹配到百度百科的词条
                            # 直接return结果即可
                            description = soup.find_all(attrs={'name': 'description'})[0]['content']
                            # description获取了页面下的概述字符串
                            title = key
                            if soup.select('.polysemantList-wrapper li span'):
                                title = title + '(' + soup.select('.polysemantList-wrapper li span')[0].text + ')'
                            self.description.append(description)  # changed
                            self.appendResult(title, description, url)
                            multiple = soup.select('.polysemantList-wrapper')
                            if len(multiple):
                                items = soup.select('.polysemantList-wrapper li a')
                                for index in range(len(items)):
                                    url = 'https://baike.baidu.com' + items[index].attrs['href']
                                    title, subtitle = self.getDescription(url)
                                    self.appendResult(title, subtitle, url)
                        else:
                            for i in soup.select(".search-list dd"):
                                title = i.contents[1].text[:-5]
                                subtitle = i.contents[3].text
                                url = i.contents[1]['href']
                                self.appendResult(title, subtitle, url)
                            if not len(self.results):
                                self.appendResult('找不到结果', '未能找到' + key + '的相关信息，请重新输入')

                    ytm = tkinter.Tk()  # 创建Tk对象
                    ytm.title("查询结果")  # 设置窗口标题
                    # ytm.geometry("500x200")  # 设置窗口尺寸

                    width = 400
                    height = 300
                    screenwidth = ytm.winfo_screenwidth()
                    screenheight = ytm.winfo_screenheight()
                    alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
                    ytm.geometry(alignstr)

                    # canvas=Canvas(ytm,width=700,height=200,bg="#FFCCCC",text=self.description)
                    # canvas.pack(expand=YES,fill=BOTH)
                    text = Text(ytm, width=400, height=300)
                    text.pack()
                    text.insert(INSERT, self.description)  # INSERT索引表示光标当前的位置
                    # text.insert(END, '你奈人生何')
                    # mainloop()

                    # theLabel=tkinter.Label(ytm,
                    #                        bg='#FFCCCC',
                    #                        text=self.description,
                    #                        width = 600,
                    #                        height = 500,
                    #                        wraplength = 80,
                    #                        justify = 'left')
                    # theLabel.pack(expand=YES,fill=BOTH)

                    # # 测试信息
                    # print('description test: ')
                    # print(self.description)
                    # print('---------------------- ')
                    ytm.mainloop()  # 进入主循环

                    # theLabel=tkinter.Label(ytm,
                    #                        bg='#FFCCCC',
                    #                        text=self.description,
                    #                        width = 600,
                    #                        height = 500,
                    #                        wraplength = 80,
                    #                        justify = 'left')
                    # theLabel.pack(expand=YES,fill=BOTH)
                    # # 测试信息
                    # print('description test: ')
                    # print(self.description)
                    # print('---------------------- ')
                    # ytm.mainloop()  # 进入主循环

                    return self.results

                def getDescription(self, url):
                    """
                    输入百度百科的url，根据DOM元素分析标题和描述
                    :param url: 百度百科的url
                    :return: tuple(title, subtitle)
                    """
                    res = self.request(url)
                    res.encoding = 'utf-8'
                    soup = BeautifulSoup(res.text)
                    title = self.key + '(' + soup.select('.polysemantList-wrapper li span')[0].text + ')'
                    subtitle = soup.find_all(attrs={'name': 'description'})[0]['content']
                    return title, subtitle

                def openUrl(self, url):
                    webbrowser.open(url)

                def appendResult(self, title, subtitle, url=None):
                    """
                    用于向result中添加项目
                    :param title: 标题
                    :param subtitle: 副标题
                    :param url:指向的网页
                    """
                    self.results.append({
                        "Title": title,
                        "SubTitle": subtitle,
                        "IcoPath": "Images/app.ico",
                        "JsonRPCAction": {
                            "method": "openUrl",
                            "parameters": [url],
                            "dontHideAfterAction": True
                        }
                    })

            test = Baidu_baike()
            test.query(num)

        # ytm = tkinter.Toplevel(self)
        ytm = tkinter.Tk()
        # ytm.geometry('300x200')
        ytm.title('词条搜索')

        # 布局窗口大小
        width = 300
        height = 200
        screenwidth = ytm.winfo_screenwidth()
        screenheight = ytm.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        ytm.geometry(alignstr)

        # 插入图片
        # photo = PhotoImage(file='searching.gif', width=150, heigh=100)
        # Label(ytm,  # text='请选择想要分析\n的小说',#justify='left',
        #       image=photo,
        #       compound=CENTER).place(x=75, y=0)

        # 搜索信息
        new_name = tkinter.StringVar()  # 将输入的注册名赋值给变量
        new_name.set('重庆师范大学')  # 将最初显示定为
        tkinter.Label(ytm, text='词条: ').place(x=10, y=110)  # 将`User name:`放置在坐标（10,10）。
        entry_new_name = tkinter.Entry(ytm, textvariable=new_name)  # 创建一个注册名的`entry`，变量为`new_name`
        entry_new_name.place(x=130, y=110)  # `entry`放置在坐标（130,10）.

        btn_comfirm_sign_up = tkinter.Button(ytm, text='搜索', command=OnButtonCheck)
        btn_comfirm_sign_up.place(x=180, y=150)

        ytm.mainloop()  # 进入主循环


    def open_file(self):
        #name = self.nameInput.get() or 'world'
        #messagebox.showinfo('Message', 'Hello, %s' % name)
        #messagebox.showinfo('Message','Hello,world')
        dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
        dlg.SetOFNInitialDir(os.path.abspath('.'))  # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()

        self.file_path = dlg.GetPathName()  # 获取选择的文件名称
        #print(file_path)
        #print(file_path[-3:])
        # 判定最后三个字符是不是txt
        if self.file_path[-3:] == "txt":
            #print(self.file_path)
            ytm = tkinter.Tk()  # 创建Tk对象
            ytm.title("提示")  # 设置窗口标题
           # ytm.geometry("300x50")  # 设置窗口尺寸

            # 布局窗口大小
            width = 300
            height = 200
            screenwidth = ytm.winfo_screenwidth()
            screenheight = ytm.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            ytm.geometry(alignstr)

            text=Text(ytm,width=300,height=50)
            text.pack()
            text.insert(INSERT,self.file_path+"打开成功") # INSERT索引表示光标当前的位置
            #l1 = tkinter.Label(ytm, text=self.file_path+"打开成功")  # 标签
            #l1.pack()  # 指定包管理器放置组件
            ytm.mainloop()  # 进入主循环
        else:
            self.open_file()
        #f=open('filename','r')


    def open_character(self):
        #name = self.nameInput.get() or 'world'
        #messagebox.showinfo('Message', 'Hello, %s' % name)
        #messagebox.showinfo('Message','Hello,world')
        dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
        #dlg.SetOFNInitialDir('D:\Project\python\ssss')  # 设置打开文件对话框中的初始显示目录
        dlg.DoModal()

        self.character_path = dlg.GetPathName()  # 获取选择的文件名称
        #print(character_path)
        #print(character_path[-3:])
        # 判定最后三个字符是不是txt
        if self.character_path[-3:] == "txt":
            #print(self.character_path)
            ytm = tkinter.Tk()  # 创建Tk对象
            ytm.title("提示")  # 设置窗口标题

            # 布局窗口大小
            width = 300
            height = 200
            screenwidth = ytm.winfo_screenwidth()
            screenheight = ytm.winfo_screenheight()
            alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
            ytm.geometry(alignstr)

            text = Text(ytm, width=300, height=50)
            text.pack()
            text.insert(INSERT, self.character_path+"打开成功")
            # l1 = tkinter.Label(ytm, text=self.character_path+"打开成功")  # 标签
            # l1.pack()  # 指定包管理器放置组件
            ytm.mainloop()  # 进入主循环
        else:
            self.open_character()
        #f=open('filename','r')

    #def frequency(self):
        # global file_path
        #print(self.file_path)
        #print(self.character_path)


    def frequency(self):
        print(self.file_path)
        print(self.character_path)

        #winPath = ''
        #winPath = self.file_path
        #print("path of windows:" + winPath)

        #if winPath != '':
            #list = winPath.split('\\')
        #else:
            #print("it is null")
        #linuxpath = '/'.join(list)
        #print("path of linux:" + linuxpath)

        '''
        旧的人物出场频次，没有柱状图
        :return:
        '''
        file = open(self.file_path, encoding="UTF-8").read()
        # print file

        frequency = {}
        # 将人物表与小说中的人物进行对比，找出他们出现的次数
        ytm = tkinter.Tk()  # 创建Tk对象
        ytm.title("提示")  # 设置窗口标题
        ytm.geometry("300x500")  # 设置窗口尺寸
        #self.file_path1=self.file_path[-3:]
        for line in open(self.character_path, encoding="UTF-8").readlines():
            print(line.strip(), len(re.findall(line.strip(), file)))
            l1 = tkinter.Label(ytm, text=(line.strip(), len(re.findall(line.strip(), file))))  # 标签
            l1.pack()  # 指定包管理器放置组件
            # ytm.mainloop()  # 进入主循环
            # frequency.update({line.strip(): len(re.findall(unicode(line.strip()), file))})
            count = len(re.findall(line.strip(), file))
            if count < 100:  # 过滤出现次数小于100的人物
                continue
            frequency[line.strip()] = count
        # l1.pack()  # 指定包管理器放置组件
        ytm.mainloop()  # 进入主循环
        data = frequency.values()

    def draw_frequency(self):
        '''
        人物出场频次图表展示
        :return:
        '''
        name = []
        number = []
        file_name = self.file_path[:-4]
        file = open(self.file_path, encoding="UTF-8").read()


        # 将人物名name和人物出现频率number放入对应列表
        for line in open(self.character_path, encoding="UTF-8").readlines():
            if len(re.findall(line.strip(), file)) >100:
                # print(line.strip(), len(re.findall(line.strip(), file)))
                name.append(line.strip())
                number.append(len(re.findall(line.strip(), file)))

        # 画出初始的柱状图
        first_bar = plt.bar(name, number)

        # 为坐标轴上的每一个柱状图标注其高度值
        for data in first_bar:
            y = data.get_height()
            x = data.get_x()
            plt.text(x + 0.15, y, str(y), va='bottom')
        # 旋转y轴字，让文字不会重叠在一起
        plt.xticks(rotation=45)

        # plt.show()
        plt.savefig(file_name + '_freqency.png')  # 图片的存储
        # plt.save(file_name + '_freqency.png')

        # 创建子窗口显示已保存的频次图
        topFreq = tkinter.Toplevel()
        topFreq.title("人物出场频次图")
        image = Image.open(file_name + '_freqency.png')
        img = ImageTk.PhotoImage(image)
        canvas1 = tkinter.Canvas(topFreq, width=image.width, height=image.height, bg='white')
        canvas1.create_image(0, 0, image=img, anchor="nw")
        canvas1.create_image(image.width, 0, image=img, anchor="nw")
        canvas1.pack()

        # name = []
        # number = []
        del first_bar
        # Button(topFreq, text='关闭', command=topFreq.quit()).pack()
        topFreq.mainloop()





    def word_cloud(self):# json file cannot renew
        print(self.character_path)
        print(self.file_path)

        file_name = self.file_path[:-4]
        print(file_name)

        stopwords = []

        for user in open(self.character_path, encoding='UTF-8').readlines():
            jieba.add_word(user.strip())

        ssss = open(self.file_path, encoding='UTF-8').read()

        # for line in open('stopwords.txt').readlines():
        #     stopwords.append(line.strip())

        stopwords += [word.strip() for word in open('stopwords.txt', encoding='UTF-8').readlines()]

        if os.path.exists(os.path.abspath('') + '\\data\\' + file_name + '_words.json'):
            words = json.loads(open(os.path.abspath('.') + '\\' + file_name + '_words.json').read().encode('UTF-8'))
        else:
            words = []
            for item in jieba.cut(ssss, cut_all=True):
                # print(item.strip().encode('utf-8'), item.strip().encode('UTF-8') in stopwords)
                if len(item) <2:
                    continue
                if item.strip().encode('utf-8') in stopwords:
                    continue
                words.append(item)
            with open(file_name + '_words.json', 'w') as buf:
                buf.write(json.dumps(words))

        counter = Counter(words)
        # text_jieba = [x for x in jieba.cut(text) if len(x) >= 2]

        # counter = sorted(counter)

        img = Image.open('book.png')  # 打开图片
        img_array = np.array(img)  # 将图片装换为数组

        wc = WordCloud(font_path='C:\Windows\Fonts\msyh.ttc',
                        width=800, height=600,
                        mask=img_array,
                        background_color='white').generate_from_frequencies(counter)
        #plt.imshow(wc)
        #plt.axis('off')
        #plt.show()
        wc.to_file(file_name + '_wordcloud.png')

        # im = Image.open(file_name + '_wordcloud.png')
        # im.show()

        top1 = tkinter.Toplevel()
        top1.title("作品词云图")
        image = Image.open(file_name + '_wordcloud.png')
        img = ImageTk.PhotoImage(image)
        canvas1 = tkinter.Canvas(top1, width=image.width, height=image.height, bg='white')
        canvas1.create_image(0, 0, image=img, anchor="nw")
        canvas1.create_image(image.width, 0, image=img, anchor="nw")
        canvas1.pack()
        top1.mainloop()



    def name_name(self):
        names = {}
        relationships = {}
        lineNames = []

        #dlg = win32ui.CreateFileDialog(1)  # 1表示打开文件对话框
        #dlg.SetOFNInitialDir(os.path.abspath('.'))  # 设置打开文件对话框中的初始显示目录
        #dlg.DoModal()

        #self.file_path_1 = dlg.GetPathName()  # 获取选择的文件名称
        #jieba.load_userdict(self.file_path_1)
        #该词词性不为“nr”或者词长度小于2
        #with codecs.open(self.file_path, "r", "utf8") as f:
            #for line in f.readlines():#读取整篇文章
                #poss = pseg.cut(line)  #分词，返回词性
                #lineNames.append([])  #为本段增加一个人物列表
                #for w in poss:
                    #if w.flag != 'nr' or len(w.word) < 2:
                        #continue   #当分词小于2或者不为“nr”的被认为不为人名
                    #lineNames[-1].append(w.word)  #为当前段的环境增加一个人物
                    #if names.get(w.word) is None:  #如果某人物不在人物字典中
                        #names[w.word] = 0
                        #relationships[w.word] = {}
                    #names[w.word] += 1
        #创建角色关系（边）
        #对于linenames中每一行，为该行中出现的所有人物两两相连。如果两个人物之间尚未有过建立，则
        #将新建的边权值设为1，否则将已存在的边权值加1
        #for line in lineNames:
            #for name1 in line:
                #for name2 in line:
                    #if name1 == name2:
                        #continue
                    #if relationships[name1].get(name2) is None:
                        #relationships[name1][name2] = 1
                    #else:
                        #relationships[name1][name2] = relationships[name1][name2] + 1
        #由于分词的不准确会出现很多不是人名的名词，会导致冗余的边，于是设置权值大于10的边不冗余
        #with codecs.open("People_node.txt", "w", "utf8") as f:
             #f.write("ID Lavel Weight\r\n")
            #for name, times in names.items():
                 #if times > 10:
                     #f.write(name + " " + name + " " + str(times) + "\r\n")

        #with codecs.open("People_edge.txt", "w", "utf8") as f:
            #f.write("Source Target Weitht\r\n")
            #for name, edges in relationships.items():
                #for v, w in edges.items():
                    #if w > 100:
                        #f.write(name + " " + v + " " + str(w) + "\r\n")

        file_name1 = self.file_path[:-4]
        time.sleep(5)
        top2 = tkinter.Toplevel()
        top2.title("人物关系图")
        image = Image.open( "cha.png")
        img = ImageTk.PhotoImage(image)
        canvas2 = tkinter.Canvas(top2, width=image.width, height=image.height, bg='white')
        canvas2.create_image(0, 0, image=img, anchor="nw")
        canvas2.create_image(image.width, 0, image=img, anchor="nw")
        canvas2.pack()
        top2.mainloop()

        #分析词性
        ##word = open(self.file_path, 'rb').read()
        ##words = pseg.cut(word)
        ##pseg.cut(words)
        ##for w in words:
            ##print(w.word, w.flag)

    def draw_feels_times(self):
        allFeels = self.db.show.find({}, {"_id": 0})
        allFeels = list(allFeels)
        frame = pd.DataFrame(allFeels)
        feels = frame['feels'].tolist()
        x_feels = []
        y_times = []
        for x in feels:
            if type(x).__name__ != 'float':
                for y in x:
                    x_feels.append(y)
                    y_times.append(x[y])
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = x_feels
        sizes = y_times
        explode = (0, 0.1, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        #plt.show()
        plt.savefig('作者情感比例.png', bbox_inches='tight')
        plt.close('all')

        top_bar_author = tkinter.Toplevel()
        top_bar_author.title("作者情感比例")
        image = Image.open('作者情感比例.png')
        img = ImageTk.PhotoImage(image)
        canvas2 = tkinter.Canvas(top_bar_author, width=image.width, height=image.height, bg='white')
        canvas2.create_image(0, 0, image=img, anchor="nw")
        canvas2.create_image(image.width, 0, image=img, anchor="nw")
        canvas2.pack()
        top_bar_author.mainloop()

    def draw_max_posion(self):
        def get_sort_rank(sort):
            sortAll = self.db.speech.find({}, {"_id": 0})
            sortAll = list(sortAll)
            frame = pd.DataFrame(sortAll)

            areas = frame[sort].tolist()
            result = []
            for a in areas:
                if type(a).__name__ != 'float':
                    result.append(a)
            address_couter = Counter(result.pop())
            maxAddress = address_couter.most_common(10)
            return maxAddress;
        a = get_sort_rank("ns")
        x_postion, y_postion = [x[0] for x in a], [x[1] for x in a]
        plt.axis([0, 10, 0, max(y_postion)])
        plt.title("唐诗中常见得十大地点", fontsize=24)
        plt.xlabel("地点名", fontsize=14)
        plt.ylabel("出现次数", fontsize=14)
        plt.plot(x_postion, y_postion, linewidth=1)
        #plt.show() #将图片保存
        plt.savefig('唐诗中常见的十大地点.png', bbox_inches='tight')
        plt.close('all')

        top_bar_site = tkinter.Toplevel()
        top_bar_site.title("常见的十大地点")
        image = Image.open('唐诗中常见的十大地点.png')
        img = ImageTk.PhotoImage(image)
        canvas1 = tkinter.Canvas(top_bar_site , width=image.width, height=image.height, bg='white')
        canvas1.create_image(0, 0, image=img, anchor="nw")
        canvas1.create_image(image.width, 0, image=img, anchor="nw")
        canvas1.pack()
        top_bar_site.mainloop()

    # 十大作者出现次数
    def draw_max_author(self):

        allAuthor = self.db.show.find({}, {"_id": 0})
        allAuthor = list(allAuthor)
        frame = pd.DataFrame(allAuthor)
        author = frame['author'].tolist()
        x_authors = []
        y_times = []
        for x in author:
            if type(x).__name__ != 'float':
                for y in x:
                    x_authors.append(y[0])
                    y_times.append(y[1])

        # 折线 饼状 柱状
        plt.bar(x_authors, y_times, 0.2, alpha=1, color='b')  # 5 color 4 透明度 3 0.9
        plt.xticks(rotation=45)
        #plt.show()
        plt.savefig('十大作者的出现次数.png', bbox_inches='tight')
        plt.close('all')

        top_bar_author = tkinter.Toplevel()
        top_bar_author.title("十大作者频次图")
        image = Image.open('十大作者的出现次数.png')
        img = ImageTk.PhotoImage(image)
        canvas2 = tkinter.Canvas(top_bar_author, width=image.width, height=image.height, bg='white')
        canvas2.create_image(0, 0, image=img, anchor="nw")
        canvas2.create_image(image.width, 0, image=img, anchor="nw")
        canvas2.pack()
        top_bar_author.mainloop()

    '''
        #pygal生成svg图像
        hist=pygal.Bar()
        hist.title="作诗最多得十大作者"
        hist.x_labels=x_authors
        hist.x_title="姓名"
        hist.y_title="出现次数"
        hist.add('次数',y_times)
        hist.render_to_file('作诗最多得十大作者.svg');
        #_x,_y=[x[] for x inauthors['author']  ],[authors['author']    ]
    '''

    def draw_season_times(self):
        allSeason = self.db.show.find({}, {"_id": 0})
        allSeason = list(allSeason)
        frame = pd.DataFrame(allSeason)
        seasons = frame['season'].tolist()
        x_seasons = []
        y_times = []
        for x in seasons:
            if type(x).__name__ != 'float':
                for y in x:
                    x_seasons.append(y)
                    y_times.append(x[y])
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = x_seasons
        sizes = y_times
        explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

        fig1, ax1 = plt.subplots()
        ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
                shadow=True, startangle=90)
        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        # plt.show()
        plt.savefig('季节饼图.png', bbox_inches='tight')
        plt.close('all')

        top_bar_season = tkinter.Toplevel()
        top_bar_season.title("季节饼图")
        image = Image.open('季节饼图.png')
        img = ImageTk.PhotoImage(image)
        canvas3 = tkinter.Canvas(top_bar_season, width=image.width, height=image.height, bg='white')
        canvas3.create_image(0, 0, image=img, anchor="nw")
        canvas3.create_image(image.width, 0, image=img, anchor="nw")
        canvas3.pack()
        top_bar_season.mainloop()

#if __name__=='__main__':
      #app = Application()
      # 设置窗口标题:
      #app.master.title('文学作品鉴赏')
      # 主消息循环:
      #app.mainloop()
      #root.mainloop()